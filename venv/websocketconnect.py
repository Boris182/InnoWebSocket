import websocket
import json


class Websocketconnect():
    def __init__(self, ipinnovaphone):
        self.ipinnovaphone = ipinnovaphone


    def open_websocket(self):

        def on_message(ws, message):
            print(message)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("### closed ###")

        def on_open(ws):
            sendAppChallenge = {'mt':'AppChallenge'}
            data = json.dumps(sendAppChallenge)
            self.ws.send(data)
            print("Open")

        websocket.enableTrace(True)
        self.ws = websocket.WebSocket()
        self.ws.connect("ws://"+ self.ipinnovaphone +"/PBX0/APPS/websocket",
                              on_open = on_open,
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
        sendAppChallenge = {'mt': 'AppChallenge'}
        data = json.dumps(sendAppChallenge)
        self.ws.send(data)
        print(self.ws.recv())
        print("Open")

