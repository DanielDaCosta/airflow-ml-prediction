# Airflow ETL
Building an ETL pipeline orchestrated by Airflow

```bash
docker pull puckel/docker-airflow
```

Building the image (installing *boto3* for AWS configurations):

```bash 
docker build -t ml-pipeline .
```

We will create a volume that maps the directory on our local machine where we’ll hold DAG definitions, and the locations where Airflow reads them on the container with the following command
```bash
docker run -d -p 8080:8080 -v /Users/danieldacosta/Documents/GitHub/airflow-etl/dags:/usr/local/airflow/dags ml-pipeline
```


# References

- http://www.marknagelberg.com/getting-started-with-airflow-using-docker/
- https://towardsdatascience.com/step-by-step-guide-of-aws-elastic-container-service-with-images-c258078130ce
- https://headspring.com/2020/06/17/orchestrating-and-running-multiple-tasks-in-aws-via-airflow/
