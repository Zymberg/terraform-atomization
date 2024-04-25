# Define a variable for the new DAG filenames
variable "dag_filenames" {
  description = "List of filenames for the new DAGs"
  type        = list(string)
  default     = []
}

# Define a variable for the new DAG IDs
variable "dag_ids" {
  description = "List of IDs for the new DAGs"
  type        = list(string)
  default     = []
}

# Define a variable for the template DAG filenames
variable "template_filenames" {
  description = "List of filenames for the template DAGs"
  type        = list(string)
  default     = []
}

# Create local_file resources for each new DAG based on the provided filenames
resource "local_file" "custom_dag" {
  count = length(var.dag_filenames)

  filename = "${path.module}/../airflow/dags/${var.dag_filenames[count.index]}"

  content  = templatefile("${path.module}/../airflow/template_dags/${var.template_filenames[count.index]}.py", {
    dag_filename = var.dag_filenames[count.index],
    dag_id       = var.dag_ids[count.index],
  })
}

# Trigger Airflow DAG refresh to load the new DAGs
resource "null_resource" "refresh_airflow_dags" {
  triggers = {
    always_run = timestamp()
  }

  # Execute command to trigger Airflow DAG refresh inside the Docker container
  provisioner "local-exec" {
    command = <<EOT
      docker exec newfolder-airflow-test-1 airflow dags trigger ${join(" ", local_file.custom_dag[*].filename)}
    EOT
    interpreter = ["cmd", "/C"]
  }
}
