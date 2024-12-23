import json
import random
import os
try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tPresione enter para continuar")
limpiar();
#################################################################
def ya_hechos():
    pass
print(F'''{Fore.WHITE+ Style.BRIGHT + Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║                                                                             ║
║              ╦     ╔═════╗     ╔═══╦═══╗   ╔═══════╗     ╔═════╗            ║
║              ║    ╔╝     ╚╗        ║       ║            ╔╝     ╚╗           ║
║              ║    ║                ║       ║            ║       ║           ║
║              ║    ╚╗               ║       ║            ║       ║           ║
║              ║     ╚═════╗         ║       ╠══════╣     ╠═══════╣           ║
║              ║           ╚╗        ║       ║            ║       ║           ║
║              ║    ╚╗     ╔╝        ║       ║            ║       ║           ║
║              ╩     ╚═════╝         ╩       ╚═══════╝    ╩       ╩           ║
║                                                                             ║
║                                                                             ║
║    ╔═══════╗            ╦                                   ╦   ╔═══╦═══╗   ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ║                    ║                                   ║       ║       ║
║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗         ║       ║       ║
║    ║            ║       ║    ║       ║    ║                 ║       ║       ║
║    ║            ║       ║    ║       ║    ║          ╔╗     ║       ║       ║
║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝     ╩       ╩       ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║       https://docs.python.org/es/3.12/library/functions.html#reversed       ║
╚═════════════════════════════════════════════════════════════════════════════╝
''')
pausa()

import datetime

nuevo(0, "inicio")

#######################################################################################################################
print ("""Devuelve verdadero si alguno de los elementos o condiciones son verdaderoses verdadero.
 Devuelve False si está vacío o si todos son falsos.
 Cualquiera puede considerarse como una secuencia de operaciones OR en los iterables proporcionados.""")
# Since all are false, false is returned
print (any([False, False, False, False]))

# Here the method will short-circuit at the
# second item (True) and will return True.
print (any([False, True, False, False]))

# Here the method will short-circuit at the
# first (True) and will return True.
print (any([True, False, False, False]))


a=1
b=2
c=3
d=4
e=5
f=0

if any ([(a>b) ,( b<c) ,( c>d ) ,(d<e)]):
    print("Alguno es True")
    print ([(a>b) ,( b<c) ,( c>d ) ,(d<e)])
else:
    print ("ninguno True")
    print([(a>b) ,( b<c) ,( c>d ) ,( d<e )])

if any ([(a>b) ,( b>c) ,( c>d ) ,( d>e ) ,(e<f)]):
    print("Alguno es True")
    print([(a>b) ,( b>c) ,( c>d ) ,( d>e ) ,(e<f)])
else:
    print ("ninguno True")
    print([(a>b) ,( b>c) ,( c>d ) ,( d>e ) ,(e<f)])

pausa()
limpias()
dato = [99, 25, 50, 5,2,88,22,1,0,4,6,44,7,3,5,8,9,4,3,];
print("Array datos :",dato)
#################################################################
print("""if all (condición / bucle for): #Si todos devuelven True, devuelve True. Caso contrario, False
if any (condición / bucle for): #Devuelve True si alguno es True. Devuelve False si esta vació o todos son #False""");
Numeros= []
while True:
    Valor1 = (int(input("Ingresa un numero mayor de 5 y menor de 10  \n"))) #Pedimos numero
    Numeros.append(Valor1) #Agregamos numero a la lista
    Valor2 = (int(input("Ingresa un numero mayor de 5 y menor de 10 \n")))#Pedimos numero
    Numeros.append(Valor2)#Agregamos numero a la lista
    Valor3 = (int(input("Ingresa un numero mayor de 5 y menor de 10 \n")))#Pedimos numero
    Numeros.append(Valor3)#Agregamos numero a la lista
    print (Numeros)#Imprimimos la lista de numeros


    if all (numero >= 5 and numero <= 10 for numero in Numeros):
        #Comprueba si todos los números cumple la condición mayor o igual a 5 y
        #Menor o igual a 10
        print ("Correcto! Los números ingresados son mayores a 5 y menores a 10")
        print ("Gracias y hasta luego")
        break #Rompemos el bucle
    elif any (numero >= 5 and numero <= 10 for numero in Numeros):
        #Comprueba si algún numero es mayor a 5 o mayor a 10
        print ("Algún numero no es correcto")
        Numeros= [] #Reseteamos la lista
        print ("Vuelve a intentarlo")
    else:
        print ("Error no has ingresado ningún numero mayor a 5 o menor a 10")
        print ("Suerte la próxima perdedor, ni siquiera un solo numero!")
        break #Rompemos el bucle

