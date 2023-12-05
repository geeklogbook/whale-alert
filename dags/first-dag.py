from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Define default_args dictionary to specify the default parameters for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define a DAG with the specified default_args
dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Set the execution interval, in this case, daily
)

# Define a Python function that will be executed by the PythonOperator
def hello_world_function():
    print("Hello, Airflow!")

# Create a PythonOperator task that will execute the hello_world_function
hello_world_task = PythonOperator(
    task_id='hello_world_task',
    python_callable=hello_world_function,
    dag=dag,
)

# Set the task dependencies (in this case, there are no dependencies)
hello_world_task