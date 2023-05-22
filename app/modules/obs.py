import sys
import logging

from obswebsocket import obsws


"""
Connecting to OBS

Refer to OBS Websocket documentation for all the ws functions
""" 
# logging.basicConfig(level=logging.INFO)
sys.path.append('../')
host = "localhost"
port = 4455
password = "secret"
ws = obsws(host, port, password)


def connect() -> None:
    ws.connect()

def disconnect() -> None:
    ws.disconnect()

def reconnect() -> None:
    ws.reconnect()



# #  Simple usage: (v5 api)
# from obswebsocket import obsws, requests
# client = obsws("localhost", 4455, "secret")
# client.connect()
# client.call(requests.GetVersion()).getObsVersion()
# '29.0.0'
# client.disconnect()


#  #Legacy usage: (v4 api)
# from obswebsocket import obsws, requests
# client = obsws("localhost", 4444, "secret", legacy=True)
# client.connect()
# client.call(requests.GetVersion()).getObsStudioVersion()
# '25.0.0'
# client.disconnect()