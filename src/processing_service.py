from python_ms_core import Core
from src.config import Settings
import threading
from python_ms_core.core.queue.models.queue_message import QueueMessage


class ProcessingService:
    
    core: Core = None

    def __init__(self, core: Core):
        self.core = core
        self.settings = Settings()


    
    def start_listening(self):
        self.listening_thread = threading.Thread(target=self.subscribe)
        self.listening_thread.start()
    
    def subscribe(self):
        """
        Start listening to the incoming topic.
        """
        try:
            self.core.get_topic(topic_name=self.settings.incoming_topic).subscribe(
                subscription=self.settings.incoming_topic_subscription,
                callback=self.process_message
            )
        except Exception as e:
            print(f"Error listening topic: {e}")


    def process_message(self, message: QueueMessage):
        """
        Process the incoming message. This is a dummy processing function that just forwards the message to the outgoing topic.
        Use the message.messageId, message.messageType to determine the type and ID of the message
        Use message.data to get the actual data of the message
        """
        print(f"Received message: {message}")
        self.core.get_topic(topic_name=self.settings.outgoing_topic).publish(data=message)
        print(f"Published message: {message}")
        message.ack()