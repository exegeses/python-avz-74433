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
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║       https://docs.python.org/es/3.12/library/functions.html#reversed       ║
╚═════════════════════════════════════════════════════════════════════════════╝
''')
pausa()



def funcion(dato):
    if dato == 0:
        return "cero es neutro, no es par ni impar"
    elif dato % 2 == 0:
        return "dato es par"
    else:#if dato % 2 != 0:
        return "dato es impar"

for dato in range (0,5):
    rec =funcion(dato)
    print (f"dato enviado {dato} info recibido {rec}")
#print (f"datos recibidos en el string {str_rec}")
# ~ 1) Lista como parámetro
 # ~ def funcion(lista):
    # ~ lista.append("tres")
    # ~ print(f"datos en la lista {lista}")

# ~ lista = ["uno","dos"]
# ~ funcion(lista)
# ~ 2) Lista como objeto global no declarada explicitamente
# ~ def funcion():
    # ~ lista.append("tres")
    # ~ print(f"datos en la lista {lista}")

# ~ lista = ["uno","dos"]









simbolos =  ["!","@","#","$","%","^","*","/","+","-","_","(",")","{","}","[","]",":",";",",",".","<",">","?","\\","|","'","~","&","ç","Ç"] 
while True:
    usuario = input ("Ingrese un password debe tener minimo de 6 caracteres al menos una mayuscula, al menos una minuscula, al menos un simbolo de teclado y al menos un numero:")
    if len(usuario)<6:
        print("no cumple con 6 caracteres minimo")
    else:
        # ~ usuario =[*usuario.strip()]#.split()
        # ~ usuario = [char for char in usuario]# comprencion funciones en una linea
        # ~ print (usuario)
        print ("upper",any([True if char.isupper() else False for char in usuario ]))
        print ("lower",any([True if char.islower() else False for char in usuario ]))
        print ("numerico",any([True if char.isdecimal() else False for char in usuario ]))
        print ("simbolos", any([True if char in simbolos else False for char in usuario ]))

        lista_tiene_1_mayuscula =  [True if char.isupper() else False for char in usuario ]
        lista_tiene_1_minuscula =  [True if char.islower() else False for char in usuario ]
        lista_tiene_1_numero    =  [True if char.isdecimal() else False for char in usuario ]
        lista_tiene_1_simbolo   =  [True if char in simbolos else False for char in usuario ]
        print(f"""
        {lista_tiene_1_mayuscula=}
        {lista_tiene_1_minuscula=}
        {lista_tiene_1_numero=}
        {lista_tiene_1_simbolo=}
        
        """)     
        pausa()       
            


        if all( [any([True if char.isupper() else False for char in usuario ]),
                 any([True if char.islower() else False for char in usuario ]),
                 any([True if char.isdecimal() else False for char in usuario ]),
                 any([True if char in simbolos else False for char in usuario ])]) is True:
            print("Password aceptado")
            break
        else:
            print("No cumple con las condiciones")

exit()
