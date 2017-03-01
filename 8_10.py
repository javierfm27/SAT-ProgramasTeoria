#!/usr/bin/python3
from webapp import webApp
import socket

class variosNavegadores(webApp):
    def parse(self, request):
        peticion = request.decode('utf-8', 'strict')
        parsedRequest = peticion.split()[1][1:]
        valor_cookie = peticion.split()[-7][-1:]
        return (parsedRequest  + "  " + cookie + " " + valor_cookie)

    def process(self, parsedRequest):
        print(parsedRequest)
        cookieBol = parsedRequest.split()[1]
        valorCookie = parsedRequest.split()[2]
        if (cookieBol != 'Cookie:'  or int(valorCookie) == 0 ):
            operando1 = parsedRequest.split()[0]
            httpCode = "200 ok \r\nset-cookie: operando=" + str(operando1)
            htmlAnswer = "<!DOCTYPE html><html><body> El primer operando es " + operando1 + ", introduzca el segundo </body></html>"
        else:
            operando2 = parsedRequest.split()[0]
            resultado = int(valorCookie) + int(operando2)
            httpCode = "200 Ok \r\nset-cookie: operando=" + str(0)
            htmlAnswer = "<!DOCTYPE html><html><body>El resultado de sumar " + valorCookie + " y " + operando2 + " es-> " + str(resultado) + "</body></html"
        return(httpCode,htmlAnswer)

if __name__ == "__main__":
    testPrueba = variosNavegadores(socket.gethostname(),1231)
