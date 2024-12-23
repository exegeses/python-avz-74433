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
print(F'''{Fore.WHITE+ Style.BRIGHT + Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║    ╔═══════╗            ╦                                                   ║
║    ║                    ║                                                   ║
║    ║                    ║                                                   ║
║    ║                    ║                                                   ║
║    ╠══════╣     ╔═══════╣    ╦       ╦    ╔═══════╗                         ║
║    ║            ║       ║    ║       ║    ║                                 ║
║    ║            ║       ║    ║       ║    ║          ╔╗                     ║
║    ╚═══════╝    ╚═══════╝    ╚═══════╝    ╚═══════╝  ╚╝                     ║
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
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║       https://docs.python.org/es/3.12/library/functions.html#reversed       ║
╚═════════════════════════════════════════════════════════════════════════════╝
''')
pausa()


def ya_hechos():
    pass

limpiar()
print(Back.GREEN+"""\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║  ╔═════╗  ╔════╗  ╔╗      ╦ ╔═════╗  ╦  ╔════╗  ╦   ╔════╗                  ║
║ ╔╝       ╔╝    ╚╗ ║╚╗     ║ ║     ╚╗ ║ ╔╝    ╚╗ ║  ╔╝    ╚╗                 ║
║ ║        ║      ║ ║ ╚╗    ║ ║      ║ ║ ║        ║  ║      ║                 ║
║ ║        ║      ║ ║  ╚╗   ║ ║      ║ ║ ║        ║  ║      ║                 ║
║ ║        ║      ║ ║   ╚╗  ║ ║      ║ ║ ║        ║  ║      ║ ╠═════╝         ║
║ ║        ║      ║ ║    ╚╗ ║ ║      ║ ║ ║        ║  ║      ║                 ║
║ ╚╗       ╚╗    ╔╝ ║     ╚╗║ ║     ╔╝ ║ ╚╗    ╔╝ ║  ╚╗    ╔╝                 ║
║  ╚════╝   ╚════╝  ╩      ╚╝ ╚═════╝  ╩  ╚════╝  ╩   ╚════╝                  ║
║                                                                             ║
║                                                                             ║
║                           ╔╗      ╦   ╔════╗  ╦         ╔══════╗  ╔════╗    ║
║                           ║╚╗     ║  ╔╝    ╚╗ ║         ║        ╔╝    ╚╗   ║
║                           ║ ╚╗    ║  ║      ║ ║         ║        ║          ║
║                           ║  ╚╗   ║  ║      ║ ║         ║        ╚╗         ║
║                           ║   ╚╗  ║  ╠══════╣ ║         ╠═════╝   ╚════╗    ║
║                           ║    ╚╗ ║  ║      ║ ║         ║              ╚╗   ║
║                           ║     ╚╗║  ║      ║ ║         ║        ╚╗    ╔╝   ║
║                           ╩      ╚╝  ╩      ╩ ╚══════╝  ╚══════╝  ╚════╝    ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣"""+Style.RESET_ALL+Back.BLUE+"""
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║ ╔══╦══╗ ╔═════╗ ╔═════╗   ╔╗      ╦  ╔════╗   ╔═════╗   ╦  ╔════╗   ╔════╗  ║
║    ║    ║       ║     ╚╗  ║╚╗     ║ ╔╝    ╚╗  ║     ╚╗  ║ ╔╝    ╚╗ ╔╝    ╚╗ ║
║    ║    ║       ║      ║  ║ ╚╗    ║ ║      ║  ║      ║  ║ ║      ║ ║        ║
║    ║    ║       ║     ╔╝  ║  ╚╗   ║ ║      ║  ║     ╔╝  ║ ║      ║ ╚╗       ║
║    ║    ╠════╝  ╠═══╦═╝   ║   ╚╗  ║ ╠══════╣  ╠═══╦═╝   ║ ║      ║  ╚════╗  ║
║    ║    ║       ║   ╚╗    ║    ╚╗ ║ ║      ║  ║   ╚╗    ║ ║      ║       ╚╗ ║
║    ║    ║       ║    ╚╗   ║     ╚╗║ ║      ║  ║    ╚╗   ║ ╚╗    ╔╝ ╚╗    ╔╝ ║
║    ╩    ╚═════╝ ╩     ╚╝  ╩      ╚╝ ╩      ╩  ╩     ╚╝  ╩  ╚════╝   ╚════╝  ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝"""+Back.RESET)
pausa()
limpiar()
print(
    """\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║    ╔══════╗    ╦       ╦   ╔═══╦═══╗   ╦       ╦    ╔═════╗    ╔╗      ╦    ║
║    ║      ╚╗   ╚╗     ╔╝       ║       ║       ║   ╔╝     ╚╗   ║╚╗     ║    ║
║    ║       ║    ╚╗   ╔╝        ║       ║       ║   ║       ║   ║ ╚╗    ║    ║
║    ║      ╔╝     ╚╗ ╔╝         ║       ║       ║   ║       ║   ║  ╚╗   ║    ║
║    ╠══════╝       ╚╦╝          ║       ╠═══════╣   ║       ║   ║   ╚╗  ║    ║
║    ║               ║           ║       ║       ║   ║       ║   ║    ╚╗ ║    ║
║    ║               ║           ║       ║       ║   ╚╗     ╔╝   ║     ╚╗║    ║
║    ╩               ╩           ╩       ╩       ╩    ╚═════╝    ╩      ╚╝    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                            operadores temarios                              ║
║                                                                             ║
║                               "if else elif"                                ║
║                                 <,>,==,!=                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m""")
print("un operador temario en python evalua la condición entre True / False y sobre esto da una salida usando una sola linea de comando. super compacto")


import this
print("*"*100)#-------------------------------------------------------------
print ("por extencion")
a=2
b=3
c="SI"
d="no"

if a>b:
    print (f"{c=} xq a>b")
else:
    print (f"{d=} xq a<=b")
pausa()
print("*"*100)
print ("por ternario")

print ( c if a>b else d)

salida = "a es mayor que b" if a>b else "b es mayor que a"
print (f"{salida=}")


salida = True if a>b else False
print (f"{salida=}")
print("*"*100)#-------------------------------------------------------------

pausa()

a= 5

if a%2!=0 :
    print("impar")
elif a!=0:
    print("par")
else:
    print("cero es neutro")




print ( "impar" if a%2!=0 else ("par" if a!=0 else "cero es neutro") )

salida = "impar" if a%2!=0 else ("par"  if a!=0  else "cero es neutro")
print(f"{salida=}")
exit()
print("*"*100)#-------------------------------------------------------------
pausa()
limpiar()

a=2
b=1
c="SI"
d="no"
#print (f"tiene {(A>B)?C:D}")
print("condition_if_true if condition else condition_if_false")
print('si a > b---', c if (a > b) else d, '---c o d!');
print("*"*100)#-------------------------------------------------------------
anda = True# remplazar con False
estado = "si: el codigo corre" if anda \
                                        else "bug: no, el codigo no corre"
print("estado del programa ", estado)
print("*"*50)
print("*"*100)#-------------------------------------------------------------

pausa()
limpiar()
############################################################################
print("Otra forma (no muy usada) es la siguiente:")
print("tupla + [booleano 0 o 1]")
print("if_test_is_false, if_test_is_true)[test]")
print("*"*100)#-------------------------------------------------------------
anda = True#1
lista = ["bug: no, el codigo no corre","si: el codigo corre" ]
estado = lista[False]
print("estado del programa ", estado)
estado = ["bug: no, el codigo no corre","si: el codigo corre"][anda]
print("estado del programa ", estado)
print("*"*100)#-------------------------------------------------------------
anda = True
print(lista[1] if anda else lista[0])# ternario
print(lista[anda])#slicing

anda = False
print(lista[1] if anda else lista[0])# ternario
print(lista[anda])#slicing

############################################################################
#                 ______________--------->demas si es booleana
#                /              \
coleccion = [9,6,3,2,5,8,7,4,1,0]
#        False |
#              True verdadero
print (f"{coleccion=}")
print (f"{coleccion[True]=}")
print (f"{coleccion[1]=}")

print (f"{coleccion[False]=}")
print (f"{coleccion[0]=}")


print (f"{coleccion[5]=}")
print (f"{coleccion[7]=}")









