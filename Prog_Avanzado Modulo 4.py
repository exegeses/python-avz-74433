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

# Casting de  entero a valor octal (0 a7)
objeto = [1,5,9,4,1,3,7,4,6,8,7,1,3,2,9,1,0]
print(f"objeto: {objeto}\n\t\t{type(objeto)}")
print ("*"*50)
tupla = tuple(objeto)
print(f"objeto: {tupla}\n\t\t{type(tupla)}")
print ("*"*50)
conjunto = set(objeto)
print(f"objeto: {conjunto}\n\t\t{type(conjunto)}")
print ("*"*50)
conjunto_congelado = frozenset(objeto)
print(f"objeto: {conjunto_congelado}\n\t\t{type(conjunto_congelado)}")
print ("*"*50)
lista = list(conjunto)
print(f"objeto: {lista }\n\t\t{type(lista)}")
print ("*"*50)
dic=dict.fromkeys(lista,"valor a cargar")
print(f"objeto: {dic }\n\t\t{type(dic)}")
print ("*"*50)





# Casting a un número complejo a partir de dos enteros (parte real y una parte imaginaria).
# Crear un número complejo con parte real e imaginaria
complejo1 = complex(3, 4)

# Crear un número complejo solo con parte real (imaginaria es 0)
complejo2 = complex(2)

# Crear un número complejo con parte imaginaria (real es 0)
complejo3 = complex(0, 1)

# Crear un número complejo desde una cadena
string = "2+3j"
complejo4 = complex(string)

print(f"{complejo1=}")
print(f"{complejo2=}")
print(f"{complejo3=}")
print(f"{complejo4=}")




exit()




# Casting de ASCII a formato  caracter
entrada_valor_ascii = 65
salida_caracter = chr(entrada_valor_ascii)#                                     casting ASCII a caracter
print(f"Resultado caracter: {salida_caracter }")

exit()





# Casting de unicode a formato ascii
texto = """¡¡¡Python es genial!!!
    y es re facil"""
salida_ascii = ascii(texto)#                                                  casting unicode  a ascii
print(f"Resultado: {salida_ascii }")
exit()
# Casting de entero que deseas convertir a formato binario
numero = 10
numero_binario = bin(numero)#                                                  casting directo de entero a binario
print(f"Resultado: {numero_binario } con prefijo")
print(f"Resultado: {numero_binario[2:]} sin priefijo")
exit


def autenticar(func):
    def wrapper(user, password):
        if user == "admin" and password == "123":
            return func(user, password)
        else:
            print(f"Acceso denegado {user}\nno puede ingresar a función")
    return wrapper

@autenticar
def mostrar_info_segura(user, password):
    print(f"Acceso concedido desde función a {user}")

mostrar_info_segura("admin", "123")  # Acceso concedido
print ("*"*50)
mostrar_info_segura("usuario", "543")


def requerir_autenticacion(func):
    def wrapper(username, password):
        if username == "admin" and password == "12345":
            return func(username, password)
        else:
            print("Acceso denegado")
    return wrapper

@requerir_autenticacion
def acceso_seguro(username, password):
    print("Acceso concedido")

acceso_seguro("admin", "12345")  # Acceso concedido
acceso_seguro("usuario", "54321")  # Acceso denegado

#··················································································

exit()















import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio} segundos")
        return resultado
    return wrapper

@medir_tiempo
def contar_hasta(n):
    for i in range(n):
        pass
    print (f"valor de {n=}")

contar_hasta(1000000)


#··················································································

exit()




def mi_decorador(func):
    def nueva_funcion():
        print("Antes de llamar a la función original")
        func()
        print("Después de llamar a la función original")
    return nueva_funcion

@mi_decorador
def mi_funcion():
    print("¡Hola desde mi_funcion!")

mi_funcion()


#··················································································



def decorador_con_argumentos(parametro):
    def mi_decorador(func):
        def nueva_funcion():
            print("Antes de llamar a la función original")
            print (f"el agumento recibido {parametro}")
            func()
            print("Después de llamar a la función original")
        return nueva_funcion
    return mi_decorador

@decorador_con_argumentos("argumento")
def saludar():
    print("¡Hola desde mi_funcion!")

saludar()


#··················································································

exit()
def decorador_con_argumentos(arg):
    def mi_decorador(func):
        def wrapper():
            print(f"Antes de la función con argumento {arg}")
            func()
            print("Después de la función")
        return wrapper
    return mi_decorador

@decorador_con_argumentos("decorador_arg")
def saludar():
    print("Hola, mundo!")

saludar()




def crear_funcion(multiplicador):
    def multiplicar(multiplicando):
        return multiplicando * multiplicador
    return multiplicar

def cuadrado(num):
    return num ** 2

def cubo(num):
    return num ** 3

numeros = [1, 2, 3, 4, 5]
r_cuadrado = operacion(cuadrado, numeros)
r_cubo     = operacion(cubo, numeros)

print(f"{r_cuadrado=}")
print(f"{r_cubo=}")

#··················································································

exit()




# ~ map, filter y lambda combinados:
# ~ python
# ~ Copy code
# ~ numeros = [1, 2, 3, 4, 5]
# ~ cuadrados = map(lambda x: x * x, numeros)
# ~ cuadrados_lista = list(cuadrados)
# ~ print(cuadrados_lista)  # Output: [1, 4, 9, 16, 25]

# ~ numeros = [1, 2, 3, 4, 5, 6]
# ~ pares = filter(lambda x: x % 2 == 0, numeros)
# ~ pares_lista = list(pares)
# ~ print(pares_lista)  # Output: [2, 4, 6]
# ~ Estos ejemplos adicionales te muestran cómo las funciones de alto nivel en Python pueden ser flexibles y poderosas para manipular datos y crear código más conciso y legible.






exit()


def operacion(func_parametro, numeros):
    #   opcion 1
    # ~ resultados = []
    # ~ for num in numeros:
        # ~ resultados.append(func_parametro(num))
    #------------------------------------------------------------------------
    #   opcion 2
    # ~ resultados = [func_parametro(num) for num in numeros ]
    #------------------------------------------------------------------------
    #   opcion 3
    resultados = list(map(func_parametro,numeros)   )
    #------------------------------------------------------------------------
    return resultados

def cuadrado(num):
    return num ** 2

def cubo(num):
    return num ** 3

numeros = [1, 2, 3, 4, 5]
r_cuadrado = operacion(cuadrado, numeros)
r_cubo     = operacion(cubo, numeros)

print(f"{r_cuadrado=}")
print(f"{r_cubo=}")








exit()




cuadrado = lambda x: x * x
print(cuadrado(5))  # Output: 25

pares = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
pares_lista = list(pares)
print(pares_lista)
exit()

