#Written by Ryan Helgoth 
#I started the lab assignment before I knew about the example code, so 
#I have listed the sources I used.
import socket

def main():
    '''
    Link: https://pythonprogramminglanguage.com/socket-client/
    Author: Unknown
    Date: Unknown
    License: None
    '''
    '''
    Link: https://www.geeksforgeeks.org/socket-programming-python/
    Author: GeeksforGeeks (improved by: pall58183, rupeshdharme200001, marcosarcticseal)
    Date: 10 Nov, 2021
    License: CCBY-SA

    I have made changes to the used content.
    '''
    host = "www.google.com"
    port = 80

    #AF_INET specifies we are using IPV4, SOCK_STREAM specifies we are using TCP
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ip = socket.gethostbyname(host)

    mySocket.connect((ip, port))

    ''' 
    Link: https://stackoverflow.com/a/818188
    Author: Gumbo
    Date: May 3 '09 at 22:28
    License: SA 3.0
    '''
    request = "GET / HTTP/1.1\r\n\r\n".encode(encoding = "us_ascii")
    
    mySocket.sendall(request)
    mySocket.shutdown(socket.SHUT_WR)

    bufferSize = 4096 #Max amount of bytes to receive at once
    reply = mySocket.recv(bufferSize)
    
    while reply:
        print(reply)
        reply = mySocket.recv(bufferSize)
    

    mySocket.close()

main() 