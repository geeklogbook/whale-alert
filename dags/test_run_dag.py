from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'test_run_dag',
    default_args=default_args,
    schedule_interval=None, 
)

def hello_world_function():
    print("Hello, Airflow!")

hello_world_task = PythonOperator(
    task_id='test_run_dag',
    python_callable=hello_world_function,
    dag=dag,
)

hello_world_task