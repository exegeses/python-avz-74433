
from colorama import *
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
#####################################################################
def pausa():
    input("\tPresione una tecla para continuar")
#####################################################################
limpiar()
print("""\033[1;37;44m\n
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
╠═════════════════════════════════════════════════════════════════════════════╣\033[0;m
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
# ~ entrada = []
# ~ def funcion(entrada):
    # ~ print (entrada,type(entrada))

# ~ x = [10, 20, 30]
# ~ funcion(x)
# ~ print(x)

# ~ print (entrada,type(entrada))
# ~ def funcion(a,b,*args,c=100,**kwargs):
    # ~ print(a)
    # ~ print(b)
    # ~ print(args)
    # ~ print(c)
    # ~ print(kwargs)
# ~ a=1
# ~ b=2
# ~ l=[1,2,3]
# ~ d={"a":1,"b":2}
# ~ c=1
# ~ funcion(a,b,*l,c,**d)
def sumar(x):
    return x+100
def cuadrado(x):
    return x**2
def superior(funcion,lista):
    resultado = []
    for n in lista:
        resultado.append(funcion(n))
    return resultado
numeros = [2,5,10]
print(superior(sumar,numeros))
out: [102, 105, 110]
print(superior(cuadrado,numeros))
out: [4, 25, 100]
