import os
import pika
from pika.adapters.blocking_connection import BlockingChannel



def prepare_channel() -> BlockingChannel:
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    return channel