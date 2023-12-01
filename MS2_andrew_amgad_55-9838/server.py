import socket
import threading

PORT = 9900
ADDR = ('192.168.1.239', PORT)

def threaded(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        data = conn.recv(1024).decode('utf-8')

        if "CLOSE SOCKET" in data:
            print('connection closed')
            conn.close()
            break
        else:
            temperature, humidity = data.split(',')
            temperature = float(temperature)
            humidity = float(humidity)

            # Process temperature and humidity data here

            conn.sendall(f"Temperature: {temperature}C, Humidity: {humidity}%".encode('utf-8'))

def main():
    print(" Server is starting...")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(5)

    while True:
        conn, addr = server.accept()
        lock = threading.Lock()
        lock.acquire()
        threading.Thread(target=threaded, args=(conn, addr)).start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == '__main__':
    main()