# Terraform Setup for Airflow DAGs Deployment

## Description

This Terraform configuration simplifies the deployment process of custom Airflow Directed Acyclic Graphs (DAGs) by automating the creation of local files from provided templates and triggering Airflow DAG refresh to seamlessly integrate the new DAGs.

The primary aim of this setup is to enhance deployment efficiency and standardize the process across environments. It abstracts manual steps, reducing the likelihood of errors and ensuring a consistent deployment experience.

### Files
#### main.tf: 
Defines the Terraform resources and variables required for deploying custom Airflow DAGs.

#### Variables: 
Define variables for the filenames of the new DAGs, their corresponding IDs, and template DAG filenames.

### Resources

#### local_file: 
Creates local files for each new DAG based on provided filenames and templates.

#### null_resource: 
Triggers Airflow DAG refresh to load the new DAGs.
#### variables.tfvars: 
Contains the values for the variables defined in main.tf.
#### docker-compose.yml: 
Defines the services required for running Airflow.

### Services:

#### airflow-test: 
Runs the Airflow container with volume mounts for DAGs and exposes port 8080 for web UI access.
#### Dockerfile: 
Sets up the Airflow environment for running custom DAGs.

#### Base Image: 
Uses the apache/airflow:latest base image.

#### Setup: 
Installs Git to allow for Git-based operations in DAGs.

### Usage
Modify the variables in variables.tfvars to specify the filenames for new DAGs, their IDs, and template filenames. If you want to create a new DAG, add its filename to the end of the existing dag_filenames, its ID to the end of dag_ids, and its template filename to the end of template_filenames. 

            dag_filenames  = [
                "welcome_john_dag.py",
                "goodbye_john_dag.py"
            ]

            dag_ids  = [ 
                "welcome_john",
                "goodbye_john"
            ]

            template_filenames = [ 
                "welcome_dag",
                "goodbye_dag"
            ]

If you want to create a new template dag, make sure to create the new template in the airflow/template_dags directory and use the other template dags as refrence.

#### Make sure you are in the Terraform directory.
#### Run terraform init to initialize Terraform.
#### Run terraform apply to create local DAG files and trigger Airflow DAG refresh.

This setup ensures that the arrays dag_filenames, dag_ids, and template_filenames stay synchronized, with each index corresponding to a specific DAG. Make sure to update the variables accordingly whenever adding or removing DAGs.



## If you need to install Terraform and Airflow follow the steps below

### Terraform Installation:
#### Download Terraform:
    1. Visit the Terraform website and download the appropriate version of Terraform for your operating system (Windows, macOS, Linux).

    2. Extract the Terraform Archive:
        After downloading the Terraform archive, extract it to a directory of your choice.

    3. Add Terraform to PATH:
        Add the directory containing the Terraform binary to your system's PATH environment variable. This step allows 
        you to run Terraform commands from any directory in your terminal or command prompt.

    4. Verify the Installation:
         Open a new terminal or command prompt window and run the command terraform --version to verify that Terraform 
         is installed correctly. 
                You should see the Terraform version number printed to the console.

#### Airflow Installation:
#### Install Python:
    If you haven't already, install Python on your system. Airflow requires Python to run.
#### Install Apache Airflow:
    1. You can install Airflow using pip, Python's package manager. Run the following command:
        pip install apache-airflow

    2. Initialize Airflow Database:
        After installing Airflow, initialize its database by running the following command:
        airflow db init

    3. Start the Airflow Web Server:
        Once the database is initialized, start the Airflow web server by running:
        airflow webserver --port 8080

    4. Start the Airflow Scheduler:
        In a separate terminal or command prompt window, start the Airflow scheduler by running:
        airflow scheduler

    5. Access Airflow Web UI:
        Open a web browser and navigate to localhost:8080 (or the specified port) to access the Airflow web UI.
            You'll be prompt to enter user information:
            - Username by default is: admin
            - Password can be found in the directory below:
                airflow/airflow-webserver.pid

**
These steps provide a basic setup for both Terraform and Apache Airflow. Depending on your environment and requirements, additional configurations may be necessary. Always refer to the official documentation for the most up-to-date installation instructions and best practices.
**
