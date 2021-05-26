# chat/consumers.py
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # as the name says, we accept connections
        self.accept()

    def disconnect(self, close_code):
        # we are not doing anything here yet
        pass

    def receive(self, text_data):
        # here , we receive a messag and load it into a json
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))
