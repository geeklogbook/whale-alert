import boto3
from airflow import DAG
from airflow.operators.python import PythonOperator
from botocore.exceptions import NoCredentialsError, EndpointConnectionError
from datetime import datetime

def check_s3_connection():
    try:
        s3_client = boto3.client(
            's3',
            endpoint_url='http://data-lake:9000',
            aws_access_key_id='minio',
            aws_secret_access_key='minio123',
            region_name='us-east-1',
            config=boto3.session.Config(signature_version='s3v4')
        )

        response = s3_client.list_buckets()
        print("Connection to MinIO is successful!")
        print("Buckets: ", [bucket['Name'] for bucket in response['Buckets']])

    except NoCredentialsError:
        print("Error: No valid credentials provided!")
    except EndpointConnectionError:
        print("Error: Unable to connect to the endpoint!")
    except Exception as e:
        print(f"An error occurred: {e}")

with DAG(
    'test_minio_connection',
    schedule_interval=None,
    start_date=datetime(2025, 1, 31), 
    catchup=False,
    tags=["infrastructure", "data-lake"]
) as dag:
    check_connection_task = PythonOperator(
        task_id='check_connection',
        python_callable=check_s3_connection
    )