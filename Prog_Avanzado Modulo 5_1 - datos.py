#!/usr/bin/env python
# -*- coding: utf-8 -*-
#######################################################################################################
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
from colorama import *
#######################################################################################################
limpiar()
from datetime import datetime, date, time
# ~ nuevo(0,estado='inicio',modulo=4)
import math
import datetime

####################################################################################################
#                                                                                                  #
#                                        Bases de datos                                            #
#                                                                                                  #
####################################################################################################

print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
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
║                                                                             ║
║                                                                             ║
║  ╔═════╗   ╔╗       ╔╗   ╔═════╗    ╔╗      ╦                               ║
║ ╔╝     ╚╗   ║       ║   ╔╝     ╚╗   ║╚╗     ║                               ║
║ ║       ║   ╚╗     ╔╝   ║       ║   ║ ╚╗    ║                               ║
║ ║       ║    ║     ║    ║       ║   ║  ╚╗   ║                               ║
║ ╠═══════╣    ╚╗   ╔╝    ╠═══════╣   ║   ╚╗  ║  ╠═════╣                      ║
║ ║       ║     ║   ║     ║       ║   ║    ╚╗ ║                               ║
║ ║       ║     ╚╗ ╔╝     ║       ║   ║     ╚╗║                               ║
║ ╩       ╩      ╚═╝      ╩       ╩   ╩      ╚╝                               ║
║                                                                             ║
║                                                                             ║
║                             ╔═══════╗   ╔═════╗  ╔══════╗    ╔═════╗        ║
║                                    ╔╝  ╔╝     ╚╗ ║      ╚╗  ╔╝     ╚╗       ║
║                                   ╔╝   ║       ║ ║       ║  ║       ║       ║
║                                  ╔╝    ║       ║ ║       ║  ║       ║       ║
║                               ╔══╝     ╠═══════╣ ║       ║  ║       ║       ║
║                              ╔╝        ║       ║ ║       ║  ║       ║       ║
║                             ╔╝         ║       ║ ║      ╔╝  ╚╗     ╔╝       ║
║                             ╚═══════╝  ╩       ╩ ╚══════╝    ╚═════╝        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝''')
pausa()
limpiar()
import os
from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione una tecla para continuar")
def ya_hechos():
    pass
limpiar();
def operaciones_sobre_txt(archivo,modo,cant=""):
    try:
        objeto_python="si es solo lectura 'objeto_python ' no tiene info\n si es una segunda operacio debes ubicar seek al inicio"
        texto="Si se corta la luz\nya no perdemos nada"
        with open (archivo, mode=modo) as io_obj:
            print (f"Antes: me encuentro en la posicion {io_obj.tell()}")
            if modo == "x":
                print ("Se creo vacio")
            elif  modo.startswith("w"):
                print ("Se creo y se ingreso una linea al inicio")
                io_obj.write(texto)
            elif  modo.startswith("a"):
                print ("Se agrego una linea al final del archivo si este no estaba creado se genero")
                io_obj.write("\nFin....")
            if  modo == "r" or "+" in modo:
                io_obj.seek(0)
                if cant=="":
                    objeto_python = io_obj.read()
                elif isinstance (cant,int):
                    objeto_python = io_obj.read(cant)
                elif cant == "xlinea":
                    modo="readline"
                    objeto_python = ""
                    for cada_linea in io_obj.readlines():
                        objeto_python+=cada_linea


            print("\n"*2)
            print (f"El contenido es :\n{objeto_python}")
            print("\n"*2)
            print (f"Despues: me encuentro en la posicion {io_obj.tell()}")
        #  tabular dentro y fuera del with <---->
            print (f"mode = {modo}".center(20))
            print (f"estado de cierre {io_obj.closed=}")
            print (f"estado de escritura {io_obj.writable()=}")
            print (f"estado de lectura {io_obj.readable()=}")
            print (f"estado de desplazamiento {io_obj.seekable()=}")

    except Exception as Error:
        print (f"Error tipo {Error}")
    finally:
        print ("-"*50)
operaciones_sobre_txt("Mineria.txt","x")
operaciones_sobre_txt("Mineria.txt","w")
operaciones_sobre_txt("Mineria.txt","w+")
operaciones_sobre_txt("Mineria.txt","a+")
operaciones_sobre_txt("Mineria.txt","r")
operaciones_sobre_txt("Mineria.txt","r",18)
operaciones_sobre_txt("Mineria.txt","r","xlinea")


#·········································································

