#Imports the needed modules to connect to server and imports json
import socket
import json
class client:
        #Stores IP address and Port to connect to Server as a client
    def __init__(self):
        self.PORT = 5030
        self.SERVER = "192.168.0.13"

        self.ADD = (self.SERVER, self.PORT)



    #Paramater in the function is a list and sent to server
    #the list is first coverted into json string and then encoded ready to be sent
    #the list receieved from client is decoded and converted back into a normal list
    def send(self, list_to_send):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(self.ADD)
        message = json.dumps(list_to_send)
        self.server.sendall(message.encode())
        reply = self.server.recv(10000).decode()
        list_from_server = json.loads(reply)

        return list_from_server


