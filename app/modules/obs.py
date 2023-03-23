# Standard Imports
import sys
import logging

# External Imports
from obswebsocket import obsws, events, requests


# Connecting to OBS
logging.basicConfig(level=logging.INFO)
sys.path.append('../')

host = "localhost"
port = 4444
password = "secret"

ws = obsws(host, port, password)

# Refer to OBS WEbsocket documentation for all the ws functions

def connect():
    ws.connect()

def disconnect():
    ws.disconnect()

def reconnect():
    ws.reconnect()