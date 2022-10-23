import pika
import os


def prepare_channel():
    url = os.environ.get("RABBITURL")
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='shopbuilder') 
    return channel