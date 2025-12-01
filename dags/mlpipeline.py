from airflow import DAG
# from airflow.operators.python import PythonOperator
# from airflow.operators.python import PythonOperator
# airflow.providers.standard.operators.python.PythonOperator
from airflow.providers.standard.operators.python import PythonOperator 

from datetime import datetime, timedelta

def preprocess_data():
    print("Preprocessing data...")
    
def train_model():
    print("Training model...")
    
def evaluate_model():
    print("Evaluating model...")

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}   
#define the dag
with DAG(
    'ml_pipeline',
    start_date=datetime(2025, 1, 1),
    schedule='@daily',
    default_args=default_args,
    catchup=False,
   ) as dag:
    preprocess_task = PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data,
    )
    train_task = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )
    evaluate_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model,
    )
    preprocess_task >> train_task >> evaluate_task  # Define task dependencies

