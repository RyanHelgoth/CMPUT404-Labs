#Written by Ryan Helgoth 

#TODO: finish citations, test on vm

import socket
from multiprocessing import Process


def handleEcho(conn, address):
    print("Connected by", address)
    bufferSize = 4096 #Max amount of bytes to receive at once
    data = conn.recv(bufferSize)
    while data:
        conn.sendall(data)
        data = conn.recv(bufferSize)
    conn.close()

def main():
    #https://realpython.com/python-sockets/#echo-client-and-server
    host = "127.0.0.1"  #Local host
    listenPort = 8001 

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.bind((host, listenPort))
    mySocket.listen()

    while True:
        conn, address = mySocket.accept()
        process = Process(target=handleEcho, args=(conn, address))
        process.daemon = True 
        process.start()
        print("Started process", process)
    
    

main() 