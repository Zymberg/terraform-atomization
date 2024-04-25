from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
import requests

# Define your placeholder variables here
message = 'Welcome to Airflow!'
dag_id = '${dag_id}'

dag = DAG(
    dag_id,
    default_args={'start_date': days_ago(1)},
    schedule_interval='0 23 * * *',
    catchup=False
)

def print_welcome():
    print(message)

print_welcome_task = PythonOperator(
    task_id='print_welcome',
    python_callable=print_welcome,
    dag=dag
)

def print_date():
    print('Today is {}'.format(datetime.today().date()))

print_date_task = PythonOperator(
    task_id='print_date',
    python_callable=print_date,
    dag=dag
)

def print_random_quote():
    response = requests.get('https://api.quotable.io/random')
    quote = response.json()['content']
    print('Quote of the day: "{}"'.format(quote))

print_random_quote_task = PythonOperator(
    task_id='print_random_quote',
    python_callable=print_random_quote,
    dag=dag
)

# Set the dependencies between the tasks
print_welcome_task >> print_date_task >> print_random_quote_task
