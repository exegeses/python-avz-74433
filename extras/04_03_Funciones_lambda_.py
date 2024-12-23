from __init__ import *
from datetime import datetime, date, time
#################################################################
def Ej_ya_hechos():
    #Con tab colocaremos aquí las practicas hechas
    pass
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║ ╔══════╗ ╦      ╦ ╔╗      ╦  ╔════╗  ╦  ╔════╗  ╔╗      ╦ ╔══════╗  ╔════╗  ║
║ ║        ║      ║ ║╚╗     ║ ╔╝    ╚╗ ║ ╔╝    ╚╗ ║╚╗     ║ ║        ╔╝    ╚╗ ║
║ ║        ║      ║ ║ ╚╗    ║ ║        ║ ║      ║ ║ ╚╗    ║ ║        ║        ║
║ ║        ║      ║ ║  ╚╗   ║ ║        ║ ║      ║ ║  ╚╗   ║ ║        ╚╗       ║
║ ╠════╗   ║      ║ ║   ╚╗  ║ ║        ║ ║      ║ ║   ╚╗  ║ ╠═════╝   ╚════╗  ║
║ ║        ║      ║ ║    ╚╗ ║ ║        ║ ║      ║ ║    ╚╗ ║ ║              ╚╗ ║
║ ║        ╚╗    ╔╝ ║     ╚╗║ ╚╗    ╔╝ ║ ╚╗    ╔╝ ║     ╚╗║ ║        ╚╗    ╔╝ ║
║ ╩         ╚════╝  ╩      ╚╝  ╚════╝  ╩  ╚════╝  ╩      ╚╝ ╚══════╝  ╚════╝  ║
║                                                                             ║
║                                                                             ║
║    ╦           ╔═════╗     ╔╗      ╔╗   ╔══════╗    ╔══════╗     ╔═════╗    ║
║    ║          ╔╝     ╚╗    ║╚╗    ╔╝║   ║      ╚╗   ║      ╚╗   ╔╝     ╚╗   ║
║    ║          ║       ║    ║ ╚╗  ╔╝ ║   ║      ╔╝   ║       ║   ║       ║   ║
║    ║          ║       ║    ║  ╚╗╔╝  ║   ╠══════╣    ║       ║   ║       ║   ║
║    ║          ╠═══════╣    ║   ╚╝   ║   ║      ╚╗   ║       ║   ╠═══════╣   ║
║    ║          ║       ║    ║        ║   ║       ║   ║       ║   ║       ║   ║
║    ║          ║       ║    ║        ║   ║      ╔╝   ║      ╔╝   ║       ║   ║
║    ╚═══════   ╩       ╩    ╩        ╩   ╚══════╝    ╚══════╝    ╩       ╩   ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                              funciones y Metodos                            ║
║                              -------------------                            ║
║          funciones    Description                                           ║
║                   lambda                                                    ║
║                                                                             ║
║          Metodos son funciones dentro de clases donde se deberia instanciar ║
║                   a la clase con self nombre_objeto                         ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              funciones,  Metodos                            ║
║                                  y Generadores                              ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
"""

https://www.w3schools.com/python/python_ref_list.asp
https://www.w3schools.com/python/python_lists.asp
https://python-para-impacientes.blogspot.com/2014/02/programacion-funcional-funciones-de.html
https://python-para-impacientes.blogspot.com/2014/02/funciones.html

La función filter() es una función la cual toma un predicado y una lista y devuelve una lista con los elementos que satisfacen el predicado. Tal como su nombre indica filter() significa filtrar, ya que a partir de una lista o iterador y una función condicional, es capaz de devolver una nueva colección con los elementos filtrados que cumplan la condición.

Todo esto podría haberse logrado también usando listas por comprensión que usaran predicados. No hay ninguna regla que diga cuando usar la función map() o la función filter() en lugar de las listas por comprensión, simplemente debe decidir que es más legible dependiendo del contexto.

Por ejemplo, suponga que tiene una lista varios números y requiere filtrarla, quedando únicamente con los números múltiples de 5, eso seria así:

>>> # Primero declaramos una función condicional
def multiple(numero):
# Comprobamos si un numero es múltiple de cinco
if numero % 5 == 0:
    # Sólo devolvemos True si lo es
    return True

>>> numeros = [2, 5, 10, 23, 50, 33]
>>> filter(multiple, numeros)
[5, 10, 50]
Si ejecuta el filtro obtiene una lista los números múltiples de 5. Por tanto cuando utiliza la función filter() tiene que enviar una función condicional, para esto, puede utilizar una función anónima lambda, como se muestra a continuación:

>>> numeros = [2, 5, 10, 23, 50, 33]
>>> filter(lambda numero: numero%5 == 0, numeros)
[5, 10, 50]
Así, en una sola línea ha definido y ejecutado el filtro utilizando una función condicional anónima y devolviendo una lista de números.

5.5.1.1. Filtrando objetos
Sin embargo, más allá de filtrar listas con valores simples, el verdadero potencial de la función filter() sale a relucir cuando usted necesita filtrar varios objetos de una lista.

Por ejemplo, dada una lista con varias personas, a usted le gustaría filtrar únicamente las cuales son menores de edad:

>>> class Persona:
...
...     def __init__(self, nombre, edad):
...         self.nombre = nombre
...         self.edad = edad
...
...     def __str__(self):
...         return "{} de {} años".format(self.nombre, self.edad)
...
>>> personas = [
...     Persona("Leonardo", 38),
...     Persona("Ana", 33),
...     Persona("Sabrina", 12),
...     Persona("Enrique", 3)
... ]
>>> menores = filter(lambda persona: persona.edad < 18, personas)
>>> for menor in menores:
print menor
Sabrina de 12 años
Enrique de 3 años
Este es un ejemplo sencillo, con el cual usted puede realizar filtrados con objetos, de forma amigable.

5.5.2. map()
La función map() toma una función y una lista y aplica esa función a cada elemento de esa lista, produciendo una nueva lista. Va a ver su definición de tipo y como se define.

Esta función trabaja de una forma muy similar a filter(), con la diferencia que en lugar de aplicar una condición a un elemento de una lista o secuencia, aplica una función sobre todos los elementos y como resultado se devuelve un lista de números doblado su valor:

>>> def doblar(numero):
return numero*2

>>> numeros = [2, 5, 10, 23, 50, 33]
>>> map(doblar, numeros)
[4, 10, 20, 46, 100, 66]
Usted puede simplificar el código anterior usando una función lambda para substituir la llamada de una función definida, como se muestra a continuación:

>>> map(lambda x: x*2, numeros)
[4, 10, 20, 46, 100, 66]
La función map() se utiliza mucho junto a expresiones lambda ya que permite evitar escribir bucles for.

Además se puede utilizar sobre más de un objeto iterable con la condición que tengan la misma longitud. Por ejemplo, si requiere multiplicar los números de dos listas:

>>> a = [1, 2, 3, 4, 5]
>>> b = [6, 7, 8, 9, 10]
>>> map(lambda x,y : x*y, a,b)
[6, 14, 24, 36, 50]
E incluso usted puede extender la funcionalidad a tres listas o más:

>>> a = [1, 2, 3, 4, 5]
>>> b = [6, 7, 8, 9, 10]
>>> c = [11, 12, 13, 14, 15]
>>> map(lambda x,y,z : x*y*z, a,b,c)
[66, 168, 312, 504, 750]
5.5.2.1. Mapeando objetos
Evidentemente, siempre que la función map() la utilice correctamente podrá mapear una serie de objetos sin ningún problema:

>>> class Persona:
...
...     def __init__(self, nombre, edad):
...         self.nombre = nombre
...         self.edad = edad
...
...     def __str__(self):
...         return "{} de {} años".format(self.nombre, self.edad)
...
>>> personas = [
...     Persona("Leonardo", 38),
...     Persona("Ana", 33),
...     Persona("Sabrina", 12),
...     Persona("Enrique", 3)
... ]
>>> def incrementar(p):
...     p.edad += 1
...     return p
...
>>> personas = map(incrementar, personas)
>>> for persona in personas:
...     print persona
...
Leonardo de 39 años
Ana de 34 años
Sabrina de 13 años
Enrique de 4 años
Claro que en este caso tiene que utilizar una función definida porque no necesitamos actuar sobre la instancia, a no ser que usted se tome la molestia de rehacer todo el objeto:

>>> class Persona:
...
...     def __init__(self, nombre, edad):
...         self.nombre = nombre
...         self.edad = edad
...
...     def __str__(self):
...         return "{} de {} años".format(self.nombre, self.edad)
...
>>> personas = [
...     Persona("Leonardo", 38),
...     Persona("Ana", 33),
...     Persona("Sabrina", 12),
...     Persona("Enrique", 3)
... ]
>>> def incrementar(p):
...     p.edad += 1
...     return p
...
>>> personas = map(lambda p: Persona(p.nombre, p.edad+1), personas)
>>> for persona in personas:
...     print persona
...
Leonardo de 39 años
Ana de 34 años
Sabrina de 13 años
Enrique de 4 años
5.5.3. lambda
La expresión lambda, es una función anónima que suelen ser usadas cuando necesita una función una sola vez. Normalmente usted crea funciones lambda con el único propósito de pasarlas a funciones de orden superior.

En muchos lenguajes, el uso de lambdas sobre funciones definidas causa problemas de rendimiento. No es el caso en Python.

>>> import os
>>> archivos = os.listdir(os.__file__.replace("/os.pyc", "/"))
>>> print filter(lambda x: x.startswith('os.'), archivos)
['os.pyc', 'os.py']
En el ejemplo anterior se usa el método os.__file__ para obtener la ruta donde esta instalada el módulo os en su sistema, ejecutando la siguiente sentencia:

>>> os.__file__
'/usr/lib/python2.7/os.pyc'
Si con el método os.__file__ obtiene la ruta del módulo os con el método replace("/os.pyc", "/") busca la cadena de carácter «/os.pyc» y la remplaza por la cadena de carácter «/»

>>> os.__file__.replace("/os.pyc", "/")
'/usr/lib/python2.7/'
Luego se define la variable archivos generando una lista de archivos usando la función os.listdir(), pasando el parámetro obtenido de la ruta donde se instalo el módulo os ejecutando en el comando previo, con la siguiente sentencia:

>>> archivos = os.listdir("/usr/lib/python2.7/")
De esta forma se define en la variable archivos un tipo lista con un tamaño de 433, como se puede comprobar a continuación:

>>> type(archivos)
<type 'list'>
>>> len(archivos)
443
Opcionalmente puede comprobar si la cadena de caracteres os.pyc se encuentras una de las posiciones de la lista archivos, ejecutando la siguiente sentencia:

>>> "os.pyc" in archivos
True
Ya al comprobar que existe la cadena de caracteres «os.pyc» se usa una función lambda como parámetro de la función filter() para filtrar todos los archivos del directorio «/usr/lib/python2.7/» por medio del función os.listdir() que inicien con la cadena de caracteres «os.» usando la función startswith().

>>> print filter(lambda x: x.startswith('os.'), os.listdir('/usr/lib/python2.7/'))
['os.pyc', 'os.py']
Así de esta forma se comprueba que existe el archivo compilado «os.pyc» de Python junto con el mismo módulo Python «os.py».





""")
pausa();limpiar();
#################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                  Lambda                                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m""")





impar = lambda numero: numero%2 != 0
impar(5)
#True
#Función lambda - operaciones de cadena

#A continuación, se presenta un ejemplo para darle la vuelta a una cadena rebanándola en sentido inverso:

revertir = lambda cadena: cadena[::-1]
revertir("Plone")
#'enolP'
revertir("enolP")
#'Plone'
#Función lambda - varios parámetros

#A continuación, se presenta un ejemplo para varios parámetros, por ejemplo para sumar dos números:

sumar = lambda x,y: x+y
sumar(5,2)
#7


#################################################################
print ("Forma clasica")
def CalculoVolumneCubo(b,a,p):#base, altura, profundidad
    return (b*a*p)
print ( CalculoVolumneCubo(10,2,5))
print ( CalculoVolumneCubo(20,10,50))
print ("Forma lambda")

CalculoVolumneCubo=lambda b,a,p : (b*a*p)#<---------return
#                           ^
#                           L___parametros de entrada
print ( CalculoVolumneCubo(10,2,5))
print ( CalculoVolumneCubo(20,10,50))
pausa()
limpiar()

datos=lambda nombre, puesto : f"el empleado {nombre} trabaja como {puesto}"
print (datos("Ariel","Mantenimiento"))
pausa()
limpiar()

xxxxx


#################################################################
#Ejercicio_funciones_Ej_010

print("""Vamos a hacer una función
def doblar(num):
    resultado = num*2
    return resultado
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num):
    resultado = num*2
    return resultado
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
pausa()
print ("-"*50)
print("""Vamos a hacerlo mas simple
def doblar(num):
    return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num):
    return num*2
print (f"el valor ingresado es de {valor}")
print("el doble es :",doblar(valor))
pausa()
print ("-"*50)
print(""" mas simple
def doblar(num): return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num): return num*2
print (f"el valor ingresado es de {valor}")
print("el doble es :",doblar(valor))

print(""" y ahora......
Esta notación simple es la que una función lambda intenta replicar, fijaros, vamos a convertir la función en una función anónima:
doblar = (lambda num: num*2)
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

pausa()
print ("-"*50)
doblar = lambda num: num*2
print ("doblar = lambda num: num*2")
print (f"el valor ingresado es de {valor}")
print("el doble es :",doblar(valor))
print(""" Ejemplo""")
pausa()
print ("-"*50)
impar = lambda num: num%2 != 0
print ("impar = lambda num: num%2 != 0")
print (f"el valor ingresado es de {valor}")
print("es impar :",impar(valor))

nuevo(1);
#################################################################
#Ejercicio_funciones_Ej_011
print ("""
Función lambda
--------------
La función lambda se utiliza para declarar funciones que sólo ocupan una línea. Son objetos que se pueden asignar a variables para usar con posterioridad.
""")
array = [11, 25, 34, 100,0, 23]
print(f"array = {array}")

dato = lambda x :x**2#<----salida
#             ^
#             L__dato q recibe
print ("dato = lambda x :x**2")
for valor in array:
    print ("dato(valor)**2:",dato(valor))

nuevo(2);
#################################################################

dato = lambda x: x*x

lista = [1,2,3,5,8,13]
print (f"lista{lista}")
print ("dato = lambda x :x*x")
for elemento in lista:
    print(f"elemento^elemento:",dato(elemento))
pausa()
print ("-"*50)
#################################################################

print (""" Lambda, con 2 argumentos:""")

area_triangulo = (lambda b,h: b*h/2)
medidas = [(34, 8), (26, 8), (44, 18)]
print (f"medidas{medidas}")
print ("area_triangulo = (lambda b,h: b*h/2)")
for datos in medidas:
    base = datos[0]
    altura = datos[1]
    print("area_triangulo(base, altura):",area_triangulo(base, altura))
nuevo(3);
#################################################################
mensaje = lambda numero: f"el número ingresado es: {numero}"
print("texto:",mensaje(2))
pausa()
print ("-"*50)
nuevo(4)
#################################################################
binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2
print ("binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2")
print ("binomio_cuadrado de (2,3):",binomio_cuadrado(2,3))
pausa()
print ("-"*50)
nuevo(5)
#################################################################
# ~ def cubos(numero):
    # ~ str_numero = str(numero)
    # ~ cubos = (int(valor)**3 for valor in str_numero)
    # ~ return sum(cubos)

# ~ valores_buscados = []
# ~ print ("Origen de datos: range(100,1000):")
# ~ for numero in range(100,1000):
    # ~ if numero == cubos(numero):
        # ~ valores_buscados.append(numero)
# ~ print(valores_buscados)
#                                       o
suma_cubos = lambda numero: sum(int(digito)**3 for digito in str(numero))
numeros_buscados = [numero for numero in range(100,1000) if suma_cubos(numero)==numero]
print ("suma_cubos = lambda numero: sum(int(digito)**3 for digito in str(numero))")
print ("numeros_buscados = [numero for numero in range(100,1000) if suma_cubos(numero)==numero]")
print ("numeros_buscados:",numeros_buscados)
nuevo(6);
##############################################################
lista_anidada=[ ["Jose", 30], ["pedro", 55],["Ariel",47],["Ana",40],["Bea", 30]]
print (f"lista_anidada:{lista_anidada}")
lista_anidada.sort(key = lambda dato : dato [1])
print ("lista_anidada.sort(key = lambda dato : dato [1])<---1 es el 2do dato de una lista")
print (f"lista_anidada ordenadas x edad:{lista_anidada}")
nuevo(7)
#################################################################
#lambda <arguments> : <value_1> if <condition_1> else (<value_2> if <condition_2> else <value_3>)

dato = lambda x :1000/x if (x  != 0) else "Error"
array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x :1000/x if (x  != 0) else 'Error'")
for valor in array:
    print (f"1000/ {valor}= {dato(valor)}")
print ("-"*50)
nuevo(8)
#################################################################

dato = lambda x : True if (x > 10 and x < 30) else False
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x : True if (x > 10 and x < 30) else False")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
nuevo(9)
#################################################################

dato = lambda x: x**2 if x%2 == 0 else x**3
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x: x**2 if x%2 == 0 else x**3")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
nuevo(10)
#################################################################
dato = lambda x : x*2 if x <=25 else (x*3 if x < 50 else -x)
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print("dato = lambda x : x*2 if x <=25  else (x*3 if x < 50 else -x)")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)

nuevo(11)
#################################################################

dato = lambda x: x if x%10 == 0 else ( x**2 if x%2 == 0 else x**3 )

Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x: x if x%10 == 0 else ( x**2 if x%2 == 0 else x**3 )")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
nuevo(12)
#################################################################

#numeros_buscados = [numero for numero in range(100,1000) if suma_cubos(numero)==numero]
#################################################################
dato = lambda x :x**2 if x % 2 == 0 else "Impar"
print ("Array:", array)
print ("dato = lambda x :x**2 if x % 2 == 0 else 'Impar'")
for valor in array:
    print (f"test",valor,dato(valor))
nuevo(13)


#################################################################

print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Lambda + map                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
Operador Map:
El operador Map, toma una función y un iterable como argumentos, y devuelve un nuevo iterable con la función aplicada a cada argumento . Ejemplo:
Como pueden ver, "map" nos a devuelto una lista con todo los elementos de la lista "array", vemos que a cada elemento le sumo 5.

resultado = map(funcion, lista)
                   ^       ^___lista de parametros para la funcion
                   L______funcion a la que llamo mandandole dato por dato de la lista
""")
#################################################################
dato = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cubo = list(map(lambda x: x**3, dato))
print(cubo)
#################################################################
#Ejemplo del operador Map
def add_five(x):
    return x + 5
array = [11, 25, 34, 100, 23]
print(f"array = {array}")
resultado = list(map(add_five, array))

print("función normal + 5",resultado)
#        lo mismo pero en lambda


resultado = list(map(lambda x:x+5, array))
print("resultado = list(map(lambda x:x+5, array))")
print("función lambda + 5",resultado)

resultado = list(map(lambda x: x**2, array))
print("resultado = list(map(lambda x: x**2, array))")
print(resultado)
nuevo(14)

#################################################################
#Ejercicio_funciones_Ej_012
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Lambda + filter (true / false)                 ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m

Operador Filter:

El operado filter (función, lista) ofrece una forma elegante de filtrar todos los elementos de una lista, para los que la función de función devuelve True.
El operador filter(f, l) necesita una función f como primer argumento. f devuelve un valor booleano, es decir, verdadero o falso. Esta función se aplicará a cada elemento de la lista. Solo si f devuelve True, el elemento de la lista se incluirá en la lista de resultados.
""")
#esta funcion necesita una lista de datos y devuelve otra de los datos filtrados true

datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even = list(filter(lambda x: x%2 == 0, datos))
print(even)

#################################################################




array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]

def filtro(DatoElLista):
    if DatoElLista % 2 == 0:# es par
        return True
print (filter(filtro,array))
print (list(filter(filtro,array)))


#Usando el operador Filter
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
print("array",array)
resultado = list(filter(lambda x: x % 2 == 0, array))
print ("resultado = list(filter(lambda x: x % 2 == 0, array))")
print("x % 2 == 0, :",resultado)
print ("-"*50)
resultado = list(filter(lambda x: x > 0, array))
print ("resultado = list(filter(lambda x: x > 0, array))")
print("x > 0 :",resultado)
print ("-"*50)
resultado = list(filter(lambda x: x % 3 != 0, array))
print ("resultado = list(filter(lambda x: x % 3 != 0, array))")
print("x % 3 != 0 :",resultado)
print ("-"*50)
resultado = list(filter(lambda x: x % 3 <= 5, array)) # list()' convierte el iterable
print ("resultado = list(filter(lambda x: x % 3 <= 5, array))")
print("x % 3 <= 5 :",resultado)
print ("-"*50)
nuevo(15);
#################################################################
#Ejercicio_funciones_Ej_013
# Ejercicio 5.6: Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud.

nuevo(4);
