# Data Pipeline Project

Please do not fork this repository, but use this repository as a template for your refactoring project. Make Pull Requests to your own repository even if you work alone and mark the checkboxes with an x, if you are done with a topic in the pull request message.

## Project for today
The task for today you can find in the [data-pipeline-project.md](data-pipeline-project.md) file.

## Setup env
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

## Upload taxi data to bucket
python src/data_ingestion.py --sa_path probable-sunup-390815-1df27c899017.json --bucket taxifisch --project_id probable-sunup-390815

## Upload spark job to bucket
gsutil cp src/revenue_report.py gs://taxifisch/code/

## Configure spark job in dataproc cluster
Main python file: 
gs://taxifisch/code/revenue_report.py

Spark JAR file:
gs://taxifisch/code/spark-bigquery-with-dependencies_2.13-0.31.1.jar

Arguments:
--input_green=gs://taxifisch/green_taxi/*.parquet
--output=gs://taxifisch/output/
--output=probable-sunup-390815.taxifisch.green-taxi

## 



