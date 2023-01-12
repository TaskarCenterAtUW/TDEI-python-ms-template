from typing import Union
from fastapi import FastAPI, Request
from fastapi.responses import Response
from python_ms_core import Core

app = FastAPI()


class OctetStreamResponse(Response):
    media_type = 'application/octet-stream'


@app.get('/')
def root():
    return {'Hello': 'World'}


@app.get('/ping')
def ping():
    return {'msg': 'Ping Successful'}


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
