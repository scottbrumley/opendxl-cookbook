# This sample demonstrates how to register a DXL service to receive Request
# messages and send Response messages back to an invoking client.

import logging
import os
import sys
import time

from dxlclient.callbacks import RequestCallback
from dxlclient.client import DxlClient
from dxlclient.client_config import DxlClientConfig
from dxlclient.message import Message, Request, Response
from dxlclient.service import ServiceRegistrationInfo

# Import common logging and configuration
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# The topic for the service to respond to
SERVICE_TOPIC = "/scottbrumley/sample/basicevent"

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# Create the client
with DxlClient(config) as client:
    # Connect to the fabric
    client.connect()
    class MyRequestCallback(RequestCallback):
        def on_request(self, request):
            # Extract
            print "Service recieved request payload: " + request.payload.decode()
            # Create the response message
            res = Response(request)
            res.payload = "pong".encode()
            # Send the response
            client.send_event_response(res)
    # Create service reg object
    info = ServiceRegistrationInfo(client, "ScottoService")
    # Add topic for the service to repond to
    info.add_topic(SERVICE_TOPIC, MyRequestCallback())
    # Register the service with the fabric ( wait up to 10 seconds for registration to complete)
    client.register_service_sync(info, 10)
    logger.info("Ping Service is running ... ")

    while True:
        time.sleep(60)

