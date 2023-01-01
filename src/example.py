import uuid
import asyncio
import datetime
from io import BytesIO, StringIO
from python_ms_core import Core
from python_ms_core.core.queue.models.queue_message import QueueMessage


def test_topics():
    topic = 'gtfs-flex-upload'
    subscription = 'uploadprocessor'
    topic_object = Core.get_topic(topic)

    queue_message = QueueMessage.data_from({
        'message': str(uuid.uuid4().hex),
        'data': {'a': 1}
    })

    event_loop_publish = asyncio.get_event_loop()
    event_loop_publish.run_until_complete(topic_object.publish(data=queue_message))

    event_loop_subscribe = asyncio.get_event_loop()
    msg = event_loop_subscribe.run_until_complete(topic_object.subscribe(subscription=subscription))
    print(msg)


def test_storage_upload():
    azure_client = Core.get_storage_client()
    container = azure_client.get_container('tdei-storage-test')
    # Creating a text stream
    txt = 'foo\nbar\nbaz'
    file_like_io = StringIO(txt)
    basename = 'sample-file'
    suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    filename = '_'.join([basename, suffix])
    test_file = container.create_file(f'{filename}.txt', 'text/plain')
    print('Start uploading...')
    test_file.upload(file_like_io.read())
    print('Uploaded')


def test_storage():
    azure_client = Core.get_storage_client()
    container = azure_client.get_container('tdei-storage-test')
    list_of_files = container.list_files()
    for file in list_of_files:
        print(file.name)
        print(file.mimetype)


if __name__ == "__main__":
    test_topics()
    test_storage_upload()
    test_storage()
