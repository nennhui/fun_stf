from channels.generic.websocket import WebsocketConsumer
import socket,struct

class ChatConsumer(WebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        self.close()



    def receive(self, text_data):
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__socket.connect(("localhost", 1111))
        text_data=(text_data.split(','))
        print(text_data,int(text_data[0]))
        x = int(int(text_data[0])*(1080 / 377))
        y = int(int(text_data[1])*(1920 / 724))
        # x = int(int(text_data[0])*(10799 / 377))
        # y = int(int(text_data[1])*(19199 / 724))
        # x = int(text_data[0])*int(10799 / 377)
        # y = int(text_data[1])*int(19199 / 724)
        print(x,y)
        f="d 0 {} {} 50\nc\nu 0\nc\n  ".format( x,y)
        f = (f.encode('utf-8'))
        print(f)
        self.__socket.send(f)
        self.__socket.close()



