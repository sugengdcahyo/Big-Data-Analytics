from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('spark_job', default_args=default_args, schedule_interval=timedelta(days=1))

t1 = BashOperator(
    task_id='run_spark',
    bash_command='./run_spark.sh ',
    dag=dag)
