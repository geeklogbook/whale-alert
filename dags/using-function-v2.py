from datetime import datetime
from airflow.decorators import task, dag


@dag(
    dag_id="using_function_v2",
    schedule_interval="@daily",
    start_date=datetime(2022, 1, 1),
    catchup=False,
    default_args={
        "retries": 2,
    },
    tags=['example'])

def using_function_v2():

    @task()
    def return_string_function():
        return "Hello World"

    return_string_function()

using_function_v2 = using_function_v2()