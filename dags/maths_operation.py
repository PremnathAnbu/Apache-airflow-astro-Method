from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator 
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

# Define function for each task
def start_number(**context):
    context['ti'].xcom_push(key='current_number', value=10)
    print("starting number 10")
    
def add_five(**context):
    ti = context['ti']
    number = ti.xcom_pull(task_ids='start_number_task', key='current_number') # Pull the number from the previous task
    result = number + 5
    print(f"Adding 5: {number} + 5 = {result}")
    ti.xcom_push(key='current_number', value=result)

def multiply_two(**context):
    ti = context['ti']
    number = ti.xcom_pull(task_ids='add_five_task', key='current_number')
    result = number * 2
    print(f"Multiplying by 2: {number} * 2 = {result}")
    ti.xcom_push(key='current_number', value=result)

def subtract_three(**context):
    ti = context['ti']
    number = ti.xcom_pull(task_ids='multiply_two_task', key='current_number')
    result = number - 3
    print(f"Subtracting 3: {number} - 3 = {result}")
    ti.xcom_push(key='current_number', value=result)

def square_number(**context):
    ti = context['ti']
    number = ti.xcom_pull(task_ids='subtract_three_task', key='current_number')
    result = number ** 2
    print(f"Squaring the number: {number}^2 = {result}")
    ti.xcom_push(key='final_result', value=result)

with DAG(
    'maths_operation_dag',
    start_date=datetime(2025, 1, 1),
    schedule='@daily',
    default_args=default_args,
    catchup=False,
   ) as dag:
    start_number_task = PythonOperator(
        task_id='start_number_task',
        python_callable=start_number,
        op_kwargs={},
    )
    
    add_five_task = PythonOperator(
        task_id='add_five_task',
        python_callable=add_five,
        op_kwargs={},
    )
    
    multiply_two_task = PythonOperator(
        task_id='multiply_two_task',
        python_callable=multiply_two,
        op_kwargs={},
    )
    
    subtract_three_task = PythonOperator(
        task_id='subtract_three_task',
        python_callable=subtract_three,
        op_kwargs={},
    )
    
    square_number_task = PythonOperator(
        task_id='square_number_task',
        python_callable=square_number,
        op_kwargs={},
    )
    start_number_task >> add_five_task >> multiply_two_task >> subtract_three_task >> square_number_task  # Define task dependencies