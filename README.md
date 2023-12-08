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
uses the `from_country` column to calculate the averages.

----

## Installation

Pre-requirements:
- pip
- (anaconda or other virtual environment)

It is recommended to create firstly a virtual environment of your choice (e.g. conda):

```bash
conda create --name challenge python=3.8
```

Afterwards activate it:

```
conda activate challenge
```

Next install the desired release with pip:

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
python run.py \
--project-tiles-path /path/to/ride-data.csv
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
The `country_code` is a two-letter country code (conforming to [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).


----

## CHANGELOG

See [CHANGELOG.md](CHANGELOG.md)

----

## Contact

Larissa Magalhaes ([larissa@challenge.com](mailto:larissa@chalenge.com))

