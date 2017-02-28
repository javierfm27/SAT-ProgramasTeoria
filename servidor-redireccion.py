#!/usr/bin/python3
import socket
import random

mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Nos permite reutilizar el puerto, cuando cerramos el servidor aunque no se haya liberado debidamente
mySocket.bind((socket.gethostname(),1231))
mySocket.listen(5)

try:
    while True:
        print("Waiting connections")
        (recvSocket, address) = mySocket.accept()
        print("Request received")
        peticion = recvSocket.recv(2048)
        print(peticion.decode('utf-8','strict'))
        numeroRandom = random.randint(0,1000000000000)
        print("Answering back")
        recvSocket.send(bytes("HTTP/1.1 301 Moved Permanently\r\n\r\n" +
                        "<!DOCTYPE html><html>" +
                        "<head><meta http-equiv='Refresh' content='3;url=" +
                        str(numeroRandom) +
                        "'></head>" +
                        "<body> Redireccionando a <a href='" +
                        str(numeroRandom) +
                        "'>" +
                        str(numeroRandom) +
                        "</a> </body> </html>"
                        , "utf-8"))

        recvSocket.close()

except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
