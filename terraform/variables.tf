variable "template_filename" {
  description = "The filename of the template DAG to copy: example: welcome_dag"
  type        = string
  default     = ""
}

# Remove these duplicate variable definitions
# variable "dag_filenames" {
#   description = "List of filenames for the new DAGs"
#   type        = list(string)
#   default     = []
# }

# variable "dag_ids" {
#   description = "List of IDs for the new DAGs"
#   type        = list(string)
#   default     = []
# }
