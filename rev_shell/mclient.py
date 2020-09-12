import socket
import sys
import os 

class Client(object):

    def __init__(self):
        self.host = '192.168.1.115'
        self.port = 9999
        self.socket = None
    

    def create_socket(self):
        self.socket = socket.socket()
        self.socket.connect((self.host,self.port))
        hostname = socket.gethostname()
        self.socket.send(hostname.encode())
        while 1:
            self.receive_commands()


    def receive_commands(self):
        cmd = self.socket.recv(1024)
        print(cmd.decode('utf-8'))


def main():
    client = Client()
    client.create_socket()


main()