#!/usr/bin/python3
import socket
import random

class variosID:
    navegadores = {}

    def parse(self, request):
        request = request.decode('utf-8')
        cookieID = request.find("Cookie")
        if (cookieID > 0):
            cookieID = request.split()[-7][3:]
        rec = request.split()[-6][1:]
        parsedRequest = [cookieID, rec]
        return parsedRequest

    def process(self, parsedRequest):
        operando = parsedRequest[1]
        cookieID = int(parsedRequest[0])
        if (cookieID < 0):
            cookieID = random.randint(0,100000000000)
            self.navegadores[cookieID] = operando
            httpCode = "200 ok\r\nset-cookie: ID=" + str(cookieID)
            htmlAnswer = "<!DOCTYPE html><html><body>Ha introducido el operando " + str(operando) + ", introduzca el segundo</body></html>"
        else:
            print(self.navegadores)
            if(self.navegadores[int(cookieID)] != 0 ):
                operando2 = self.navegadores[cookeiID]
                resultado = int(operando) + int(operando2)
                self.navegadores[cookieID] = 0
                httpCode = "200 ok\r\nset-cookie: ID=" + str(cookieID)
                htmlAnswer = "<!DOCTYPE html><html><body>La suma de sumar " + str(operando) + " y " + str(operando2)  + " es " + str(resultado)  + "</body></html>"
            else:
                self.navegadores[cookieID] = operando
                httpCode = "200 ok\r\nset-cookie: ID=" + str(cookieID)
                htmlAnswer = "<!DOCTYPE html><html><body>Ha introducido el operando " + str(operando) + ", introduzca el segundo</body></html>"
        return(httpCode,htmlAnswer)

    def __init__(self, hostname, port):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        mySocket.listen(5)

        while True:
            print('Waiting for connections')
            (recvSocket, address) = mySocket.accept()
            print('HTTP request received (going to parse and process):')
            request = recvSocket.recv(2048)
            print(request.decode('utf-8'))
            parsedRequest = self.parse(request)
            (returnCode, htmlAnswer) = self.process(parsedRequest)
            print('Answering back...')
            recvSocket.send(bytes("HTTP/1.1 " + returnCode + " \r\n\r\n"
                            + htmlAnswer + "\r\n", 'utf-8'))
            recvSocket.close()

if __name__ == "__main__":
    testID = variosID(socket.gethostname(), 1231)
