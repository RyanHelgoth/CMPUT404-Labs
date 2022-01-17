#Written by Ryan Helgoth 

#TODO: finish citations, test on vm, check if encode is needed on vm

import socket

def main():
    #https://pythonprogramminglanguage.com/socket-client/
    #https://www.geeksforgeeks.org/socket-programming-python/
    host = "www.google.com"
    port = 80

    #AF_INET specifies we are using IPV4, SOCK_STREAM specifies we are using TCP
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #https://stackoverflow.com/questions/51316029/python-socket-recv-data-in-while-loop-not-stopping
    mySocket.setblocking(False) 
    ip = socket.gethostbyname(host)

    mySocket.connect((ip, port))

    #https://stackoverflow.com/a/818188
    request = "GET / HTTP/1.1\r\n\r\n".encode(encoding = "us_ascii")
    
    mySocket.sendall(request)

    bufferSize = 4096 #Max amount of bytes to receive at once
    reply = mySocket.recv(bufferSize)
    
    while reply:
        print(reply)
        reply = mySocket.recv(bufferSize)

    mySocket.close()

main() 