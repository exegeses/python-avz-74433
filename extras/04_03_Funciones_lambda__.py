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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
pausa();limpiar();
#################################################################

#Ejercicio_Funciones_Ej_001
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                   lambda parametros : expresion                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""");

lista_org = ["linea_1","linea_2","linea_3","linea_4","linea_5"]
mayusculas = lambda dato:dato.upper()
print (mayusculas("zz"))
lst =  ['1234', 'hello', '6787']
print (f"{[x for x in lst if x.isalpha()]=}")

#Or if you definitely want to use a lambda:
print (f"{[x.upper() if x.isalpha() else float(x) for x in lst ]=}")

print (f"{filter(lambda x: x.isalpha(), lst)}")

nuevo(4);
#################################################################
#Ejercicio_Funciones_Ej_005
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                               Lambda   Anonimas                             ║
║                 lambda <parámetro> :expresión                               ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
http://conocepython.blogspot.com/2017/08/t2-las-funciones-lambda-elogio-de-la.html
https://programacionpython80889555.wordpress.com/2018/10/30/funciones-lambda-en-python/

Operador lambda:
El operador lambda que no es función lambda, es una forma de crear funciones anónimas, es decir, funciones sin nombre. Estas funciones son desechable, es decir, solo se necesitan donde se han creado. Las funciones lambda se utilizan principalmente en combinación con las funciones Map, Filter y Reduce.

lambda no es una función es keyword o palabra reservada del lenguaje que introduce en el punto de la declaración una expresión: una expresión lambda. El resultado de dicha expresión es a todos los efectos un callable equivalente a uno generado con la sentencia def.

La sintaxis general de una función lambda es bastante simple:
lambda argument_list : expression

El operador lambda o función lambda, es una forma de crear funciones anónimas, es decir, funciones sin nombre. Estas funciones son desechables, es decir, solo se nesecitan donde se han creado. Las funciones lambda se utilizan principalmente en combinatorio con las funciones Map, Filter y Reduce.
""")

area_triangulo =lambda base,altura:(base*altura)/2
while True:
	try:
		base = float(input("Ingrese la base :"))
		altura = float(input("Ingrese la altura :"))
		break
	except ValueError:
		print ("Error de entrada/salida.")
print(area_triangulo(base,altura))
nuevo(5);
#################################################################
#Ejercicio_Funciones_Ej_006
#Función lambda que devuelve la suma de sus dos argumentos:
func_lambda = lambda x, y : x + y
print("func_lambda(2 , 6)",func_lambda(2 , 6))

#Segundo ejemplo de lambda
#Función lambda que devuelve la raíz cuadrada de su argumento
func_lambda = lambda x : x**1/2
print("func_lambda(233)",func_lambda(233))
print("func_lambda(233)",(lambda x : x**1/2)(233))


func_lambda = lambda x: x < 5
print(func_lambda(3))  # Devuelve 'True'
print(func_lambda(8))  # Devuelve 'False'

func_lambda =  lambda x, y, z=1: (x+y) * z
print("func_lambda(5, 6) :",func_lambda(5, 6))
print("func_lambda(5, 6, 7) :",func_lambda(5, 6, 7))
print("func_lambda(5, 6, 7) :",(lambda x, y, z=1: (x+y) * z)(5, 6, 7))
nuevo(6);
#################################################################
#Ejercicio_Funciones_Ej_007

print("Con strings")
revertir = lambda cadena: cadena[::-1]
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ:",revertir("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print("BUEN DIA, ¿COMO VA LA VIDA?:",revertir("BUEN DIA, ¿COMO VA LA VIDA?"))
print("Neuquen:",revertir("Neuquen"));print("Es un palíndromo")

pausa();limpiar();
array = ['a','b','c']
num = range(1,4)
for contador in map(lambda x, y: x*y, array, num):
	print(contador)
#sin lambda con zip
for contador in (x*y for x,y in zip(array, num)):
    print(contador)
nuevo(7);
#################################################################
#Ejercicio_Funciones_Ej_008
print ("Ver \nhttps://es.quora.com/Qu%C3%A9-hace-realmente-la-funci%C3%B3n-lambda-de-Python-Quiero-dominarle-pero-no-la-entiendo")

resultado = lambda s: s.strip().upper()

print(resultado("  hOlA CoMo EsTaS   "))

print("Con funciones")
def imprimir_si(lista, fn):
	for elemento in lista:
		if fn(elemento):
			print(elemento)

lista1=[9, 20, 70, 60, 19]
print("Valores pares de la lista")
imprimir_si(lista1, lambda x: x%2==0)
print("Valores múltiplos de 3 o de 5")
imprimir_si(lista1, lambda x: x%3==0 or x%5==0)
print("Imprimir valores mayores o iguales a 50")
imprimir_si(lista1, lambda x: x>=50)
print("Imprimir los valores comprendidos entre 10 y 50 o 70 y 100")
imprimir_si(lista1, lambda x: x>=10 and x<=50 or x>=70 and x<=100)
print("Imprimir la lista completa")
imprimir_si(lista1, lambda x: True )

nuevo(8);
#################################################################
#Ejercicio_Funciones_Ej_009
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                              Lambda + map                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
Operador Map:
El operador Map, toma una función y un iterable como argumentos, y devuelve un nuevo iterable con la función aplicada a cada argumento . Ejemplo:
Como pueden ver, "map" nos a devuelto una lista con todo los elementos de la lista "array", vemos que a cada elemento le sumo 5.
""")

#Ejemplo del operador Map
def add_five(x):
	return x + 5
print("array = [11, 25, 34, 100, 23]")
array = [11, 25, 34, 100, 23]
resultado = list(map(add_five, array))
print("función normal + 5",resultado)
#        lo mismo pero en lambda


resultado = list(map(lambda x:x+5, array))
print("función lambda + 5",resultado)

resultado = list(map(lambda x: x**2, array))
print(resultado)



nuevo(9);
#################################################################
#Ejercicio_Funciones_Ej_010

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

print("""Vamos a hacerlo mas simple
def doblar(num):
	return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num):
	return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))

print(""" mas simple
def doblar(num): return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")

def doblar(num): return num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))

print(""" y ahora......
Esta notación simple es la que una función lambda intenta replicar, fijaros, vamos a convertir la función en una función anónima:
doblar = (lambda num: num*2)
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
""")


doblar = lambda num: num*2
valor = int(input("Valor : "))
print("el doble es :",doblar(valor))
print(""" Ejemplo""")

impar = lambda num: num%2 != 0
valor = int(input("Valor : "))
print("es impar :",impar(valor))

nuevo(10);
#################################################################
#Ejercicio_Funciones_Ej_011
print ("""
Función lambda
--------------
La función lambda se utiliza para declarar funciones que sólo ocupan una línea. Son objetos que se pueden asignar a variables para usar con posterioridad.
""")
cuadrado = lambda x: x*x

lista = [1,2,3,5,8,13]
for elemento in lista:
	print(cuadrado(elemento))

print (""" Lambda, con 2 argumentos:""")

area_triangulo = (lambda b,h: b*h/2)
medidas = [(34, 8), (26, 8), (44, 18)]
for datos in medidas:
	base = datos[0]
	altura = datos[1]
	print(area_triangulo(base, altura))
nuevo(11);
#################################################################
#Ejercicio_Funciones_Ej_012
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

#Usando el operador Filter
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
print("array",array)
resultado = list(filter(lambda x: x % 2 == 0, array))
print("x % 2 == 0, :",resultado)

resultado = list(filter(lambda x: x > 0, array))
print("x > 0 :",resultado)

resultado = list(filter(lambda x: x % 3 != 0, array))
print("x % 3 != 0 :",resultado)

resultado = list(filter(lambda x: x % 3 <= 5, array)) # list()' convierte el iterable
print("x % 3 <= 5 :",resultado)

nuevo(12);
#################################################################
#Ejercicio_Funciones_Ej_013
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                     Ver practicas de objetos y volver                       ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""");

class Funcion_Contador:#
	Valor = 0   # This represents the Valor of objects of this class
	def __init__(self, nombre_objeto):
		self.nombre_objeto = nombre_objeto
		print (nombre_objeto, 'creado')
		Funcion_Contador.Valor += 1
	def __del__(self):
		print (self.nombre_objeto, 'borrado')
		Funcion_Contador.Valor -= 1
		if Funcion_Contador.Valor == 0:
			print ('Se borro el ultimo objeto')
		else:
			print (Funcion_Contador.Valor, 'Objetos remanentes')
objerto_1 = Funcion_Contador("Primer objeto")
objerto_2 = Funcion_Contador("Segundo objeto")
objerto_3 = Funcion_Contador("Tercer objeto")
del objerto_2

#################################################################
print("""Función de Ámbito global.
El espacio de nombres del intérprete de Python corresponde al ámbito global.
La función globals() regresa el contenido del espacio de nombres del ámbito global como un objeto de tipo dict.
Cuando se invoca la función dir() sin argumentos desde el intérprete, ésta regresa un objeto de tipo list con el listado de nombres del ámbito global.
Ámbitos locales.
Cada función genera su propio espacio de nombres cada vez que es invocada. Cada uno de estos espacios de nombres es un ámbito local.
La función locals() regresa el contenido del espacio de nombres del ámbito local como un objeto de tipo dict. Cuando se invoca la función dir() sin argumentos desde una función, ésta regresa un objeto de tipo list con el listado de nombres del ámbito local.
""")
sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))
