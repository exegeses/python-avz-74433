


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make the data
x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Default behavior is axlim_clip=False
ax.plot_wireframe(X, Y, Z, color='C0')

# When axlim_clip=True, note that when a line segment has one vertex outside
# the view limits, the entire line is hidden. The same is true for 3D patches
# if one of their vertices is outside the limits (not shown).
ax.plot_wireframe(X, Y, Z, color='C1', axlim_clip=True)

# In this example, data where x < 0 or z > 0.5 is clipped
ax.set(xlim=(0, 10), ylim=(-5, 5), zlim=(-1, 0.5))
ax.legend(['axlim_clip=False (default)', 'axlim_clip=True'])

plt.show()



exit()













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
print ("*"*50)###########################################################################

def filtro (cada_entrada):
    """
    la funcion filtro requiere:
        como parametro de entrada explicito cada_entrada esperando un numero
        como parametro de entrada implicito global nombre como string
        como parametro de entrada implicito salidas como lista
        como parametro de entrada implicito filtrados como lista
        
    posee parametros explicitos de salida con el argumento "ok"
    """
    global nombre
    
    if not isinstance (filtrados , list):
        print ("verifique que filtrados debe existir como una lista")
        return
    
    if cada_entrada %2 !=0:
        cada_salida = "impar"
        filtrados.append(cada_entrada)
        salidas.append(cada_salida)
        nombre = nombre.upper()
        print (f"""
        {cada_entrada=}
        {cada_salida=}
        {filtrados=}
        {nombre=}
        en funcion {id(nombre)=}
        """)
        return "ok"
nombre = "Ariel" 
salidas = []
filtrados = []
entradas = [9,5,1,7,4,6,3,2,8,0,1,5,9]
print ("filtros")
print (f"antes {id(nombre)=}")


help (filtro)

for cada_entrada in entradas:
    filtro (cada_entrada)


    
print (f"""
{entradas=}
{salidas=}
{filtrados=}
{nombre=}
despues {id(nombre)=}
""")    
pausa()
print ("*"*50)
salidas =   [  "impar"     for cada_entrada in entradas   if cada_entrada %2 !=0 ]
filtrados = [cada_entrada  for cada_entrada in entradas   if cada_entrada %2 !=0 ] 
print (f"""
{entradas=}
{salidas=}
{filtrados=}
""")    

# ~ pausa()






exit()
import this
"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

"""








