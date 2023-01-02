# TDEI-Python-Template-MS
## Introduction 
This micro-service acts as example for creating all the new micro-services for TDEI project in Python. The reference code can be used in other micro-services.

## Requirements
python 3.10

## How to run the project with Python3.10

#### Create virtual env

`python3.10 -m venv .venv`

`source .venv/bin/activate`

#### Install requirements

`pip install -r requirements.txt`

#### Install Python MS Core Package

`pip install -i https://test.pypi.org/simple/ python-ms-core`

#### Set up env file, create a .env file at project root level 

```
PROVIDER=Azure
LOGGERQUEUE=Endpoint=sb://xxxxxxxxxxxxx
QUEUECONNECTION=Endpoint=sb://xxxxxxxxxxxxx
STORAGECONNECTION=DefaultEndpointsProtocol=https;xxxxxxxxxxxxx
CALLBACK_URL=http://127.0.0.1:8000/logs
```
Note: Replace the endpoints with the actual endpoints

### Run the Server

`uvicorn src.main:app --reload`

### Run the examples

`python src/example.py`


## How to run the project with Anaconda

#### Create virtual env
Create a virtual env using Anaconda, see here https://docs.anaconda.com/navigator/tutorials/manage-environments/

Go to project location and activate the conda environment

#### Install requirements

`pip install -r requirements.txt`

#### Install Python MS Core Package

`pip install -i https://test.pypi.org/simple/ python-ms-core`

#### Set up environment variables 
Run the below commands to setup the environment variables
```
export PROVIDER="Azure"
export LOGGERQUEUE="Endpoint=sb://xxxxxxxxxxxxx"
export QUEUECONNECTION="Endpoint=sb://xxxxxxxxxxxxx"
export STORAGECONNECTION="DefaultEndpointsProtocol=https;xxxxxxxxxxxxx"
export CALLBACK_URL="http://127.0.0.1:8000/logs"
```
Note: Replace the endpoints with the actual endpoints

### Run the Server

`uvicorn src.main:app --reload`

### Run the examples

`python src/example.py`