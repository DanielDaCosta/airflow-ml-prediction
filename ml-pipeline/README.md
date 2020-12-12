# Deploy ETL to ECS Fargate

# Code

The XGboost model used in this ECS task can be retrieved in more detail on https://github.com/DanielDaCosta/energy-forecast

The final model has an forecasting horizon (The number of time periods to forecast into the future) of 48 time periods which corresponds to 2 days ahead forecasting.

# AWS

## Push Image to ECR

Create a Private ECR repository

```bash
$ docker images

$ docker tag e9ae3c220b23 aws_account_id.dkr.ecr.region.amazonaws.com/my-web-app

$ docker push aws_account_id.dkr.ecr.region.amazonaws.com/my-web-app
```

## Create ECS Cluster

You can check this tutorial on how to set-up an ECS Fargate Cluster: https://medium.com/underscoretec/deploy-your-own-custom-docker-image-on-amazon-ecs-b1584e62484

# References

- https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html