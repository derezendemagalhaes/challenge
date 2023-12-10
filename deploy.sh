#!/bin/bash

# Set your AWS region
export AWS_REGION="your-aws-region"

# Set your Elastic Beanstalk application and environment names
export EB_APPLICATION_NAME="your-application-name"
export EB_ENVIRONMENT_NAME="your-environment-name"

# Set your ECR repository URI
export ECR_REPO_URI="your-ecr-repository-uri"

# Set AWS credentials using environment variables or AWS profiles

# Build and push Docker image to ECR
$(aws ecr get-login --no-include-email --region $AWS_REGION)
docker build -t $ECR_REPO_URI .

# Push the image to ECR
docker push $ECR_REPO_URI

# Deploy to Elastic Beanstalk
eb deploy --region $AWS_REGION

# Update Elastic Beanstalk environment
eb use $EB_ENVIRONMENT_NAME
eb config put --envvars FLASK_ENV=production
eb config put ContainerImage=$ECR_REPO_URI/$EB_ENVIRONMENT_NAME:latest
eb deploy --region $AWS_REGION
