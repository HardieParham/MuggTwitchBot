# Standard Imports
import sys
import logging

# External Imports
from obswebsocket import obsws, events, requests


# Connecting to OBS
class Obs():
    logging.basicConfig(level=logging.INFO)
    sys.path.append('../')

    host = "localhost"
    port = 4444
    password = "secret"

    ws = obsws(host, port, password)

    def connect():
        Obs.ws.connect()

    def disconnect():
        Obs.ws.disconnect()

    def reconnect():
        Obs.ws.reconnect()