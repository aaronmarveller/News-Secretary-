""" Backend Service. """
import datetime
import json
import logging
import os
import sys

from bson.json_util import dumps  # pylint: disable=import-error
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer # pylint: disable=import-error

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
import mongodb_client  # pylint: disable=import-error, wrong-import-position

from cloudAMQP_client import CloudAMQPClient

LOG_CLICKS_TASK_QUEUE_URL = "amqp://erygdeea:mJdprUO-I6KpJNoyO18sx23FFQm1ouIX@donkey.rmq.cloudamqp.com/erygdeea"
LOG_CLICKS_TASK_QUEUE_NAME = "tap-news-log-clicks-task-queue"

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

LOGGER_FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
LOGGER = logging.getLogger('backend_service')
LOGGER.setLevel(logging.DEBUG)

cloudAMQP_client = None

def add(num1, num2):
    """ Test method """
    LOGGER.debug("add is called with %d and %d", num1, num2)
    return num1 + num2


def get_one_news():
    """ Get one news. """
    LOGGER.debug("get_one_news is called")

    # TODO: get one news from mongodb.

    return json.loads(dumps(res))


def get_news(user_id):
    # TODO


def log_news_click_for_user(user_id, news_id):
    LOGGER.debug('log_news_click_for_user is called with %s and %s', user_id, news_id)
    message = {'userId':user_id, 'newsId':news_id, 'timestamp':str(datetime.utcnow())}
    cloudAMQP_client.sendMessage(message)


def start(host=SERVER_HOST, port=SERVER_PORT):
    cloudAMQP_client = CloudAMQPClient(LOG_CLICKS_TASK_QUEUE_URL, LOG_CLICKS_TASK_QUEUE_NAME)

    """ Start rpc server. """
    server = SimpleJSONRPCServer((host, port))
    server.register_function(add, "add")

    # TODO: register your function onto the server.

    LOGGER.info("Starting RPC server on %s:%d", host, port)
    server.serve_forever()


if __name__ == "__main__":
    start()
