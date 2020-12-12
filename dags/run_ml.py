from airflow import DAG
from airflow.models import Variable
from airflow.contrib.operators.ecs_operator import ECSOperator
import copy
from datetime import datetime, timedelta
# Airflow Variables
awsRegionName = Variable.get('AwsRegionName')
awsCluster = Variable.get('AwsCluster')
awsTaskDefinition = Variable.get('AwsTaskDefinition')
awsNetworkSubnet = Variable.get('AwsNetworkSubnet')
awsContainerName = Variable.get('AwsContainerName')
AIRFLOW_ECS_OPERATOR_RETRIES=2

default_args = {
   'owner': 'ml-pipeline',
   'depends_on_past': False,
   'retries': 0
}

# DAG base information
dag = DAG(
    dag_id='ml-pipeline',
    default_args=default_args,
    schedule_interval=None,
)

# ECS Args
ecs_operator_args_template = {
    'aws_conn_id': 'aws_default',
    'region_name': awsRegionName,
    'launch_type': 'FARGATE',
    'cluster': awsCluster,
    'task_definition': awsTaskDefinition,
    'network_configuration': {
        'awsvpcConfiguration': {
            'assignPublicIp': 'ENABLED',
            'subnets': [awsNetworkSubnet]
        }
    },
    'awslogs_group': '/ecs/' + awsTaskDefinition,
    'awslogs_stream_prefix': 'ecs/' + awsContainerName,
    'overrides': {
        'containerOverrides': [
            {
                'name': awsContainerName,
                'memoryReservation': 500,
            },
        ],
    },
}

ecs_operator_args = copy.deepcopy(ecs_operator_args_template)
ecs_operator = ECSOperator(
    task_id='run_ml',
    dag=dag,
    retries=AIRFLOW_ECS_OPERATOR_RETRIES,
    retry_delay=timedelta(seconds=10),
    **ecs_operator_args
)
