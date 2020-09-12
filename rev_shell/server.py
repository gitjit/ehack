import socket
import sys

# constants
HOST = ''
PORT = 9999


def start_server():
    global s
    try:
        s = socket.socket()
        s.bind((HOST, PORT))
        s.listen(5)
        print("Server : ", "Waiting for new client")
        conn, address = s.accept()
        print('Connection has been established | ' +
              'IP ' + address[0] + 'Port ' + str(address[1]))
        send_commands(conn)
    except socket.error as err:
        print('Socket creation failed :' + str(err) + '\n' + "retrying...")


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.send(str.encode('quit'))
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    start_server()


start_server()
