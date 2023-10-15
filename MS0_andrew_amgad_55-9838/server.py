import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8081
server_socket.bind(('127.0.0.1', 8081)) # (ip add , port)
server_socket.listen(5) # socket listen to the port

print("Server is listening for incoming connections...")

while True:
    client, add = server_socket.accept() # when a connection to a client is accepted
    print("Connection from client has been established.")
    
    while True:

        data = client.recv(1024).decode() # recieve data from the client and decode it into string

        if 'CLOSE SOCKET' in data:
            # Close the socket connection
            client.send('Socket connection closed.'.encode())
            client.close()
            print('Socket connection closed.')

            break # Break the connection 

        else:
            capitalized_data = data.upper() # Return a copy of the string converted to uppercase.
            client.send(capitalized_data.encode())