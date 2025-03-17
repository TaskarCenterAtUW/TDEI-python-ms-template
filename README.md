# TDEI-Python-Template-MS
## Introduction 
This micro-service acts as example for creating all the new micro-services for TDEI project in Python. The reference code can be used in other micro-services.

This template has the following
- [config.py](./src/config.py)
This file is used to maintain all the configurations required for running the application.

- [processing_service.py](./src/processing_service.py)
This file and the classes within are used to interact with the service bus messages (incoming and outgoing)

- [storage_service.py](./src/storage_service.py)
This file and the classes within are used to interact with the remote file storage.


## Requirements
python 3.10

## How to run the project with Python3.10

#### Create virtual env

`python3.10 -m venv .venv`

`source .venv/bin/activate`

#### Install requirements

`pip install -r requirements.txt`


#### Set up env file, create a .env file at project root level 

```
PROVIDER=Azure
QUEUECONNECTION=Endpoint=sb://xxxxxxxxxxxxx
STORAGECONNECTION=DefaultEndpointsProtocol=https;xxxxxxxxxxxxx
```
Note: Replace the endpoints with the actual endpoints

#### Configure the incoming and outgoing subscription and topic 
Change the following parameters in [config.py](./src/config.py)
```python
incoming_topic: str = 'incoming-topic' # Change this
incoming_topic_subscription: str = 'incoming-sub' # Change this
outgoing_topic: str = 'outgoing-topic' # Change this
```

### Run the Server

`uvicorn src.main:app --reload`



## How to run the project with Anaconda

#### Create virtual env
Create a virtual env using Anaconda, see here https://docs.anaconda.com/navigator/tutorials/manage-environments/

Go to project location and activate the conda environment

#### Install requirements

`pip install -r requirements.txt`

#### Set up environment variables 
Run the below commands to setup the environment variables
```
export PROVIDER="Azure"
export QUEUECONNECTION="Endpoint=sb://xxxxxxxxxxxxx"
export STORAGECONNECTION="DefaultEndpointsProtocol=https;xxxxxxxxxxxxx"
```
Note: Replace the endpoints with the actual endpoints

### Run the Server

`uvicorn src.main:app --reload`

