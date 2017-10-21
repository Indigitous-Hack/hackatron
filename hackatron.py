import logging
import threading
import configparser
import os
from Legobot.Lego import Lego

from Legobot.Connectors.Slack import Slack
from Legobot.Legos.Help import Help

config = configparser.ConfigParser()
config.read('config.ini')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)

# Initialize lock and baseplate
lock = threading.Lock()
baseplate = Lego.start(None, lock)
baseplate_proxy = baseplate.proxy()

# Add children
baseplate_proxy.add_child(Slack, os.environ['SLACK_TOKEN'])
baseplate_proxy.add_child(Help)
