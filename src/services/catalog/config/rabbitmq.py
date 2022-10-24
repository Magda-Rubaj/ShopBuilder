import os
import pika
from pika.adapters.blocking_connection import BlockingChannel



def prepare_channel() -> BlockingChannel:
    url = os.environ.get("AMQP_URL")
    params = pika.URLParameters(url)
    # params.socket_timeout = 5
    pika_cred = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='shopbuilder') 
    return channel