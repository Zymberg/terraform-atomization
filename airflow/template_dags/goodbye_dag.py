from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime

# Define your placeholder variables here
message = 'Goodbye!'
dag_id = '${dag_id}'

# Define the DAG
dag = DAG(
    dag_id,
    default_args={'start_date': days_ago(1)},
    schedule_interval='0 23 * * *',
    catchup=False
)

# Define task to print goodbye message
def print_goodbye():
    print(message)

print_goodbye_task = PythonOperator(
    task_id='print_goodbye',
    python_callable=print_goodbye,
    dag=dag
)

# Define task to print current date
def print_date():
    print('Today is {}'.format(datetime.today().date()))

print_date_task = PythonOperator(
    task_id='print_date',
    python_callable=print_date,
    dag=dag
)

# Set task dependencies
print_goodbye_task >> print_date_task
