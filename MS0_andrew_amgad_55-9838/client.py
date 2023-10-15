import socket
import select
import sys


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8081
client_socket.connect(('127.0.0.1', 8081))

while True:
    message = input("Enter your message: ")
    mess_bytes = message.encode()
    client_socket.send(mess_bytes)
    sdata = client_socket.recv(1024).decode()
    print(sdata)