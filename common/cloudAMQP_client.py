import json
import logging
import pika

logger_format = '%(asctime)s - %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('cloud_amqp_client')
logger.setLevel(logging.DEBUG)


class CloudAMQPClient:
  def __init__(self, cloud_amqp_url, queue_name):
    self.cloud_amqp_url = cloud_amqp_url
    self.queue_name = queue_name
    self.params = pika.URLParameters(cloud_amqp_url)
    self.params.socket_timeout = 3
    self.connection = pika.BlockingConnection(self.params)
    self.channel = self.connection.channel()
    self.channel.queue_declare(queue=queue_name)


  def sendMessage(self, message):
    # TODO: send the given message to rabbitmq through channel.basic_publish


  def getMessage(self):
    # TODO: get a message from rabbitmq through channel.basic_get


  # BlockingConnection.sleep is a safer way to sleep than time.sleep(). This
  # will repond to server's heartbeat.
  def sleep(self, seconds):
    # TODO: sleep for the given duration in secondes using connection.sleep
