from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import Response
from python_ms_core import Core
from src.processing_service import ProcessingService

app = FastAPI()


class OctetStreamResponse(Response):
    media_type = 'application/octet-stream'


@app.get('/')
def root():
    return {'Hello': 'World'}


@app.get('/ping')
def ping():
    return {'msg': 'Ping Successful'}

@app.on_event("startup")
async def startup_event():
    try:
        app.core = Core()
        app.processing_service = ProcessingService(app.core)
        app.processing_service.start_listening()
    except Exception as e:
        print(e)
        print(e)
        print('\n\n\x1b[31m Application startup failed due to missing or invalid .env file \x1b[0m')
        print('\x1b[31m Please provide the valid .env file and .env file should contains following parameters\x1b[0m')
        print()
        print('\x1b[31m POSTGRES_HOST=xxxx \x1b[0m')
        print('\x1b[31m POSTGRES_USER=xxxx \x1b[0m')
        print('\x1b[31m POSTGRES_PASSWORD=xxxx \x1b[0m')
        print('\x1b[31m POSTGRES_DB=xxxx \x1b[0m')
        print('\x1b[31m POSTGRES_PORT=xxxx \x1b[0m')
        print('\x1b[31m MONGO_DB_CONNECTION=xxxx \x1b[0m')
        print('\x1b[31m REQUEST_TOPIC=xxxx \x1b[0m')
        print('\x1b[31m REQUEST_SUBSCRIPTION=xxxx \x1b[0m')
        print('\x1b[31m RESPONSE_TOPIC=xxxx \x1b[0m')
        print('\x1b[31m QUEUECONNECTION=xxxx \x1b[0m')
        parent_pid = os.getpid()
        parent = psutil.Process(parent_pid)
        for child in parent.children(recursive=True):
            child.kill()
        parent.kill()


@app.get('/download', response_class=OctetStreamResponse)
async def download():
    storage_client = Core.get_storage_client()
    storage_container = storage_client.get_container(name='gtfspathways')
    file_lists = storage_container.list_files()
    first_file = file_lists[1]
    return Response(
        content=first_file.get_stream(),
        media_type=first_file.mimetype,
        headers={'Content-Disposition': f'attachment; filename={first_file.name}'},
        status_code=200
    )


@app.post('/logs')
async def logs(info : Request):
    req_info = await info.json()
    return req_info
