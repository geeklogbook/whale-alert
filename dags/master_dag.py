from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.dummy import DummyOperator
from airflow.utils.dates import days_ago
from airflow import DAG

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1), 
}

dag = DAG(
    'master_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    tags=['orchestration']
)

start = DummyOperator(
    task_id='start',
    dag=dag,
)

trigger_test_run = TriggerDagRunOperator(
    task_id='trigger_test_run',
    trigger_dag_id='test_run_dag',
    wait_for_completion=True,
    execution_date='{{ execution_date }}',
    reset_dag_run=True,
    dag=dag,
)

trigger_minio = TriggerDagRunOperator(
    task_id='trigger_minio',
    trigger_dag_id='test_minio_connection',
    wait_for_completion=True,
    execution_date='{{ execution_date }}',
    reset_dag_run=True,
    dag=dag,
)

trigger_whale_alert = TriggerDagRunOperator(
    task_id='trigger_whale_alert',
    trigger_dag_id='whale_alert',
    wait_for_completion=True,
    execution_date='{{ execution_date }}',
    reset_dag_run=True,
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

start >> trigger_test_run >> trigger_minio >> trigger_whale_alert >> end 