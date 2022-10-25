import os
import pika
from pika.adapters.blocking_connection import BlockingChannel



def prepare_channel() -> BlockingChannel:
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue='shopbuilder') 
    return channel