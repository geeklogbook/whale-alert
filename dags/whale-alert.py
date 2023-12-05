from datetime import datetime, timedelta
from airflow import DAG
# from bs4 import BeautifulSoup
import logging
from airflow.operators.python_operator import PythonOperator


default_args = {
    'owner': 'jc',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'whale-alert',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Set the execution interval, in this case, daily
)


def whale_alert_extraction():
    try:
        # Your logic for whale alert extraction here
        logging.info("Whale Alert Extraction completed successfully.")
        return "Whale Alert Extraction"
    except Exception as e:
        logging.error(f"Error in Whale Alert Extraction: {str(e)}")
        raise


# Create a PythonOperator task that will execute the hello_world_function
whale_alert_task = PythonOperator(
    task_id='whale_alert_extraction',
    python_callable=whale_alert_extraction,
    dag=dag
)

# Set the task dependencies (in this case, there are no dependencies)
whale_alert_extraction