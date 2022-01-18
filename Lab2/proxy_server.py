#Written by Ryan Helgoth with some code from lab 2 examples.
import socket

HOST = "www.google.com"
PORT = 80
#CLIENT_PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyStart:
        print("Starting proxy server")
        proxyStart.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxyStart.bind((HOST, PORT))
        proxyStart.listen(2)
        
        while True:
            conn, addr = proxyStart.accept()
            print("Connected by", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyEnd:
                print("Connecting to", HOST)
                ip = socket.gethostbyname(HOST)
                proxyEnd.connect(ip, PORT)

                print("Sending client data to", HOST)
                clientData = conn.recv(BUFFER_SIZE)
                proxyEnd.sendall(clientData)
                proxyEnd.shutdown(socket.SHUT_WR)

                print("Sending data from", HOST, "to client")
                hostData = proxyEnd.recv(BUFFER_SIZE)
                conn.sendall(hostData)

            conn.close()


if __name__ == "__main__":
    main()
