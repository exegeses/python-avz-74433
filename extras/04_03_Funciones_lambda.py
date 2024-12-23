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
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
║                              Funciones y Metodos                            ║
║                              -------------------                            ║
║          Funciones    Description                                           ║
║                   lambda                                                    ║
║                                                                             ║
║          Metodos son funciones dentro de clases donde se deberia instanciar ║
║                   a la clase con self nombre_objeto                         ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║                              Funciones,  Metodos                            ║
║                                  y Generadores                              ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝''')


#   son funciones anomimas pero se vuelcan en un objeto
#       lambda arg_entrada : expression de salida
# ~ lambda <arguments> : <value_1> if <condition_1> else (<value_2> if <condition_2> else <value_3>)


def fun ( valor_1, valor_2):        #       ingreso 2 agumentos
    return(valor_1 * valor_2)       #       regreso uno
print (f"{fun(2,4)=}")
print (f"{fun(6,4)=}")
print (f"{fun(valor_2=2, valor_1=4)=}")
print ("*"*100)
fun = lambda valor_1, valor_2 : (valor_1 * valor_2)
#           ^                ^  \_________________/
#           |_sin parentesis_|        return
print (f"{fun(2,4)=}")
print (f"{fun(6,4)=}")
print (f"{fun(valor_2=2, valor_1=4)=}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################


def fun (valor_1, valor_2) : 
    if valor_1 > valor_2 :
        return valor_1 * valor_2 
    else:
        return valor_1 / valor_2

fun = lambda valor_1, valor_2 : valor_1 * valor_2 if valor_1 > valor_2 else  valor_1 / valor_2
#           ^                ^  \_______________/                            \_______________/
#           |_sin parentesis_|        return                 O                     return        
print (f"{fun(2,4)=}")
print (f"{fun(valor_2=6,valor_1=4)=}")
print("*"*50)
pausa()
limpiar()

def fun (valor_1, valor_2) : 
    return (valor_1 * valor_2 , valor_1 / valor_2)#      return una tupla () o lista []
print (f"{fun(2,4)=}")
print (f"{fun(6,4)=}")
print (f"{fun(valor_2=2, valor_1=4)=}")
fun = lambda valor_1, valor_2 : (valor_1 * valor_2 , valor_1 / valor_2)
#           ^                ^  \_____________________________________/
#           |_sin parentesis_|        return una tupla  () o lista []
print (f"{fun(2,4)=}")
print (f"{fun(6,4)=}")
print (f"{fun(valor_2=2, valor_1=4)=}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
fun = lambda x : int(x) if x.isdigit() else  "Error"
x=input('ingrese un numero entero : ')
print (f"{fun(x)} {type(fun)}")
#       o
print (f"{fun(input('ingrese un numero entero : '))} {type(fun)}")
#------------------------------------------------------------------------------------------------------
def fun (x) : 
    if x.isdigit() :
        return int(x) 
    elif x.replace(".","",1).isdigit() :
        return float(x)
    else :
        return "Error"

fun = lambda x : int(x) if x.isdigit() else  (float(x)   if x.replace(".",",1).isdigit() else "Error")
x=input('ingrese un numero : ')
print (f"{fun(x)} {type(fun)}")
#       o
print (f"{fun(input('ingrese un numero : '))} {type(fun)}")
#------------------------------------------------------------------------------------------------------
# ~ print (z :=input('ingrese un dato : '))

print("*"*50)
pausa()
limpiar()
#######################################################################################################
def fun (n): 
    if n%10 == 0 :
        return n 
    elif  n%2 == 0 :
        return  n**2 
    else:
        return n**3 


fun = lambda n: n if n%10 == 0 else ( n**2 if n%2 == 0 else n**3 )
print(f"{fun(4)=}")
print(f"{fun(3)=}")
print(f"{fun(20)=}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################

def fun  ( x,y ): 
    if x < y :
        return f"{x} es menor que {y}" 
    elif x > y :
        return f"{x} es mayor que {y}" 
    else:
        return f"{x} es igual a {y}"


fun = lambda x,y : f"{x} es menor que {y}" if x < y else (f"{x} es mayor que {y}" if x > y else f"{x} es igual a {y}")
print (fun(2,4))
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################

# Iterating With Python Lambdas
  
# list of numbers
l1 = [4, 2, 13, 21, 5]
  
# list of square of numbers 
# lambda function is used to iterate 
# over list l1
l2 = list(map(lambda v: v ** 2, l1))
  
# print list
print(l2)


numbers = [2, 8, 0, 1, 1, 9, 7, 7]

description = {
                "cantidad de objetos": len(numbers),
                "suma": sum(numbers),
                "promedio": sum(numbers) / len(numbers),
                }
print (f"{description=}")

description = {
                "cantidad de objetos": (num_len := len(numbers)),
                "suma": (num_sum := sum(numbers)),
                "promedio": num_sum / num_len,
                }

print (f"{description=}")
print (f"{num_sum=}")
print (f"{num_len=}")
numbers = [7, 6, 1, 4, 1, 8, 0, 6]
def slow(x):
    return (x**2)
results = [slow(num) for num in numbers if slow(num) > 0]
print(f"{results=}")
results = list(filter(lambda value: value > 0, (slow(num) for num in numbers)))
print(f"{results=}")
# Using a double list comprehension
results = [value for num in numbers for value in [slow(num)] if value > 0]
print(f"{results=}")
results = [value for num in numbers if (value := slow(num)) > 0]
print(f"{results=}")
#------------------------------------------------------------------------------------------------------
print("*"*50)
pausa()
limpiar()
#######################################################################################################
pausa()


print((lambda x, y, z: x + y + z)(1, 2, 3))

print((lambda x, y, z=3: x + y + z)(1, 2))

print((lambda x, y, z=3: x + y + z)(1, y=2))

print((lambda *args: sum(args))(1,2,3))

print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))

print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))


# ~ lst = [lambda i=i: i + i for i in range(1, 60)]

# ~ xx= lambda _: i+i for i in lista_numeros 


# ~ for f in lst:
    # ~ print(f())



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

def revertir(cadena):
    if len(cadena)>=2:
        return cadena[::-1]
    else:
        return False

revertir = lambda cadena: cadena[::-1] if len(cadena)>=2 else False
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

print(""" y ahora
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
#Ejercicio_Funciones_Ej_011
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

#################################################################
#Ejercicio_Funciones_Ej_013
# Ejercicio 5.6: Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud.




Nombre_diccionario_1=[
                    {"Nombre":"Ariel","Apellido":"Garcia","Edad":47},
                    {"Nombre":"Daniela","Apellido":"Perez","Edad":48},
                    {"Nombre":"Ana","Apellido":"Gonzalez","Edad":42},
                    {"Nombre":"Juan","Apellido":"Gomez","Edad":41},
                    {"Nombre":"Pepe","Apellido":"Martin","Edad":43}
                ]

Nombre_diccionario_1 = sorted(Nombre_diccionario_1 ,  key=lambda Nombre_diccionario_1: Nombre_diccionario_1 ['Edad'])
print("Nombre_diccionario_1:",Nombre_diccionario_1)
nuevo(5);
#################################################################
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
ordenado =  [sorted(dato) for dato in [array]]
print ("Ordenado:",ordenado)
nuevo(6);
#################################################################
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
ordenado =  [dato for dato in array if dato % 2 ==0 ]
print ("Ordenado:",ordenado)
nuevo(6);
#################################################################
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
ordenado =  [dato if dato % 2 ==0 else "No tomar xq es impar" for dato in array]
print ("Ordenado:",ordenado)
nuevo(6);
#################################################################
lista = list(filter(lambda x : all( x % y !=0 for y in range (2,x)),range (2,50)))
print ("lista primos:",lista)
nuevo(7);
#################################################################

g = [(x,y) for x in ["origen","destino"] for y in [34.46, 56.2]]
print (g)
nuevo(8);
#################################################################
# ~ fibo= [0,1]
# ~ fibSerie=[fibo.append(fibo[-2]+fibo[-1]) for i in range(5)]
# ~ print("Fibonacci:",fibSerie)

nuevo(9);
#################################################################
heights = {'John': 175, 'Jane': 150, 'Jim': 155, 'Matt': 170}

tall = {key:value for (key, value) in heights.items() if value >= 170}

print(tall)
# Returns: {'John': 175, 'Matt': 170}
nuevo(10);
#################################################################
# ~ campos = data_mar.columns.values.tolist()
# ~ eliminar = ["LECTURA_ENERGIA_ACTIVA", "LECTURA_ENERGIA_REACTIVA", \
    # ~ "LECTURA_POTENCIA_TOTAL"]
# ~ data_mar = data_mar[[e for e in campos if e not in eliminar]]
my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])
#################################################################

# Python3 code to demonstrate working of
# Maximum record value key in dictionary
# Using max() + lambda function

# initializing dictionary
test_dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
             'is' : {'Manjeet' : 8, 'Himani' : 9},
             'best' : {'Manjeet' : 10, 'Himani' : 15}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing search key
key = 'Himani'

# Maximum record value key in dictionary
# Using max() + lambda function
res = max(test_dict, key = lambda sub: test_dict[sub][key])

# printing result
print("The required key is : " + str(res))
#################################################################
# ~ { expresionGeneraClave : expresionGeneraValor for variable in lista if condicion }
# ~ Veamos un ejemplo:

# ~ Dada una lista de Productos queremos generar un diccionario con sus nombres y precios.

# ~ productos = [Producto("aceite", 6.8), Producto("pan", 2.5),  Producto("agua", 6.4)]
# ~ precios = { p.nombre : p.precio for p in productos }
# ~ print "Precios", precios

def square(x): 
    return lambda: x * x
lst = [square(i) for i in [1, 2, 3, 4, 5]]
for f in lst: 
    print(f())
    
lst = [lambda i=i: i + i for i in range(1, 6)]
for f in lst:
    print(f())
exit()

