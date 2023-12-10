# Challenge
API implementing the calculation of the average ride duration in seconds per country.

## Project Hierarchy

``` bash
Challenge
   ├── app
   │   ├── __init__.py
   │   ├── app.py
   │   ├── args.py
   │   └── templates
   │       └── index.html
   │
   ├── tests
   │   └── __init__.py
   │   └── test_app.py
   │
   ├── run.py
   ├── CHANGELOG.md
   ├── README.md
   └── requirements.txt

```
----

## Description

The purpose of this module is to implement an API that calculates the average ride duration in seconds per
country. The input csv data should contains two country columns `from_country` and  `to_country`. This module 
uses the `from_country` and `duration` columns to calculate the averages. With the `duration` column containing
the duration of the ride in seconds and the `from_country` column containing the two-letter country code 
(conforming to [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).

----

## Installation

Pre-requirements:
- pip
- (anaconda or other virtual environment)

Clone the git repository:

```bash
git clone https://github.com/derezendemagalhaes/challenge.git
```

It is recommended to create firstly a virtual environment of your choice (e.g. conda):

```bash
conda create --name challenge python=3.8
```

Afterwards activate it:

```
conda activate challenge
```

Next navigate to the challenge root directory and install the environment requirements with pip:

```bash
pip install -r requirements.txt
```

## Usage

For an overview about all input arguments and their meanings, navigate to the challenge directory and run:
```bash
python run.py -h
```

| argument             | required | type     | example                                                                               |  notes                                                                   | 
|:---------------------|:---------|:---------|:--------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| csv-data-path   | yes      | Path or S3Path | /path/to/file/ride-data.csv or s3://challenge-flix/ride-data.csv     |                        



Example command to initialize the API:

```bash
python run.py --ride-data-path ride-data.csv
```
The API index can be called via browser on:

```bash
http://127.0.0.1:5000/
```

Or via curl:
```bash
curl http://127.0.0.1:5000/
```

To access the country average ride duration in seconds the `country_code` should be provided as such:
```bash
curl http://127.0.0.1:5000/<country_code>
```
----
## Deployment
For the deployment of the Flask API on AWS Elastic Beanstalk using Docker and Amazon Elastic Container Registry (ECR), a set of essential scripts and configuration files has been developed. These resources aim to automate and simplify the deployment process. To deploy the following set up would be required:

1. Configure the Dockerfile and make the `deploy.sh` script executable:
```bash
chmod +x deploy.sh
```
2. AWS Elastic Beanstalk was configured on: `.ebextensions/01_flask.config`
3. Add the references to the correct ECR repository URI to the Dockerfile.
4. Run the deployment script to deploy:
```bash
./deploy.sh
```

## Changelog

See [CHANGELOG.md](CHANGELOG.md)

----

## Contact

Larissa Magalhaes ([larissa@challenge.com](mailto:larissa@chalenge.com))

