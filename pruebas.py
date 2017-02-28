#!/usr/bin/python3
print("Hola esto es una prueba para ver si va en el terminal")
#Listas
#--> para crear una lista, se pone entre corches y comas
lista = [2,4,6,8,10,12]
#--> para borrar se puede borrar de la siguiente manera
print(lista)
lista[1:3] = []
print(lista)
lista[:] = [] #Asi la borramos entera
print(lista)
lista = [1,2,3,4,5,5,6,5,43,4,56,3,4]
print(len(lista)) #asi vemos la longitud de la listaa
#-->Asi se puede hacer asignacion multiple
b, c = 0,1
print(str(b) + ' ' + str(c))
