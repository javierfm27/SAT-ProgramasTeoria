#!/usr/bin/python3
from webapp import webApp
import socket

class variosNavegadores(webApp):

    def parse(self, request):
        peticion = request.decode('utf-8', 'strict')
        print(peticion)
        parsedRequest = peticion.split()[1][1:]
        cookie = peticion.split()[-8][-1:]
        valor_cookie = peticion.split()[-7][-1:]
        return (parsedRequest + cookie + valor_cookie)

    def process(self, parsedRequest):
        print(parsedRequest)
        x = parsedRequest("cookie")
        print(x)
        operando = parsedRequest.split()[0]
        if (x > 0):
            codeHTTP = "200 Ok \r\n" + "set-cookie: operando=" + str(operando)
            htmlAnswer = "<!DOCTYPE html> <html><body> Me ha llegado este operando " + str(operando) + ", introduzca el siguiente"  + " </body></html>"
            return (codeHTTP, htmlAnswer)
        else:
            codeHTTP = "200 ok \r\n" + "set-cookie: operando="
            resultado = int(cookie_recibida) + int(operando)
            htmlAnswer = "<!DOCTYPE html><html><body> La suma de " + cookie_recibida + " y " + operando + " es " + str(resultado) + "</body></html>"
            return (codeHTTP, htmlAnswer)

    def __init__(self, hostname, port):
        webApp.__init__(self, hostname, port)

if __name__ == "__main__":
    testPrueba = variosNavegadores(socket.gethostname(),1231)
