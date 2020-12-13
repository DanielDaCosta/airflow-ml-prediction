# Airflow ETL
Building an ETL pipeline orchestrated by Airflow

## Building Airflow on Docker

```bash
docker pull puckel/docker-airflow
```

Building the image (installing *boto3* for AWS configurations):

```bash 
docker build -t ml-pipeline .
```

We will create a volume that maps the directory on our local machine where we’ll hold DAG definitions, and the locations where Airflow reads them on the container with the following command:

```bash
docker run -d -p 8080:8080 -v /Users/danieldacosta/Documents/GitHub/airflow-etl/dags:/usr/local/airflow/dags ml-pipeline
```

## s3
On this example we are using two buckets: one for storing the moldel .sav and inputs (.csv), and another one for storing the model output.

- READ_BUCKET=ml-sls-deploy-prd
- READ_DATA_PATH=data
- READ_MODELS_PATH=models
- WRITE_BUCKET=ml-sls-deploy-prd-results
- WRITE_DATA_PATH=results

## Deploy your ECS cluster
You will need to create the following objects:

- **Create a Cluster**. Choose `Network only`. This configuration is built using Fargate Tasks: *the Fargate launch type allows you to run your containerized applications without the need to provision and manage the backend infrastructure. When you run a task with a Fargate-compatible task definition, Fargate launches the containers for you.*

- **Task Definition**. The creation of your container blueprint. You'll need to create a `Task Role`: IAM Role that tasks can use to make API requests to authorized AWS services; Since our container is reading and writing to/from s3, it will need these permissions. You will also need to create a `Task Execution Role`: an IAM that helps pulling images from your docker register, we are using ECR here.

- **Add a Container**. You'll need to deploy your container to ECS Fargate. You can use the Docker image on folder 'ml-pipeline' as an example.

I recommend that you follow this tutorial: https://towardsdatascience.com/step-by-step-guide-of-aws-elastic-container-service-with-images-c258078130ce. 

## Set Environment variables on Airflow

You will need to set up your AWS credentials and ECS variables on the Airflow Console
![Airflow_varibales](Images/Airflow_Variables.png)

## Run DAG

Once everything set up you can Trigger your DAG manually and check if everthing went well.

# References

- http://www.marknagelberg.com/getting-started-with-airflow-using-docker/
- https://towardsdatascience.com/step-by-step-guide-of-aws-elastic-container-service-with-images-c258078130ce
- https://headspring.com/2020/06/17/orchestrating-and-running-multiple-tasks-in-aws-via-airflow/
