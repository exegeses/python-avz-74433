try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar():
    import os
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
limpiar()
def pausa():
    temp=input("\tPresione una tecla para continuar")
    print("\n")
#####################################################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
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
╠═════════════════════════════════════════════════════════════════════════════╣
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
║                                                                             ║
║                          print                                              ║
║                          variables (objetos con un dato)                    ║
║                              -int,                                          ║
║                              -float,                                        ║
║                              -reales,                                       ║
║                              -booleanas,                                    ║
║                              -¿strings?                                     ║
║                          type()                                             ║
║                          casting                                            ║
║                          condicional if else elif                           ║
║                          operadores                                         ║
║                              - + - * / // % **                              ║
║                              - de asignacion = += -= *= /=                  ║
║                              - de relacion == < <= > >= !=                  ║
║                              - de logica not is or in                       ║
║                          bucles while                                       ║
║                          colecciones(objetos con multiples datos)           ║
║                              -listas, Tuplas                                ║
║                              -   append, pop, insert, index, remove, sort,  ║
║                              -   min, max, sum                              ║
║                              -set, fs                                       ║
║                              -diccionarios                                  ║
║                          bucles for                                         ║
║                          continue / break                                   ║
║                          archivos externos TX, json open                    ║
║                              - r read / w write / a append / x crear,       ║
║                              - b binrios,                                   ║
║                              - json load dump,                              ║
║                              - pickle,                                      ║
║                              -                                              ║
║                          lista de palabras reservadas                       ║
║                          Funciones built-in / integradas                    ║   #https://docs.python.org/es/3.11/library/functions.html
║                          Funciones estandar                                 ║
║                              -argumentos posicionales                       ║
║                              -argumentos arbitrarios posicionales (*args),  ║
║                              -Keywords arguments número arbitrario(**kwargs)║
║                              -argumentos por omisión                        ║
║                               return                                        ║
║                               agrupar - desagrupar                          ║
║                          ambitos de objetos (variables - colecciones)       ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                                                                             ║
║   ╔══════╗     ╔═══════╗    ╔══════╗     ╔═════╗     ╔═════╗     ╔═════╗    ║
║   ║      ╚╗    ║            ║      ╚╗   ╔╝     ╚╗   ╔╝     ╚╗   ╔╝     ╚╗   ║
║   ║       ║    ║            ║       ║   ║       ║   ║           ║       ║   ║
║   ║      ╔╝    ║            ║      ╔╝   ║       ║   ╚╗          ║       ║   ║
║   ╠══╦═══╝     ╠═════╣      ╠══════╝    ╠═══════╣    ╚═════╗    ║       ║   ║
║   ║  ╚═╗       ║            ║           ║       ║          ╚╗   ║       ║   ║
║   ║    ╚═╗     ║            ║           ║       ║   ╚╗     ╔╝   ╚╗     ╔╝   ║
║   ╩      ╚═    ╚═══════╝    ╩           ╩       ╩    ╚═════╝     ╚═════╝    ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝

''')
#######################################################################################################
# ~ Funciones built-in (integradas o preconstruidas)


"""


if -- else  -- elif
match  (nombre):
    case "Ariel" :
"""        

x = ""
while not x.replace(" ","").isalnum():
    x = input ("ingrese su nombre:")    
else:
    print ("ok")



coleccion = 1,2,3,4,5,6,7,8,9
coleccion =(1, 2, 3, 4, 5, 6, 7, 8, 9)
print (f"""
{coleccion =}
{type(coleccion) =}
{id(coleccion) =}
{dir(coleccion) =}
""")

"""
<class 'tuple'>=['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',

 'count', 'index']



"""
coleccion = [1,2,"tres",4.5,5j,6,[7.1,7.2,7.3],8,9]

print (f"""
{coleccion =}
{type(coleccion) =}
{id(coleccion) =}
{dir(coleccion) =}
""")


"""
<class 'list'>['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 



'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


"""

# ~ coleccion = [1,2,"tres",4.5,5j,6,[7.1,7.2,7.3],8,9]
coleccion =(1, 2, 3, 4, 5, 6, 7, 8, 9)

inicio = 0
fin = 25#<------------limute final
rango = range (inicio,fin)
print (f"{rango=}")
for numero in rango:
    print(f"\t{numero=}")

print ("*"*50)
# ~ coleccion = [1,2,"tres",4.5,5j,6,[7.1,7.2,7.3],8,9]
coleccion =(1, 2, 3, 4, 5, 6, 7, 8, 9)

inicio = 0
#fin = 25#<------------limute final
fin = len(coleccion)


rango = range (inicio,fin)
print (f"{rango=}")
for index in rango:
    print(f"\t{index=}       {coleccion[index]}")





print ("*"*50)
coleccion = [1,2,"tres",4.5,5j,6,[7.1,7.2,7.3],8,9]
# ~ coleccion =(1, 2, 3, 4, 5, 6, 7, 8, 9)

inicio = 0
#fin = 25#<------------limute final
fin = len(coleccion)


rango = range (inicio,fin)
print (f"{rango=}")
for index in rango:
    dato =  coleccion[index]
    print(f"\t{index=}       {dato}       {type(dato)}")


print ("*"*50)
coleccion = [1,2,"tres",4.5,5j,6,[7.1,7.2,7.3],8,9]
for dato  in coleccion:
    print(f"\t{dato}       {type(dato)}")


for index, dato  in enumerate(coleccion):
    print(f"\t{index=}       {dato}       {type(dato)}")


exit()


def funcion():
    pass

def nombre_funcion(argumentos):
    # código
    return retorno
# ~ Argumentos por defecto
def imprimir_mensaje(mensaje="No has escrito nada."):
    print(f"{mensaje=}")

# ~ Documentación en funciones
def sumar(a, b):
    """
    docstring
        suma los dos argumentos de entrada y retorna es resultado
    """
    resultado =  a + b
    return resultado
print(f"{sumar(6,2)=}")
print(f"{sumar.__doc__=}")

input("Enter para continuar......")
# ~ Ámbito de las variables

global variable# no aconsejable

variable = 10
def funcion():
    global variable
    variable = 5
print(f"{variable=}")
funcion()
print(f"{variable=}")
# ~ Paso por valor y por referencia
def funcion(entrada):
    entrada.append(40)
dato = [10, 20, 30]
funcion(dato)
print(f"{dato=}")
print('''
        Argumentos de longitud variable 
        Al declarar la función con un parámetro *, hará que los argumentos, sean la cantidad que fueran, lleguen individualmente y que una vez recibido 
            la función lo empaquete en una tupla de manera automática.
        Atención: No confundir * con los punteros en otros lenguajes de programación, no tiene nada que ver 
        ¡En Python existen los punteros a memoria!
''')
def sumar(*args):
    print(f"{args=}")
    print(f"{type(args)=}")
    total = 0
    for n in args:
        total += n
    return total
l=sumar(10,0,5,4)
print(f"{l=}")
print('''
        El doble asterisco ** (usualmente acompañado por el nombre kwargs) captura cualquier keyword argument que no haya sido definido junto con la función. 
        Los argumentos capturados por este operador son almacenados, como dijimos, en un diccionario que tiene como claves los strings que representan los 
            nombres de los argumentos, y como valor, el valor del argumento. 
        Este operador debe ir al final de la definición de otros parámetros, si los hubiera.
''')
# ~ Ejemplo:
def sumar(**kwargs):
    print(f"{kwargs=}")
    print(f"{type(kwargs)=}")
    total = 0
    for n in kwargs:
        total+= kwargs[n]

    print(f"{total=}")
sumar(a=5, b=20, c=23)
# ~ Orden para usar diferentes argumentos
def funcion(a,b,*args,c=100,**kwargs):
    print(f"{a=}\t\t\t{type(a)=}")
    print(f"{b=}\t\t\t{type(b)=}")
    print(f"{args=}\t\t\t{type(args)=}")
    print(f"{c=}\t\t\t{type(c)=}")
    print(f"{kwargs=}\t\t\t{type(kwargs)=}")

######################################

def superior(funcion,lista):
    nueva = []
    for n in lista:
        nueva.append(funcion(n))
    return nueva


######################################

print(f"{superior(lambda x : x**3,[1,2,3])=}")
print()

input("Enter para continuar......")

'''
Las palabras clave assert, try, except, finally y raise están relacionadas con las excepciones, y nos permiten tratar el qué hacer 
cuando las cosas no salen como esperamos. El siguiente código intenta hacer un cast de cadena a entero, manejando un posible error.
Si x="10" el casteo se realiza sin problemas, ya que es posible representar esa cadena como un entero. 
Sin embargo hay que estar preparados siempre para lo peor.
Si x="a" no se podría hacer int() y tendríamos un error. 
Si no manejamos este error, el programa se pararía, y esto no es algo deseable. 
El uso de try, except y finally nos permite controlar dicho error y actuar en consecuencia sin que el programa se pare.

'''
