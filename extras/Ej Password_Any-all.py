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
print ("""
Enunciado del Programa
Diseñe un programa en Python que solicite al usuario ingresar una contraseña y valide que cumpla con los siguientes criterios:
    Longitud mínima: La contraseña debe contener al menos 10 caracteres.
    Contenido obligatorio: La contraseña debe incluir:
    Al menos una letra mayúscula.
    Al menos una letra minúscula.
    Al menos un número.
    Al menos un símbolo especial de teclado (de una lista predefinida de símbolos).
    Detalles del Programa
    Entrada:
    El programa solicita al usuario ingresar una contraseña a través del teclado.
    En caso de que no cumpla con alguno de los requisitos, se pide al usuario que reingrese una nueva contraseña hasta que sea válida.
    Proceso:
    Se valida la longitud mínima de la contraseña.
    Se revisa cada carácter de la contraseña para verificar si es una letra mayúscula, minúscula, número o símbolo especial.
    Se utilizan listas para almacenar los resultados de cada validación.
    Finalmente, se verifica si la contraseña cumple con todos los requisitos de manera acumulativa.
    Salida:
    Si la contraseña cumple con todos los requisitos, el programa muestra el mensaje "password aceptado".
    Si no cumple con los requisitos, muestra el mensaje "password no aceptado rehacer" y permite al usuario intentarlo nuevamente.
    Finalización:
    Cuando se introduce una contraseña válida, el programa finaliza mostrando la contraseña aceptada y un mensaje de despedida.
    Consideraciones Adicionales
    El programa utiliza una lista predefinida de símbolos para validar los caracteres especiales.
    Se emplea la función any() para determinar si las listas contienen al menos un valor verdadero y all() para comprobar si todos los criterios se cumplen.
    Se muestran mensajes intermedios para ayudar al usuario a entender qué criterio no se cumple.
    Este programa es útil para implementar reglas básicas de seguridad en contraseñas en aplicaciones que requieran autenticación de usuarios.
""")
pausa()
########################################################################
########################################################################
###                                                                  ###
###                   intentalo hacer por ti mismo                   ###
###                               simple                             ###
########################################################################
########################################################################
simbolos =  ["!","@","#","$","%","^","*","/","+","-","_","(",")","{","}","[","]",":",";",",",".","<",">","?","\\","|","'","~","&","ç","Ç",'"'] 

lista_tiene_1_mayuscula = list()
lista_tiene_1_minuscula = list()
lista_tiene_1_numero    = list()
lista_tiene_1_simbolo   = list()


while True:
    limpiar()
    password = input ("Ingrese un password debe tener mínimo de 10 caracteres al menos una mayúscula, al menos una minúscula, al menos un símbolo de teclado y al menos un numero:")
    if len(password)<10:
        print("no cumple con 6 caracteres minimo")
        pausa()
        continue
    else:
        
        for char in password:
            print (f"\nCaracter = {char} :", end="\t")
            
            print ("\nMayúscula :", end="\t")
            if char.isupper():
                print ("True\n")
                lista_tiene_1_mayuscula.append(True)
            else:
                print ("False\n")
                lista_tiene_1_mayuscula.append(False)
            print ("\nMinúscula :", end="\t")
            if char.islower():
                print ("True\n")
                lista_tiene_1_minuscula.append(True)
            else:
                print ("False\n")
                lista_tiene_1_minuscula.append(False)
            print ("\nNumero :", end="\t")
            if char.isdigit():
                print ("True\n")
                lista_tiene_1_numero.append(True)
            else:
                print ("False\n")
                lista_tiene_1_numero.append(False)
            
            print ("\nSímbolo :", end="\t")
            # ~ if not (char.isalnum()):
            if char in simbolos:
                print ("True\n")
                lista_tiene_1_simbolo.append(True)
            else:
                print ("False\n")
                lista_tiene_1_simbolo.append(False)
        print(f"""
        {lista_tiene_1_mayuscula=}
        {lista_tiene_1_minuscula=}
        {lista_tiene_1_numero=}
        {lista_tiene_1_simbolo=}
        
        """)    
        print(f"""
        {any(lista_tiene_1_mayuscula)=}
        {any(lista_tiene_1_minuscula)=}
        {any(lista_tiene_1_numero)=}
        {any(lista_tiene_1_simbolo)=}
        
        """)    
        resultados = [any(lista_tiene_1_mayuscula),any(lista_tiene_1_minuscula),any(lista_tiene_1_numero),any(lista_tiene_1_simbolo)]
        print(f"""
        {resultados=}
        {all(resultados)=}

        """)    
        
        '''   
        if all (resultados):
            print ("password aceptado")
            break
        else:
            print ("password no aceptado rehacer")
        ''' 
        
        
        if all ([any(lista_tiene_1_mayuscula),any(lista_tiene_1_minuscula),any(lista_tiene_1_numero),any(lista_tiene_1_simbolo)]):
            print ("password aceptado")
            break
        else:
            print ("password no aceptado rehacer")
        
        pausa()
      
print (f"Adios supassword {password} fua aceptado")

########################################################################
########################################################################
###                                                                  ###
###                   intentalo hacer por ti mismo                   ###
###                              compleja                            ###
########################################################################
########################################################################
''' 
        
        
        
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
'''
