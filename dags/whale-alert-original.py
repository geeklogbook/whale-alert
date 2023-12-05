# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import datetime
# from airflow.decorators import dag, task 
# from airflow.providers.postgres.operators.postgres import PostgresOperator


# import os
# AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')

# @dag(
#     schedule_interval="@daily",
#     start_date=datetime(2022, 1, 1),
#     catchup=False,
#     default_args={
#         "retries": 2,
#     },
#     tags=['example'])
# def whale_alert():

#     @task()
#     def extract():
#         URL = "https://whale-alert.io/whales.html"
#         page = requests.get(URL)
#         soup = BeautifulSoup(page.content, "html.parser")
#         table = soup.find('table', attrs={'class': 'table'})
#         table_body = table.find('tbody')
#         table_rows = table_body.find_all('tr')
#         crypto_dict = {
#             "datetime_utc": [], 
#             "crypto": [], 
#             "known": [], 
#             "unknown": []}
#         current_utc = datetime.utcnow()
#         current_utc_str = current_utc.strftime("%Y%m%d")

#         for x in table_rows:
#             coin = x.find("td").get_text().strip()
#             td_list = x.find_all("td")
#             known = td_list[1].text
#             unknown = td_list[2].text
#             crypto_dict["datetime_utc"].append(current_utc)
#             crypto_dict["crypto"].append(coin)
#             crypto_dict["known"].append(known)
#             crypto_dict["unknown"].append(unknown)
        
#         whale_df = pd.DataFrame.from_dict(crypto_dict)

#         path = f'{AIRFLOW_HOME}/dags/output/{current_utc_str}.csv'
#         whale_df.to_csv(path, index=False)
#         return "scrapped-transformed-enriched-saved"

#     extract()

# whale_alert = whale_alert()