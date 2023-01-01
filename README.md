# TDEI-Python-Template-MS
## Introduction 
This micro-service acts as example for creating all the new micro-services for TDEI project in Python. The reference code can be used in other micro-services.

## Requirements
python 3.10

## How to run the project

#### Create virtual env

`python3.10 -m venv .venv`

`source .venv/bin/activate`

#### Install requirements

`pip install -r requirements`

#### Install Python MS Core Package

`pip install -i https://test.pypi.org/simple/ python-ms-core`


### Run the Server

`uvicorn src.main:app --reload`

### Run the examples

`python src/example.py`