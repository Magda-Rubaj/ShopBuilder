import os
import pika
from pika.adapters.blocking_connection import BlockingChannel



def prepare_channel() -> BlockingChannel:
    url = pika.URLParameters(os.environ.get("AMQP_URL"))
    connection = pika.BlockingConnection(url)
    channel = connection.channel()
    return channel