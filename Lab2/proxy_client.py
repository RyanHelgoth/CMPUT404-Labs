#Written by Ryan Helgoth

import socket

def main():
    HOST = "127.0.0.1"
    PORT = 8001
    BUFFER_SIZE = 4096

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.connect((HOST, PORT))

    request = "GET / HTTP/1.1\r\n\r\n".encode(encoding = "us_ascii")
    mySocket.sendall(request)
    mySocket.shutdown(socket.SHUT_WR)

    reply = mySocket.recv(BUFFER_SIZE)
    while reply:
        print(reply)
        reply = mySocket.recv(BUFFER_SIZE)
    
    mySocket.close()

main() 