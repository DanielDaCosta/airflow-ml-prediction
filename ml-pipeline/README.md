# Deploy ETL to ECS Fargate

# Push Image to ECR

Create a Private ECR repository

```
$ docker images

$ docker tag e9ae3c220b23 aws_account_id.dkr.ecr.region.amazonaws.com/my-web-app

$ docker push aws_account_id.dkr.ecr.region.amazonaws.com/my-web-app
```
# References

- https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html