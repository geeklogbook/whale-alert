from datetime import datetime
from airflow.decorators import task 
from airflow import DAG
import pendulum

with DAG(
    dag_id="using_function_v1",
    schedule=None,
    start_date=pendulum.datetime(2023,1,1,tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:

    @task()
    def return_string_function():
        return "Hello World"

    return_string_function()