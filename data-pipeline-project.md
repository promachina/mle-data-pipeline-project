# Data Pipeline Project

In this project you are going to build a data pipeline that is processing the `Green Taxi Trips` of the NYC Taxi Trip Dataset. 

1. The first task is to write a script that is directly uploading the data of the first 3 months of the year 2021 to a GCS bucket.

2. The second task is to write a ETL or ELT pipeline that is taking the data from the GCS bucket and that is processing the data and calculating the revenue per day.  This can be done in the Google Cloud or on your local machine.

Bonus task if you have the time:

1. Use prefect for the Workflow Orechestration.


## Questions:

1. What are the steps you took to complete the project?
- Copy-paste python templates from batch processing module and refactor for project task
- Data upload
- Spark job on GCP
- Setup BigQuery

2. What are the challenges you faced?
I tried to set up a workflow orchestration with the managed Airflow service on GCP but ran into many issues during the deployement.

3. What are the things you would do differently if you had more time?
Set it as a DAG on Airflow.
## Submission:

Please submit your solution as a link to a github repository. The repository should contain the scripts and a README.md file that is answering the questions above.


1. upload green taxi trips to bucket
2. transform with pyspark: revenue per day
3. load into bigquery
