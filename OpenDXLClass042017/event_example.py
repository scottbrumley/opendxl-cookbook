# This sample demonstrates how to register a callback to receive Event messages
# from the DXL fabric. Once the callback is registered, the sample sends a
# set number of Event messages to the fabric and waits for them all to be
# received by the callback.

import logging
import os
import sys
import time
from threading import Condition

from dxlclient.callbacks import EventCallback
from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig
from dxlclient.message import Event, Request, Response, Message

# Import common logging and configuration
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# The topic to publish to
SERVICE_TOPIC = "/scottbrumley/sample/basicevent"
#SERVICE_TOPIC = "/odxl/service/hello"
#SERVICE_TOPIC = "/odxl/puzzler/service/6degrees"

# The total number of events to send
TOTAL_EVENTS = 10

# Condition/lock used to protect changes to counter
event_count_condition = Condition()

# The events received (use an array so we can modify in callback)
event_count = [0]

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# Create the client
with DxlClient(config) as client:

    # Connect to the fabric
    client.connect()

    #
    # Register callback and subscribe
    #

    # Create and add event listener
    req = Request(SERVICE_TOPIC)

    req.payload = "Rosamund Pike".encode()

    res = client.sync_request(req)

    if res.message_type != Message.MESSAGE_TYPE_ERROR:
        print "Client Recieved response payload: " + res.payload.decode()