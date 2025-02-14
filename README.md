# mlproject

# workflow

update config.yaml
update schema.yaml
update params.yaml
update the entity
update the configuration manager in src config
update the components
update the pipeline
update the main.py
update the app.py

clone the repository
https://github.com/MANOJKUMAR0616/mlproject

# step1: create virtual environment

python -m venv mlp

mlp\Scripts\activate

# install the requirements

pip install -r requirements.txt

# AWS CICD Deployment with Github Actions

# 1. login to AWS console

# 2. create IAM user for deployment

    # 1. ECR: Elastic Container Registry to save docker image in AWS

    # 2. EC2: virtual machine

# 3. Description
    # 1. build docker image of the source code

    # 2. push your docker image to ECR

    # 3. launch EC2

    # 4. pull your image from ECR to EC2

    # 5. launch docker image in EC2

    # policy:

    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess

    url: 149536485590.dkr.ecr.ap-south-1.amazonaws.com/mlproject


