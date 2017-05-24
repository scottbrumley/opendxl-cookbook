# This sample demonstrates how to register a DXL service to receive Request
# messages and send Response messages back to an invoking client.

import logging
import os
import sys
import time, json

from dxlclient.callbacks import EventCallback
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
#SERVICE_TOPIC = "/scottbrumley/sample/basicevent"
#SERVICE_TOPIC = "/mcafee/event/tie/file/repchange/broadcast"
SERVICE_TOPIC = "/mcafee/#"

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# Create the client
with DxlClient(config) as client:
    # Connect to the fabric
    client.connect()
    class ChgRepCallback(EventCallback):
        def on_event(self, event):
            # Extract
            resultStr = json.loads(event.payload.decode())
            print event.destination_topic
            print resultStr

    client.add_event_callback(SERVICE_TOPIC, ChgRepCallback())

    while True:
        time.sleep(60)

