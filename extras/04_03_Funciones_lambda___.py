from __init__ import *
from datetime import datetime, date, time
#################################################################
def Ej_ya_hechos():
    #Con tab colocaremos aquí las practicas hechas
    pass
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
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
║    ╦           ╔═════╗     ╔╗      ╔╗   ╔══════╗    ╔══════╗     ╔═════╗    ║
║    ║          ╔╝     ╚╗    ║╚╗    ╔╝║   ║      ╚╗   ║      ╚╗   ╔╝     ╚╗   ║
║    ║          ║       ║    ║ ╚╗  ╔╝ ║   ║       ║   ║       ║   ║       ║   ║
║    ║          ║       ║    ║  ╚╗╔╝  ║   ║      ╔╝   ║       ║   ║       ║   ║
║    ║          ╠═══════╣    ║   ╚╝   ║   ╠══════╣    ║       ║   ╠═══════╣   ║
║    ║          ║       ║    ║        ║   ║      ╚╗   ║       ║   ║       ║   ║
║    ║          ║       ║    ║        ║   ║      ╔╝   ║      ╔╝   ║       ║   ║
║    ╚═══════   ╩       ╩    ╩        ╩   ╚══════╝    ╚══════╝    ╩       ╩   ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║    Función lambda                                                           ║
║    --------------                                                           ║
║    Son funciones que sólo ocupan una línea.                                 ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
pausa()
limpiar()
#################################################################
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                  Lambda                                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
#################################################################
print (f"Forma clasica".center(50))
def CalculoVolumneCubo(b,a,p):#base, altura, profundidad
    return (b*a*p)
print ( f"{CalculoVolumneCubo(10,2,5)=}")
print ( f"{CalculoVolumneCubo(20,10,50)=}")
print (f"Forma lambda".center(50))
CalculoVolumneCubo=lambda b,a,p : (b*a*p)#<---------return
#                           ^
#                           L___parametros de entrada
print ( f"{CalculoVolumneCubo(10,2,5)=}")
print ( f"{CalculoVolumneCubo(20,10,50)=}")
print ("-"*50)
pausa()
limpiar()
#################################################################
impar = lambda numero: numero%2 != 0
impar(5)
 - operaciones de cadena
#slicing en sentido inverso:
revertir = lambda cadena: cadena[::-1]
print(f"{revertir('Python es genial')=}")
#################################################################
#Función lambda - varios parámetros
sumar = lambda x,y: x+y
print(f"{sumar(5,2)=")
#################################################################
datos=lambda nombre, puesto : f"el empleado {nombre} trabaja como {puesto}"
print (f"{datos('Ariel','Mantenimiento')}")
print ("-"*50)
pausa()
limpiar()
#################################################################

def doblar(num):
    resultado = num*2
    return resultado
valor=55.5
print("el doble es :",doblar(valor))
print ("-"*50)
doblar = lambda num: num*2
print ("doblar = lambda num: num*2")
print ("el doble es :",doblar(valor))
pausa()
print ("-"*50)
impar = lambda num: num%2 != 0
print ("impar = lambda num: num%2 != 0")
print (f"el valor ingresado es de {valor}")
print("es impar :",impar(valor))
print ("-"*50)
pausa()
limpiar()

#################################################################

array = [11, 25, 34, 100,0, 23]
print(f"array = {array}")

dato = lambda x :x**2#<----salida
#             ^
#             L__dato q recibe
print ("dato = lambda x :x**2")
for valor in array:
    print ("dato(valor)**2:",dato(valor))

print ("-"*50)
pausa()
limpiar()
#################################################################

dato = lambda x: x*x

lista = [1,2,3,5,8,13]
print (f"lista{lista}")
print ("dato = lambda x :x*x")
for elemento in lista:
    print(f"elemento*elemento:",dato(elemento))
print ("-"*50)
pausa()
limpiar()
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
print ("-"*50)
pausa()
limpiar()
#################################################################
mensaje = lambda numero: f"el número ingresado es: {numero}"
print("texto:",mensaje(2))
print ("-"*50)
pausa()
limpiar()
#################################################################
binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2
print ("binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2")
print ("binomio_cuadrado de (2,3):",binomio_cuadrado(2,3))

print ("-"*50)
pausa()
limpiar()
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
print ("-"*50)
pausa()
limpiar()
##############################################################
lista_anidada=[ ["Jose", 30], ["pedro", 55],["Ariel",47],["Ana",40],["Bea", 30]]
print (f"lista_anidada:{lista_anidada}")
lista_anidada.sort(key = lambda dato : dato [1])
print ("lista_anidada.sort(key = lambda dato : dato [1])<---1 es el 2do dato de una lista")
print (f"lista_anidada ordenadas x edad:{lista_anidada}")
print ("-"*50)
pausa()
limpiar()
#################################################################
#lambda <arguments> : <value_1> if <condition_1> else (<value_2> if <condition_2> else <value_3>)

dato = lambda x :1000/x if (x  != 0) else "Error"
array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x :1000/x if (x  != 0) else 'Error'")
for valor in array:
    print (f"1000/ {valor}= {dato(valor)}")
print ("-"*50)
pausa()
limpiar()
#################################################################

dato = lambda x : True if (x > 10 and x < 30) else False
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x : True if (x > 10 and x < 30) else False")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
pausa()
limpiar()
#################################################################

dato = lambda x: x**2 if x%2 == 0 else x**3
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x: x**2 if x%2 == 0 else x**3")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
pausa()
limpiar()
#################################################################
dato = lambda x : x*2 if x <=25 else (x*3 if x < 50 else -x)
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print("dato = lambda x : x*2 if x <=25  else (x*3 if x < 50 else -x)")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
pausa()
limpiar()
#################################################################

dato = lambda x: x if x%10 == 0 else ( x**2 if x%2 == 0 else x**3 )

Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x: x if x%10 == 0 else ( x**2 if x%2 == 0 else x**3 )")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
pausa()
limpiar()
#################################################################

#numeros_buscados = [numero for numero in range(100,1000) if suma_cubos(numero)==numero]
#################################################################
dato = lambda x :x**2 if x % 2 == 0 else "Impar"
print ("Array:", array)
print ("dato = lambda x :x**2 if x % 2 == 0 else 'Impar'")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
pausa()
limpiar()


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
print ("-"*50)
pausa()
limpiar()
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
pausa()
limpiar()
#################################################################
# Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud.
Nombre_diccionario_1=[
                    {"Nombre":"Ariel","Apellido":"Garcia","Edad":47},
                    {"Nombre":"Daniela","Apellido":"Perez","Edad":48},
                    {"Nombre":"Ana","Apellido":"Gonzalez","Edad":42},
                    {"Nombre":"Juan","Apellido":"Gomez","Edad":41},
                    {"Nombre":"Pepe","Apellido":"Martin","Edad":43}
                ]

Nombre_diccionario_1 = sorted(Nombre_diccionario_1 ,  key=lambda Nombre_diccionario_1: Nombre_diccionario_1 ['Edad'])
print("Nombre_diccionario_1:",Nombre_diccionario_1)
print ("-"*50)
pausa()
limpiar()
#################################################################
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
ordenado =  [sorted(dato) for dato in [array]]
print ("Ordenado:",ordenado)
print ("-"*50)
pausa()
limpiar()
#################################################################
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
ordenado =  [dato for dato in array if dato % 2 ==0 ]
print ("Ordenado:",ordenado)
print ("-"*50)
pausa()
limpiar()
#################################################################
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
ordenado =  [dato if dato % 2 ==0 else "No tomar xq es impar" for dato in array]
print ("Ordenado:",ordenado)
print ("-"*50)
pausa()
limpiar()
#################################################################
lista = list(filter(lambda x : all( x % y !=0 for y in range (2,x)),range (2,50)))
print ("lista primos:",lista)
print ("-"*50)
pausa()
limpiar()
#################################################################

g = [(x,y) for x in ["origen","destino"] for y in [34.46, 56.2]]
print (g)
print ("-"*50)
pausa()
limpiar()
#################################################################
heights = {'John': 175, 'Jane': 150, 'Jim': 155, 'Matt': 170}

tall = {key:value for (key, value) in heights.items() if value >= 170}

print(tall)
print ("-"*50)
pausa()
limpiar()
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
print ("-"*50)
pausa()
limpiar()
#################################################################

# Python3 code to demonstrate working of
# Maximum record value key in dictionary
# Using max() + lambda function

# initializing dictionary
ejemplo = { 'clave1' : {'Equipo A' : 1,  'Equipo B' : 10},
            'clave2' : {'Equipo A' : 5,  'Equipo B' : 5},
            'clave3' : {'Equipo A' : 10, 'Equipo B' : 1}}

# printing original dictionary
print(f"datos del diccionario :{ejemplo} ")

# initializing search key
key = 'Equipo B'

# Maximum record value key in dictionary
# Using max() + lambda function
res = max(ejemplo, key = lambda sub: ejemplo[sub][key])

# printing result
print(f"datos del diccionario :{res} ")
print ("-"*50)
pausa()
limpiar()
#################################################################
# ~ { expresionGeneraClave : expresionGeneraValor for variable in lista if condicion }
# ~ Veamos un ejemplo:

# ~ Dada una lista de Productos queremos generar un diccionario con sus nombres y precios.

# ~ productos = [Producto("aceite", 6.8), Producto("pan", 2.5),  Producto("agua", 6.4)]
# ~ precios = { p.nombre : p.precio for p in productos }
# ~ print "Precios", precios


geoloc = (
(15.623037, 13.258358),
(55.147488, -2.667338),
(54.572062, -73.285171),
(3.152857, 115.327724),
(-40.454262, 172.318877)
)

# Ordenación por longitud (primer elemento de la tupla)
print(f"{sorted(geoloc)=}")
# ~ [(-40.454262, 172.318877),
 # ~ (3.152857, 115.327724),
 # ~ (15.623037, 13.258358),
 # ~ (54.572062, -73.285171),
 # ~ (55.147488, -2.667338)]

# Ordenación por latitud (segundo elemento de la tupla)
print(f"{sorted(geoloc, key=lambda t: t[1])=}")
# ~ [(54.572062, -73.285171),
 # ~ (55.147488, -2.667338),
 # ~ (15.623037, 13.258358),
 # ~ (3.152857, 115.327724),
 # ~ (-40.454262, 172.318877)]
print ("-"*50)
pausa()
limpiar()
