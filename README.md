# airflow-etl
Building an ETL pipeline orchestrated by Airflow

```
docker pull puckel/docker-airflow
```

We will create a volume that maps the directory on our local machine where we’ll hold DAG definitions, and the locations where Airflow reads them on the container with the following command:

```
docker run -d -p 8080:8080 -v /path/to/dags/on/your/local/machine/:/usr/local/airflow/dags  puckel/docker-airflow webserver
```


# References

- http://www.marknagelberg.com/getting-started-with-airflow-using-docker/