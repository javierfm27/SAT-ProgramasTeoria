#!/usr/bin/python3
"""
    clase cache
    Clase a la que se le pasa como recurso el servidor web de otro dominio, actuando
    nuestra aplicacion como intermediaria, guardando los html asociadas a esas URL
    que se le pasan como recurso para una peticion futura.
    Javier Fernandez Morata
"""
import webapp
import socket

class cache(webapp.webApp):

    diccServ ={}

    def obtainHtml(self, servidor):
        import urllib.request
        with urllib.request.urlopen(servidor) as f:
            htmlAnswer = f.read(10000).decode('utf-8')
            f.close()
        return (htmlAnswer)

    def html(self, htmlbody):
        return ("<!DOCTYPE html><html>" + htmlbody + "</html>")

    def parse(self, request):
        """
        Me quedo con el metodo y la URL que le paso como parametro
        """
        request = request.decode('utf-8')
        method = request.split()[0]
        url = request.split()[1]
        return method, url

    def process(self, requestParsed):
        method, rec = requestParsed
        if (method == 'GET'):
            url = "http:/" + rec
            if(url in self.diccServ):
                print("Entra por el de que si lo tengo")
                httpCode = "200 Ok"
                htmlAnswer = self.diccServ[url]
            else:
                httpCode = "200 Ok"
                htmlAnswer = self.obtainHtml(url)
                self.diccServ[url] = htmlAnswer
        else:
            httpCode = "400 BadRequest"
            htmlBody = "Lo siento, no podemos generar Recursos ni actualizar"
            htmlAnswer = self.html(htmlBody)
        return(httpCode , htmlAnswer)

if __name__ == "__main__":
    testCache = cache('localhost',1231)
