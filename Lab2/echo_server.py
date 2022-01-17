#Written by Ryan Helgoth 

#TODO: finish citations, test on vm

import socket

def main():
    #https://realpython.com/python-sockets/#echo-client-and-server
    host = "127.0.0.1"  #Local host
    listenPort = 8001 

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind((host, listenPort))
    mySocket.listen()

    conn, address = mySocket.accept()
    bufferSize = 4096 #Max amount of bytes to receive at once
    data = conn.recv(bufferSize)
    while data:
        conn.sendall(data)
        data = conn.recv(bufferSize)

    conn.close()
    mySocket.close()

main() 