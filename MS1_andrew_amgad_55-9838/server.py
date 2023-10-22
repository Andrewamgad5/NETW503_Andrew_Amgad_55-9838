import socket
import threading

PORT = 9900
ADDR = ('127.0.0.1', PORT)

def threaded(conn, addr):
    #new connection
    print("[NEW CONNECTION] " + str(addr) + " connected.")

    while True:
        #recieve data from the client
        data = conn.recv(1024).decode('utf-8')

        #check if the client wants to close the socket
        if "CLOSE SOCKET" in data:
            print('connection closed')
            conn.close()
            break
        #send uppercase letter
        else:
            conn.sendall(data.upper().encode('utf-8'))

def main():
    #define server main fucntion
    print(" Server is starting...")

    #creat socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #bind the socket to the server address
    server.bind(ADDR)

    #server listen to incoming connections
    server.listen(5)

    while True:
        #accept incoming connections
        conn, addr = server.accept()

        #creat lock for thread
        lock = threading.Lock()

        #acquire the lock
        lock.acquire()

        #start a new thread to handle the connection
        threading.Thread(target=threaded, args=(conn, addr)).start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == '__main__':
    main()