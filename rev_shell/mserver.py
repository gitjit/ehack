# multi server
import socket 
import time
import sys
import struct 
import threading

NUM_THREADS = 2
JOBS = [1,2]

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
                print('Server: Waiting for new client')
                conn, address = self.socket.accept() 
                print ( address )
                conn.setblocking(1) # blocking
                client_hostname = conn.recv(1024).decode('utf-8')
                address = address + (client_hostname,)
                print (address)
            except Exception as e:
                print('Error accepting connections: ' + str(e))
                continue
            self.all_connections.append(conn)
            self.all_addresses.append(address)
            print('\nConnection has been established: {0} ({1})'.format(address[-1],address[0]))
        
        return
    

    def handle_client(self):
        pass 

def start_server(server):
    print ('starting server...', server)
    server.create_server()
    server.start_server()
    
def process_client(server):
    print ('Processing client .. ')
    while True:
        cmd = input('Enter your Command : ')
        if cmd == 'ls':
            for  item in server.all_addresses:
                print(item)
    pass 


def start():
    server = MultiServer()
    listener_thread = threading.Thread(target=start_server,args=(server,))
    listener_thread.daemon = True
    listener_thread.start()
   
    worker_thread = threading.Thread(target=process_client,args=(server,))
    worker_thread.daemon = True
    worker_thread.start()
    listener_thread.join()
    worker_thread.join()


def main():
    start()

    


main()
