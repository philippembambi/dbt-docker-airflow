from datetime import datetime, timedelta
from airflow import DAG
from docker.types import Mount

from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator

from airflow.providers.docker.operators.docker import DockerOperator
import subprocess
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator

CONN_ID = ''


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
}


dag = DAG(
    'elt_and_dbt',
    default_args=default_args,
    description='An ELT workflow with dbt',
    start_date=datetime(2023, 10, 3),
    catchup=False,
)

t1 = AirbyteTriggerSyncOperator(
    task_id='airbyte_posgres_postgres',
    airbyte_conn_id='airbyte',
    connection_id=CONN_ID,
    asynchronous=False,
    wait_second=3,
    dag=dag,
)

t2 = DockerOperator(
    task_id='dbt_run',
    image='ghcr.io/dbt-labs/dbt-postgres:1.4.7',
    command=[
        "run",
        "--profiles-dir",
        "/root",
        "--project-dir",
        "/dbt",
        "--full-refresh"
    ],
    auto_remove=True,
    docker_url="unix://var/run/docker.sock",
    network_mode="bridge",
    mounts=[
        Mount(source='//home/mgr_phil/Documents/ecommerce_dbt',
              target='/dbt', type='bind'),
        Mount(source='/home/mgr_phil/.dbt', target='/root', type='bind'),
    ],
    dag=dag
)

t1 >> t2