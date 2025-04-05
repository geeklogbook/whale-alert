import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from airflow.decorators import dag, task
import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError

BUCKET_NAME = "whale-alert"
ENDPOINT_URL = "http://data-lake:9000"
ACCESS_KEY = "minio"
SECRET_KEY = "minio123"

@dag(
    schedule="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False,
    default_args={"retries": 2},
    tags=['whale-alert']
)
def whale_alert():

    @task()
    def extract():
        url = "https://whale-alert.io/whales.html"
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        object_name = f"bronze/{timestamp}.csv"

        try:
            soup = BeautifulSoup(requests.get(url).content, "html.parser")
            table_rows = soup.select("table.table tbody tr")

            data = {
                "datetime_utc": [datetime.utcnow()] * len(table_rows),
                "crypto": [row.find("td").text.strip() for row in table_rows],
                "known": [row.find_all("td")[1].text for row in table_rows],
                "unknown": [row.find_all("td")[2].text for row in table_rows]
            }

            csv_data = pd.DataFrame(data).to_csv(index=False)

            s3_client = boto3.client(
                's3',
                endpoint_url=ENDPOINT_URL,
                aws_access_key_id=ACCESS_KEY,
                aws_secret_access_key=SECRET_KEY
            )

            s3_client.put_object(Bucket=BUCKET_NAME, Key=object_name, Body=csv_data)
            return object_name  
        except Exception as e:
            return f"Extraction failed: {e}"

    @task()
    def transform(object_name):
        s3_client = boto3.client(
            's3',
            endpoint_url=ENDPOINT_URL,
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )

        try:
            obj = s3_client.get_object(Bucket=BUCKET_NAME, Key=object_name)
            df = pd.read_csv(obj['Body'])

            for col in ['crypto', 'known', 'unknown']:
                df[col] = df[col].astype(str).str.replace(r'[$,]', '', regex=True).replace('-', '0').astype(float)

            transformed_name = object_name.replace("bronze/", "silver/")
            transformed_csv = df.to_csv(index=False)

            s3_client.put_object(Bucket=BUCKET_NAME, Key=transformed_name, Body=transformed_csv)
            return f"Transformed data saved as {transformed_name}"
        except (BotoCoreError, NoCredentialsError) as e:
            return f"MinIO operation failed: {e}"
        except Exception as e:
            return f"Transformation failed: {e}"

    transform(extract())

whale_alert()