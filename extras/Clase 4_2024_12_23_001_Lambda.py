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

#################################################################
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                  Lambda                                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m""")

# ~ def impar(numero):
    # ~ return numero%2!=0
    
impar = lambda numero: numero%2 != 0
print(f"{type(impar)=}")
r=impar(5)
print (f"{r=}")
r=impar(50)
print (f"{r=}")

r=impar(15)
print (f"{r=}")


#True
#Función lambda - operaciones de cadena

#A continuación, se presenta un ejemplo para darle la vuelta a una cadena rebanándola en sentido inverso:

revertir = lambda cadena: cadena[::-1]
print(revertir("Plone"))
#'enolP'
print(revertir("Python es Genial!!!!!!!!!!!"))
#'Plone'
#Función lambda - varios parámetros

#A continuación, se presenta un ejemplo para varios parámetros, por ejemplo para sumar dos números:

sumar = lambda x,y: x+y
print(sumar(5,2))
print ("-"*50)#################################################################
pausa()
limpiar()
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


print ("-"*50)#################################################################
pausa()
limpiar()

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

print ("-"*50)#################################################################
pausa()
limpiar()
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

print ("-"*50)#################################################################
pausa()
limpiar()

dato = lambda x: x*x

lista = [1,2,3,5,8,13]
print (f"lista{lista}")
print ("dato = lambda x :x*x")
for elemento in lista:
    print(f"elemento^elemento:",dato(elemento))


print ("-"*50)#################################################################
pausa()
limpiar()

print (""" Lambda, con 2 argumentos:""")

area_triangulo = (lambda b,h: b*h/2)
medidas = [(34, 8), (26, 8), (44, 18)]
print (f"medidas{medidas}")
print ("area_triangulo = (lambda b,h: b*h/2)")
for datos in medidas:
    base = datos[0]
    altura = datos[1]
    print("area_triangulo(base, altura):",area_triangulo(base, altura))
print ("-"*50)#################################################################
pausa()
limpiar()
mensaje = lambda numero: f"el número ingresado es: {numero}"
print("texto:",mensaje(2))
pausa()
print ("-"*50)#################################################################
pausa()
limpiar()
binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2
print ("binomio_cuadrado = lambda a,b: a**2 + 2*a*b + b**2")
print ("binomio_cuadrado de (2,3):",binomio_cuadrado(2,3))
pausa()
print ("-"*50)#################################################################
pausa()
limpiar()
suma_cubos = lambda numero: sum(int(digito)**3 for digito in str(numero))
numeros_buscados = [numero for numero in range(0,1200) if suma_cubos(numero)==numero]
print ("suma_cubos = lambda numero: sum(int(digito)**3 for digito in str(numero))")
print ("numeros_buscados = [numero for numero in range(100,1000) if suma_cubos(numero)==numero]")
print ("numeros_buscados:",numeros_buscados)
print ("-"*50)#################################################################
pausa()
limpiar()
lista_anidada=[ ["Jose", 30], ["pedro", 55],["Ariel",47],["Ana",40],["Bea", 30]]
print (f"lista_anidada:{lista_anidada}")
lista_anidada.sort(key = lambda dato : dato [1])
print ("lista_anidada.sort(key = lambda dato : dato [1])<---1 es el 2do dato de una lista")
print (f"lista_anidada ordenadas x edad:{lista_anidada}")
print ("-"*50)#################################################################
pausa()
limpiar()
#lambda <arguments> : <value_1> if <condition_1> else (<value_2> if <condition_2> else <value_3>)

dato = lambda x :1000/x if (x  != 0) else "Error"
array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x :1000/x if (x  != 0) else 'Error'")
for valor in array:
    print (f"1000/ {valor}= {dato(valor)}")
print ("-"*50)
print ("-"*50)#################################################################
pausa()
limpiar()

dato = lambda x : True if (x > 10 and x < 30) else False
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x : True if (x > 10 and x < 30) else False")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)
print ("-"*50)#################################################################
pausa()
limpiar()

dato = lambda x: x**2 if x%2 == 0 else x**3
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x: x**2 if x%2 == 0 else x**3")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)#################################################################
pausa()
limpiar()
dato = lambda x : x*2 if x <=25 else (x*3 if x < 50 else -x)
Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print("dato = lambda x : x*2 if x <=25  else (x*3 if x < 50 else -x)")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)#################################################################
pausa()
limpiar()
def dato(x):
    if x%10==0:
        s=x
    else:
        if x %2==0:
            s=x**2
        else:
            s=x**3
    return s

dato = lambda x: x if x%10 == 0 else ( x**2 if x%2 == 0 else x**3 )

Array = [11, 25, 34, 100,0, 23]
print ("Array:", array)
print ("dato = lambda x: x if x%10 == 0 else ( x**2 if x%2 == 0 else x**3 )")
for valor in array:
    print (f"test",valor,dato(valor))

print ("-"*50)#################################################################
pausa()
limpiar()
dato = lambda x :x**2 if x % 2 == 0 else "Impar"
print ("Array:", array)
print ("dato = lambda x :x**2 if x % 2 == 0 else 'Impar'")
for valor in array:
    print (f"test",valor,dato(valor))
print ("-"*50)#################################################################
pausa()
limpiar()

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
print ("-"*50)#################################################################
pausa()
limpiar()
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

print ("-"*50)#################################################################
pausa()
limpiar()


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
print ("-"*50)#################################################################
pausa()
limpiar()

# Encontrar las palabras de una lista que tienen al menos 5 caracteres de longitud.
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                 sin      Lambda                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m""")
paises = ['Colombia', 'Perú', 'Alemania', 'Estados Unidos', 'China', 'Argentina', 'Irán', 'Irak']

print('Contenido actual de la variable `paises`:', paises)
print('Cantidad actual de elementos de la variable `paises`:', len(paises))

print()

# Solución #1:
print('Solución #1')
paises_mas_5_caracteres = []

for p in paises:
    if len(p) >= 5:
        paises_mas_5_caracteres.append(p)

print('Contenido actual de la variable `paises_mas_5_caracteres`:', paises_mas_5_caracteres)
print('Cantidad actual de elementos de la variable `paises_mas_5_caracteres`:', len(paises_mas_5_caracteres))

print()

# Solución #2:
print('Solución #2')

paises_mas_5_caracteres = [p for p in paises if len(p) >= 5]
print('Contenido actual de la variable `paises_mas_5_caracteres`:', paises_mas_5_caracteres)
print('Cantidad actual de elementos de la variable `paises_mas_5_caracteres`:', len(paises_mas_5_caracteres))


print ("-"*50)#################################################################
pausa()
limpiar()

Nombre_diccionario_1=[
                    {"Nombre":"Ariel","Apellido":"Garcia","Edad":47},
                    {"Nombre":"Daniela","Apellido":"Perez","Edad":48},
                    {"Nombre":"Ana","Apellido":"Gonzalez","Edad":42},
                    {"Nombre":"Juan","Apellido":"Gomez","Edad":41},
                    {"Nombre":"Pepe","Apellido":"Martin","Edad":43}
                ]

Nombre_diccionario_1 = sorted(Nombre_diccionario_1 ,  key=lambda Nombre_diccionario_1: Nombre_diccionario_1 ['Edad'])
print("Nombre_diccionario_1:",Nombre_diccionario_1)
print ("-"*50)#################################################################
pausa()
limpiar()
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
ordenado =  [sorted(dato) for dato in [array]]
print ("Ordenado:",ordenado)
print ("-"*50)#################################################################
pausa()
limpiar()
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
ordenado =  [dato for dato in array if dato % 2 ==0 ]
print ("Ordenado:",ordenado)
print ("-"*50)#################################################################
pausa()
limpiar()
array = [0, 2, -5, 8, -10, 23, 31, 35, 36, -47, 50, -77, 93]
ordenado =  [dato if dato % 2 ==0 else "No tomar xq es impar" for dato in array]
print ("Ordenado:",ordenado)
print ("-"*50)#################################################################
pausa()
limpiar()
lista = list(filter(lambda x : all( x % y !=0 for y in range (2,x)),range (2,50)))
print ("lista primos:",lista)
print ("-"*50)#################################################################
pausa()
limpiar()
g = [(x,y) for x in ["origen","destino"] for y in [34.46, 56.2]]
print (g)
print ("-"*50)#################################################################
pausa()
limpiar()
heights = {'John': 175, 'Jane': 150, 'Jim': 155, 'Matt': 170}

tall = {key:value for (key, value) in heights.items() if value >= 170}

print(tall)
print ("-"*50)#################################################################
pausa()
limpiar()
# ~ campos = data_mar.columns.values.tolist()
# ~ eliminar = ["LECTURA_ENERGIA_ACTIVA", "LECTURA_ENERGIA_REACTIVA", \
    # ~ "LECTURA_POTENCIA_TOTAL"]
# ~ data_mar = data_mar[[e for e in campos if e not in eliminar]]
my_dict = {'x':500, 'y':5874, 'z': 560}

key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])
print ("-"*50)#################################################################
pausa()
limpiar()
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
print ("-"*50)#################################################################
pausa()
limpiar()











