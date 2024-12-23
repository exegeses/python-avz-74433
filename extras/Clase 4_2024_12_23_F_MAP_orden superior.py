
from colorama import *
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
#####################################################################
def pausa():
    input("\tPresione una tecla para continuar")
#####################################################################
limpiar()
from datetime import datetime, date, time

#################################################################
def Ej_ya_hechos():
    #Con tab colocaremos aquí las practicas hechas
    pass
    limpiar()
    print(F'''{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
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
    ║                              ╔══════╗   ╔═══════╗                           ║
    ║                              ║      ╚╗  ║                                   ║
    ║                              ║       ║  ║                                   ║
    ║                              ║       ║  ║                                   ║
    ║                              ║       ║  ╠══════╝                            ║
    ║                              ║       ║  ║                                   ║
    ║                              ║      ╔╝  ║                                   ║
    ║                              ╚══════╝   ╚═══════╝                           ║
    ║                                                                             ║
    ║                                                                             ║
    ║           ╔═════╗    ╔══════╗    ╔══════╗   ╔═══════╗   ╔╗      ╦           ║
    ║          ╔╝     ╚╗   ║      ╚╗   ║      ╚╗  ║           ║╚╗     ║           ║
    ║          ║       ║   ║       ║   ║       ║  ║           ║ ╚╗    ║           ║
    ║          ║       ║   ║      ╔╝   ║       ║  ║           ║  ╚╗   ║           ║
    ║          ║       ║   ╠═══╦══╝    ║       ║  ╠══════╝    ║   ╚╗  ║           ║
    ║          ║       ║   ║   ╚╗      ║       ║  ║           ║    ╚╗ ║           ║
    ║          ╚╗     ╔╝   ║    ╚╗     ║      ╔╝  ║           ║     ╚╗║           ║
    ║           ╚═════╝    ╩     ╚╝    ╚══════╝   ╚═══════╝   ╩      ╚╝           ║
    ║                                                                             ║
    ║                                                                             ║
    ║    ╔═════╗  ╦       ╦ ╔══════╗  ╔═══════╗ ╔══════╗  ╦  ╔═════╗  ╔══════╗    ║
    ║   ╔╝     ╚╗ ║       ║ ║      ╚╗ ║         ║      ╚╗ ║ ╔╝     ╚╗ ║      ╚╗   ║
    ║   ║         ║       ║ ║       ║ ║         ║       ║ ║ ║       ║ ║       ║   ║
    ║   ╚╗        ║       ║ ║      ╔╝ ║         ║      ╔╝ ║ ║       ║ ║      ╔╝   ║
    ║    ╚═════╗  ║       ║ ╠══════╝  ╠══════╝  ╠═══╦══╝  ║ ║       ║ ╠═══╦══╝    ║
    ║          ╚╗ ║       ║ ║         ║         ║   ╚╗    ║ ║       ║ ║   ╚╗      ║
    ║   ╚╗     ╔╝ ╚╗     ╔╝ ║         ║         ║    ╚╗   ║ ╚╗     ╔╝ ║    ╚╗     ║
    ║    ╚═════╝   ╚═════╝  ╩         ╚═══════╝ ╩     ╚╝  ╩  ╚═════╝  ╩     ╚╝    ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
    ║                                                                             ║
    ║                                                                             ║
    ║    lambda denera una funcion anónima                                        ║
    ║                                                                             ║
    ║  ● lambda argumentos: expresión                                             ║
    ║      Son funciones que pueden definir cualquier número de parámetros pero   ║
    ║      una única expresión. Esta expresión es evaluada y devuelta.            ║
    ║      Se pueden usar en cualquier lugar en el que una función sea requerida  ║
    ║      Estas funciones están restringidas al uso de una sola expresión.       ║
    ║      Se suelen usar en combinación con otras funciones, generalmente como   ║
    ║      argumentos de otra función.                                            ║
    ║                                                                             ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                                                             ║
    ║                                                                             ║
    ║     map, filter y reduce necesitan una funcion como primer argumento.       ║
    ║                                                                             ║
    ║                                                                             ║
    ║  ● map(funcion, iterable(s))                                                ║
    ║      aplica una función a cada uno de los elementos de una lista.           ║
    ║                                                                             ║
    ║  ● filter(funcion, iterable(s))                                             ║
    ║      Filtra una lista de elementos para los que una función devuelve True   ║
    ║                                                                             ║
    ║  ● reduce(funcion, iterable[, initial]) del módulo functools.               ║
    ║      Esta función se utiliza principalmente para llevar a cabo un cálculo   ║
    ║      acumulativo sobre una lista de valores  y devolver el resultado.       ║
    ║                                                                             ║
    ╠═════════════════════════════════════════════════════════════════════════════╣
    ║                                                                             ║
    ║                                                                             ║
    ║     y de yapa                                                               ║
    ║                                                                             ║
    ║                                                                             ║
    ║  ● zip(iterable 1, iterable 2)                                              ║
    ║                                                                             ║
    ║                                                                             ║
    ║  ● enumerate(iterable)                                                      ║
    ║                                                                             ║
    ║                                                                             ║
    ║                                                                             ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝
    ''');#Funciones incorporadas (map, zip, enumerate, reduce, filter).Funciones incorporadas (map, zip, enumerate, reduce, filter).
    pausa();limpiar()


    def funcion (parametro):
        if isinstance (parametro, (int, float)):
            return parametro**2
        elif isinstance (parametro, str):
            return parametro.title()
        elif isinstance (parametro, (list,tuple)):
            salida =[]
            for cada_dato in parametro:
                salida.append(cada_dato*2)
            return salida
        
        return None


    print (type ("hola"))
    print (type (5))
    print (type (3.14159))
    print (type (funcion))



    pausa()

    ##################################################################################
    exit()





    def sumar(d1,d2=8):
        return d1+d2

    def funcion (dato):
        print (f"{dato=}  {type(dato)}")
        


    funcion (89)
    funcion ("Hola Istea")
    funcion (8.9)
    funcion (5j)
    funcion (sumar(d2=1,d1=2))
    funcion (sumar(2))
    pausa()

    ##################################################################################
    exit()
    ##################################################################################
    #--------------------------------------------
    def sumar(d1,d2):
        return d1+d2
    #--------------------------------------------
    restar = lambda d1,d2 :d1-d2
    #--------------------------------------------
    def multi(d1,d2):
        return d1*d2
    #--------------------------------------------
    def dividir(d1,d2):
        if d2 !=0:
            return d1/d2
        else:
            return 0
    #--------------------------------------------
    def exp(d1,d2):
        return d1**d2
    #--------------------------------------------
    def div_piso(d1,d2):
        if d2 !=0:
            return d1//d2
        else:
            return 0
    #--------------------------------------------
    def resto(d1,d2):
        if d2 !=0:
            return d1%d2
        else:
            return 0
    #--------------------------------------------






    dic = { "+":sumar,
            "-":restar,
            "/":dividir,
            "//":div_piso,
            "%":resto,
            "*":multi,
            "**":exp
            }
    resultado =0
    operador = "+"
    numero = ""
    while True:
        if resultado !=0:
            operador = ""
            while operador not in dic.keys() and operador.upper() != "S":
                operador = input (f"ingrese un operador:{', '.join(dic.keys())}:")
            if (operador.upper() == "S"):
                break
            numero = ""
            while not numero.replace(".","").isdigit():
                numero = input ("ingrese un numero:")
            numero = float(numero)   
            resultado = dic[operador] (resultado, numero)
        else:
            while not numero.replace(".","").isdigit():
                numero = input ("ingrese un numero:")
            resultado = float(numero)
        print (f"{resultado=}")
        
        
    
    
    
##################################################################################
    
 
pausa();limpiar()
    
    
    
    
def iva (d1):
    return d1*1.21
entrada = [9,7,2,6,4,8,1,3,8,1,4,2]  
salida  = []    
#################### extencion ################################
for cada_dato in entrada:
    salida.append(iva(cada_dato))
print (f"""
{entrada=}
{salida =}""")
#################### comprension ################################

salida_c = [iva(cada_dato) for cada_dato in entrada]
    
print (f"""
{entrada=}
{salida_c=}""")
#################### F.o.superior ################################
  
salida_m = map(iva, entrada)
# el iterador __next__ lo agota
for cada_dato in salida_m:
    print (f"en map {cada_dato}")

salida_m_en_lista = list(salida_m)

print (f"""
map
{entrada=}
{salida_m=}
{salida_m_en_lista=}
""")  


for cada_dato in salida_m_en_lista:
    print (f"en list {cada_dato}")

  
    
print ("-"*100)
print (f"""
{entrada=}
{salida_m=}
{salida_m_en_lista=}
""")  




salida_m = map((lambda d1:d1*1.2), entrada)
# el iterador __next__ lo agota
for cada_dato in salida_m:
    print (f"en map {cada_dato}")

salida_m_en_lista = list(salida_m)

print (f"""
map
{entrada=}
{salida_m=}
{salida_m_en_lista=}
""")  
pausa()
    
    
    
    
    
    
    
    
    
    
    
##################################################################################################
#Ejercicio_Funciones_Ej_001
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║                        ╔╗      ╔╗    ╔═════╗    ╔══════╗                    ║
║                        ║╚╗    ╔╝║   ╔╝     ╚╗   ║      ╚╗                   ║
║                        ║ ╚╗  ╔╝ ║   ║       ║   ║       ║                   ║
║                        ║  ╚╗╔╝  ║   ║       ║   ║      ╔╝                   ║
║                        ║   ╚╝   ║   ╠═══════╣   ╠══════╝                    ║
║                        ║        ║   ║       ║   ║                           ║
║                        ║        ║   ║       ║   ║                           ║
║                        ╩        ╩   ╩       ╩   ╩                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
La función de orden superior map() aplica una función a una colección de datos y
 y devuelve un nuevo iterable con la función aplicada a cada argumento.


resultado = map(funcion, coleccion)
                   ^       ^coleccion de parametros para la funcion
                   L______funcion a la que llamo mandandole dato por dato de la lista
''')
print ("-"*50)
pausa()
limpiar()
##################################################################################################
def cuadrado(cada_numero):
    return cada_numero**2

lista = [1, 2, 3, 4, 5]
lista_de_cuadrados = []
for cada_numero in lista:
    lista_de_cuadrados.append(cuadrado(cada_numero))
print(f"{lista_de_cuadrados=}")

pausa()

#------------------------------------------------------------------------------------------------------
lista = [1, 2, 3, 4, 5]
lista_de_cuadrados = map(cuadrado, lista)
print (f"función: {lista_de_cuadrados}  {type(lista_de_cuadrados)}")
lista_de_cuadrados = list(lista_de_cuadrados)
print (f"función: {lista_de_cuadrados}  {type(lista_de_cuadrados)}")
pausa()

#------------------------------------------------------------------------------------------------------
lista_de_cuadrados = map((lambda cada_numero: cada_numero**2), lista)
print (f"lambda /map: {lista_de_cuadrados}  {type(lista_de_cuadrados)}")
pausa()
#------------------------------------------------------------------------------------------------------
lista_de_cuadrados = list(map((lambda cada_numero: cada_numero**2), lista))#casting de objeto mat a objeto list
print (f"lambda /list(map): {lista_de_cuadrados}  {type(lista_de_cuadrados)}")
#------------------------------------------------------------------------------------------------------
print ("-"*50)
pausa()
limpiar()

##########################################################################################################################


def multiplicar(x):
    return (x*x)
def sumar(x):
    return (x+x)
lista = [1, 2, 3, 4, 5]

lista_retorno_mult=[]
lista_retorno_sumar=[]

for index, cada_numero in enumerate(lista):
    lista_retorno_mult.append(multiplicar(cada_numero))
    lista_retorno_sumar.append(sumar(cada_numero))
    print(f"multiplic:{lista_retorno_mult[index]}\tsuma:{lista_retorno_sumar[index]}")
pausa()
#------------------------------------------------------------------------------------------------------
lista = [1, 2, 3, 4, 5]
for i in lista:
    valor = list(map(lambda x: x(i), [multiplicar, sumar]))
    print(f"multiplic:{valor[0]}\tsuma:{valor[1]}")

#------------------------------------------------------------------------------------------------------

funcs = [multiplicar, sumar]
for i in range(5):
    valor = list(map(lambda x: x(i), funcs))
    print(f"multiplic:{valor[0]}\tsuma:{valor[1]}")

#------------------------------------------------------------------------------------------------------

funcs = [multiplicar, sumar]

valor = list(map(lambda x: (x(i) for i in range(5)), funcs))
print(f"lambda x: x(i) for i in range(5) multiplic:{valor[0]}\tsuma:{valor[1]}")
# ~ for i in range(5):
    # ~ valor = list(map(lambda x:  [x[i]*x[i],x[i]+x[i]]))
    # ~ print(f"multiplic:{valor[0]}\tsuma:{valor[1]}")
#------------------------------------------------------------------------------------------------------
print ("-"*50)
pausa()
limpiar()

##########################################################################################################################
# Ordenar un conjunto de datos numéricos de forma descendente.

print('Digite seis números separados por espacios: ', end='')
numeros = list(map(int, input().split()))

print(numeros)

numeros.sort()

print(numeros)

numeros.reverse()

print(numeros)

#------------------------------------------------------------------------------------------------------
print ("-"*50)
pausa()
limpiar()

##########################################################################################################################
print('Escriba los valores x e y separados por espacio: ', end='')
x, y = map(int, input().split())
print(x, y)
#------------------------------------------------------------------------------------------------------
print ("-"*50)
pausa()
limpiar()

##########################################################################################################################

# Salida:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
print("*"*50,"\nEj Nro 1/map")
#Ej Nro 1/map:
lista1=[10,9,8,7,6,5,4,3,2,1,0];
lista2=[0,1,2,3,4,5,6,7,8,9,10];
def funcion (var_1, var_2):
    return  (var_1 * var_2)


#for  x,y in zip(lista1,lista2):
print(f"{(list( map(funcion,lista1,lista2)))=}" )
print (f"lambda : lista_resultado={(list( map(lambda x,y : x*y,lista1,lista2)))=}")
print ("-"*50)
pausa()
limpiar()
##################################################################################################
#Ej Nro 2/map:
print("*"*50,"\nEj Nro 2/map")
import math
def area_circulo(radio):
    return math.pi * radio ** 2
lista_ = [1, 2, 3]
print(f"{(list(map(area_circulo, lista_)))=}" )
print(f"lambda :{(list(map(lambda  radio :math.pi * radio ** 2, lista_)))=}" )

#Para convertir el iterador a una lista hemos empleado la función list(). También, podríamos haber recorrido el iterador con un for...in:
# ~ for resultado in map(area_circulo, lista_):
    # ~ print(resultado)
print ("-"*50)
pausa()
limpiar()
####################################################################################################
#Ej Nro 3/map:
print("*"*50,"\nEj Nro 3/map")
def cuadrado(numero):
    return numero ** 2
lista_ = [-2, 4, -6, 8]
print(f"{(list(map(cuadrado, lista_)))=}")
print(f"lambda :{(list(map(lambda x:x**2, lista_)))=}")
print ("-"*50)
pausa()
limpiar()
##################################################################################################
#Ej Nro 4/map:
'''
Con map() genera una función que regrese una lista con el len cada palabra de un string.
Ojo con los simbolos pegados a las palabras xq se separa por espacio.
'''
print("*"*50,"\nEj Nro 4/map")
def longitud_palabras(string_): # Función
    len_palabra = list(map(len, string_.split())) # Longitud de cada palabra
    return len_palabra # Retornar resultado
string = 'Hola Ariel, ¿como va Python? ¿volvemos a basic de comodore?'
print (f"{longitud_palabras(string)=}")
print(f"lambda :{(list(map(lambda x:len(x),  string.split())))=}")
print ("-"*50)
pausa()
limpiar()
##################################################################################################
#Ej Nro 5/map:
print("*"*50,"\nEj Nro 5/map")
def filtro (var_1, var_2):
    #----------------------------------
    var3=(var_1 * var_2)
    # ~ if   (var3 >= 10):
        # ~ return var3
    #----------------------------------
    # ~ return  ((var_1 * var_2) >= 10)
    #----------------------------------
    return var3
lista1=[10,9,8,7,6,5,4,3,2,1,0];
lista2=[0,1,2,3,4,5,6,7,8,9,10];
print(f"lista_filtrada={list( map(filtro,lista1,lista2))=}")
print(f"lambda : lista_filtrada={(list( map(lambda x,y : x*y ,lista1,lista2)))=}")
print ("-"*50)
pausa()
limpiar()
##################################################################################################
dato = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
cubo = list(map(lambda x: x**3, dato))
print(cubo)
print ("-"*50)
pausa()
limpiar()
##################################################################################################
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
print ("-"*50)
pausa()
limpiar()
##################################################################################################

print('''
La función map() toma una función y una lista y aplica esa función a cada elemento de esa lista, produciendo una nueva lista.

Esta función trabaja de una forma muy similar a filter(), con la diferencia que en lugar de aplicar una condición a un elemento de una lista o secuencia,
aplica una función sobre todos los elementos y como resultado se devuelve un lista de números doblado su valor:
''')
def doblar(numero):
    return numero*2

numeros = [2, 5, 10, 23, 50, 33]
print(F"{map(doblar, numeros)=}")
# ~ [4, 10, 20, 46, 100, 66]
# ~ Usted puede simplificar el código anterior usando una función lambda para substituir la llamada de una función definida, como se muestra a continuación:
print(F"{map(lambda x: x*2, numeros)=}")

# ~ [4, 10, 20, 46, 100, 66]
# ~ La función map() se utiliza mucho junto a expresiones lambda ya que permite evitar escribir bucles for.

# ~ Además se puede utilizar sobre más de un objeto iterable con la condición que tengan la misma longitud. Por ejemplo, si requiere multiplicar los números de dos listas:

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
print(F"{map(lambda x,y : x*y, a,b)=}")
# ~ [6, 14, 24, 36, 50]
# ~ E incluso usted puede extender la funcionalidad a tres listas o más:

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = [11, 12, 13, 14, 15]
print(F"{map(lambda x,y,z : x*y*z, a,b,c)=}")
# ~ [66, 168, 312, 504, 750]
# ~ 5.5.2.1. Mapeando objetos
# ~ Evidentemente, siempre que la función map() la utilice correctamente podrá mapear una serie de objetos sin ningún problema:

print ("-"*50)
pausa()
limpiar()
##################################################################################################

def sumar(x):
    return x+100
def cuadrado(x):
    return x**2
def superior(funcion,lista):
    resultado =funcion(4)
    # ~ for n in lista:
        # ~ resultado.append(funcion(n))
    return resultado
numeros = [2,5,10]
print(f"{superior(sumar,numeros)=}")
# ~ out: [102, 105, 110]
print(f"{superior(cuadrado,numeros)=}")
# ~ out: [4, 25, 100]
from statistics import mean
mean([1, 2, 3, 4, 4])


print(f"{mean([-1.0, 2.5, 3.25, 5.75])=}")
# ~ from fractions import Fraction as F
# ~ mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
# ~ Fraction(13, 21)

# ~ from decimal import Decimal as D
# ~ mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
def esPositivo(n):
    return n > 0
def positivosConFilter(numeros):
    return filter(esPositivo, numeros)
for x in (positivosConFilter([2, -1, 4, 0, -10, -2, 6, -8])):
    print (f"filter(esPositivo, numeros)",x)
print ("-"*50)
pausa()
limpiar()
##################################################################################################
# add 3 to the parameter
def add3(x):
    return x + 3
# One list [5,6,7] with normal function
print( list( map(add3, [5,6,7]) ) )
# One list [5,6,7] with lambda
print( list( map(lambda x: x + 3, [5,6,7]) ) )
# Two lists [1,2,3] and [5,6,7] with lambda
print( list( map(lambda x, y: x + y, [1,2,3], [5,6,7]) ) )

# Dictionary objects in a list
puntos_total = [
                {"usuario": 'Juan',
                 "puntos": 60
                },
                {"usuario": 'Ana',
                 "puntos": 70
                },
                {"usuario": 'Lu',
                 "puntos": 90
                }
            ]
print(f"{list( map(lambda x: x['usuario'], puntos_total) )=}")
print(f"{list( map(lambda x: x['puntos'] + 10, puntos_total) )=}")
print(f"{list( map(lambda x: x['usuario'] == 'Ana', puntos_total) )=}")
