import websocketconnect
from pip._vendor.distlib.compat import raw_input

wsc = websocketconnect.Websocketconnect("192.168.70.230")

wsc.open_websocket()

print("test")



