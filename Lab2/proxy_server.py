#Written by Ryan Helgoth with some code from lab 2 examples.
import socket

LOCAL_HOST = "127.0.0.1"
REMOTE_HOST = "www.google.com"
HOST_PORT = 80
CLIENT_PORT = 8001
BUFFER_SIZE = 4096

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyStart:
        print("Starting proxy server")
        proxyStart.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxyStart.bind((LOCAL_HOST, CLIENT_PORT))
        proxyStart.listen(2)
        
        
        conn, addr = proxyStart.accept()
        print("Connected by", addr)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxyEnd:
            print("Connecting to", REMOTE_HOST)
            ip = socket.gethostbyname(REMOTE_HOST)
            proxyEnd.connect((ip, HOST_PORT))

            print("Sending client data to", REMOTE_HOST)
            clientData = conn.recv(BUFFER_SIZE)
            proxyEnd.sendall(clientData)
            proxyEnd.shutdown(socket.SHUT_WR)

            print("Sending data from", REMOTE_HOST, "to client")
            hostData = proxyEnd.recv(BUFFER_SIZE)
            while hostData:
                conn.sendall(hostData)
                hostData = proxyEnd.recv(BUFFER_SIZE)
            
            conn.close()
            print("Proxy server shutting down")


if __name__ == "__main__":
    main()
