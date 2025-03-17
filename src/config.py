import os
"""
This module handles the configuration settings for the application.

"""
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    """
    Settings class for loading and managing environment variables.

    Attributes:
        app_name (str): The name of the application. Change this as per the need of your own service.
        incoming_topic (str): The name of the incoming topic. Change as per the need of the service.
        incoming_topic_subscription (str): The name of the subscription for the incoming topic. Change as per need.
        outgoing_topic (str): The name of the outgoing topic. Change as per need.
        storage_container (str): The name of the storage container. Change as per need.
        max_concurrent_messages (int): The maximum number of concurrent messages. Default is the value of the environment variable 'MAX_CONCURRENT_MESSAGES' or 1 if not set.
    """
    # Load environment variables from .env file
    app_name: str = 'Python MS Core Template'
    incoming_topic: str = 'incoming-topic' # Change this
    incoming_topic_subscription: str = 'incoming-sub' # Change this
    outgoing_topic: str = 'outgoing-topic' # Change this
    storage_container: str = 'storage-container' # Change this
    max_concurrent_messages: int = os.environ.get('MAX_CONCURRENT_MESSAGES', 1)


