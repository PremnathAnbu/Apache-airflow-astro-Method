from airflow import DAG
from airflow.sdk import task
from datetime import datetime

#define the DAG
with DAG(
    dag_id='math_operations_taskflow',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',
    catchup=False,
   ) as dag:
    @task
    def start_number():
        initial_value = 10
        print(f"Starting number: {initial_value}")
        return initial_value
    @task
    def add_five(number):
        result = number + 5
        print(f"Adding 5: {number} + 5 = {result}")
        return result
    @task
    def multiply_two(number):
        result = number * 2
        print(f"Multiplying by 2: {number} * 2 = {result}")
        return result
    @task
    def subtract_three(number):
        result = number - 3
        print(f"Subtracting 3: {number} - 3 = {result}")
        return result
    @task
    def square_number(number):
        result = number ** 2
        print(f"Squaring the number: {number}^2 = {result}")
        return result
    @task
    def print_result(result):
        print(f"Final result is: {result}")
    # Define task dependencies   
    start_value=start_number()
    added_value=add_five(start_value)
    multiplied_value=multiply_two(added_value)
    subtracted_value=subtract_three(multiplied_value)
    squared_value=square_number(subtracted_value)
    print_result(squared_value)