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

print ("operador ternario".center (50) )
x = 2

if x %2 != 0:
    salida = "impar"
elif x ==0:
    salida = "cero es neutro, ni par ni impar"
else :
    salida = "par"


print (f"{salida=}")
print("*"*50)################################################

# ~ salida = "impar" if x %2 != 0 else "no es impar"
salida = "impar" if x %2 != 0 else \
                        ("cero es neutro, ni par ni impar" if x ==0 else "par") 

print (f"{salida=}")
print("*"*50)################################################

pausa()
limpiar()
print ("extencion".center (50) )


entradas = [9,5,1,7,4,6,3,2,8,0,1,5,9]
salidas =  []

for cada_entrada in entradas:
    if cada_entrada %2 != 0:
        cada_salida = "impar"
    elif cada_entrada ==0:
        cada_salida = "cero es neutro, ni par ni impar"
    else :
        cada_salida = "par"
    print (f"""
    {cada_entrada=}
    {cada_salida=}
    """)
    salidas.append(cada_salida)

print (f"""
    {list(zip( entradas, salidas))=}
    """)

print (f"{salida=}")
print("*"*50)################################################
print ("one line comprenhesion list".center (50) )

salidas = ["impar" if cada_entrada %2 != 0 else ("cero es neutro, ni par ni impar" if x ==0 else "par") for cada_entrada in entradas] 

print (f"""
    {list(zip( entradas, salidas))=}
    """)
print("*"*50)################################################
print ("one line comprenhesion dict".center (50) )

salidas = {cada_entrada : "impar" if cada_entrada %2 != 0 else ("cero es neutro, ni par ni impar" if x ==0 else "par") for cada_entrada in entradas}

print (f"""
    { salidas=}
    """)

salidas = {f"{cada_entrada}_index:{index}" : "impar" if cada_entrada %2 != 0 else ("cero es neutro, ni par ni impar" if x ==0 else "par") for index, cada_entrada in enumerate(entradas)}

print (f"""
    { salidas=}
    """)
print("*"*50)################################################
print ("one line comprenhesion dict".center (50) )

salidas = {cada_entrada : "impar" if cada_entrada %2 != 0 else ("cero es neutro, ni par ni impar" if x ==0 else "par") for cada_entrada in entradas}

print (f"""
    { salidas=}
    """)

salidas = {f"{cada_entrada}_index:{index}" : "impar" if cada_entrada %2 != 0 else ("cero es neutro, ni par ni impar" if x ==0 else "par") for index, cada_entrada in enumerate(entradas)}

print (f"""
    { salidas=}
    """)
    
    
    
print("*"*50)################################################
print ("one line comprenhesion generador".center (50) )

salidas = ("impar" if cada_entrada %2 != 0 else ("cero es neutro, ni par ni impar" if x ==0 else "par") for cada_entrada in entradas)
print (f"""
    { salidas=}
    { type(salidas)=}""")
    
    
print("*"*50)################################################
print ("one line comprenhesion tupla".center (50) )

salidas = tuple("impar" if cada_entrada %2 != 0 else ("cero es neutro, ni par ni impar" if x ==0 else "par") for cada_entrada in entradas)
print (f"""
    { salidas=}
    { type(salidas)=}
    
    """)
print("*"*50)################################################
print ("one line comprenhesion list ---------> like filter".center (50) )



filtro  = [f"impar:{cada_entrada}"  for cada_entrada in entradas if cada_entrada %2 != 0 ] 

print (f"""
    {filtro=}
    """)    
    
def filtro (cada_entrada):
    if cada_entrada %2 != 0:
        return f"impar:{cada_entrada}" 
    return


salidas = []
for cada_entrada in entradas:
    regreso =filtro (cada_entrada)
    if regreso is not None:
        salidas.append(regreso)
print (f"""
{salidas=}
""")   




pausa()
limpiar()
   
print("*"*50)################################################

salidas = lambda entradas: [f"impar:{cada_entrada}"  "impar" if cada_entrada %2 != 0 else ("cero es neutro, ni par ni impar" if x ==0 else "par") for cada_entrada in entradas]

# Llamar la lambda y mostrar la salida
resultados = salidas(entradas)
print (f"""
{resultados=}
# ~ """)     
 

pausa()
limpiar()
   
print("*"*50)################################################

salidas = lambda : [f"impar:{cada_entrada}"  "impar" if cada_entrada %2 != 0 else ("cero es neutro, ni par ni impar" if x ==0 else "par") for cada_entrada in entradas]

# Llamar la lambda y mostrar la salida
resultados = salidas()
print (f"""
{resultados=}
""")        
   
   
   
   
   
print("*"*50)################################################
salidas  = lambda entradas : [f"impar:{cada_entrada}"  for cada_entrada in entradas if cada_entrada %2 != 0 ] 

# Llamar la lambda y mostrar la salida
resultados = salidas(entradas)
print (f"""
{resultados=}
""")        


    

exit()






















exit()
#######################################################################################################
print ("*"*50)###########################################################################
entrada = 0
print ("extencion")
if entrada %2 !=0:
    salida = "impar"
elif entrada == 0:
    salida = "cero es neutos"
else:
    salida = "par"
print (f"""
{entrada=}
{salida=}
""")
# ~ print ("*"*50)###########################################################################
# ~ print ("ternario")
# ~ salida = "impar" if entrada %2 !=0 else "no impar"

# ~ print (f"""
# ~ {entrada=}
# ~ {salida=}
# ~ """)

print ("*"*50)###########################################################################
print ("ternario anidado")
salida = "impar" if entrada %2 !=0 else ("cero es neutos" if entrada == 0 else "par")

print (f"""
{entrada=}
{salida=}
""")

pausa()
limpiar()
print ("*"*50)###########################################################################
entradas = [9,5,1,7,4,6,3,2,8,0,1,5,9]
salidas =  []
print ("extencion")
for cada_entrada in entradas:
    if cada_entrada %2 !=0:
        cada_salida = "impar"
    elif cada_entrada == 0:
        cada_salida = "cero es neutos"
    else:
        cada_salida = "par"
        
    print (f"""
    {cada_entrada=}
    {cada_salida=}
    """)
    salidas.append(cada_salida)
    
print (f"""
{entradas=}
{salidas=}
""")    
pausa()
print ("*"*50)###########################################################################
entradas = [9,5,1,7,4,6,3,2,8,0,1,5,9]
print ("extencion")
salidas = []
for cada_entrada in entradas:
    cada_salida = "impar" if entrada %2 !=0 else ("cero es neutos" if entrada == 0 else "par")
    print (f"""
    {cada_entrada=}
    {cada_salida=}
    """)
    salidas.append(cada_salida)
    
print (f"""
{entradas=}
{salidas=}
""")    
pausa()
print ("*"*50)###########################################################################
entradas = [9,5,1,7,4,6,3,2,8,0,1,5,9]
print ("comprension - one line comprehension list")
salidas = ["impar" if entrada %2 !=0 else ("cero es neutos" if entrada == 0 else "par") for cada_entrada in entradas]
print (f"""
{entradas=}
{salidas=}
""")    

pausa()
print ("*"*50)###########################################################################
entradas = [9,5,1,7,4,6,3,2,8,0,1,5,9]
print ("comprension - one line comprehension dict")
salidas = {cada_entrada : "impar" if entrada %2 !=0 else ("cero es neutos" if entrada == 0 else "par") for cada_entrada in entradas}
print (f"""
{entradas=}
{salidas=}
""")    
pausa()
print ("*"*50)
###########################################################################
entradas = [9,5,1,7,4,6,3,2,8,0,1,5,9]
print ("comprension - one line comprehension dict")
salidas = {f"{cada_entrada}_index:{indice}" : "impar" if entrada %2 !=0 else ("cero es neutos" if entrada == 0 else "par") for indice,cada_entrada in enumerate(entradas)}
print (f"""
{entradas=}
{salidas=}
""")    

pausa()
print ("*"*50)###########################################################################
entradas = [9,5,1,7,4,6,3,2,8,0,1,5,9]
print ("comprension - one line comprehension generador")
salidas = ("impar" if entrada %2 !=0 else ("cero es neutos" if entrada == 0 else "par") for cada_entrada in entradas)
print (f"""
{entradas=}
{salidas=}
{type (salidas)}
""")  

print ("comprension - one line comprehension tuple")
salidas = tuple("impar" if entrada %2 !=0 else ("cero es neutos" if entrada == 0 else "par") for cada_entrada in entradas)
print (f"""
{entradas=}
{salidas=}
{type (salidas)}
""")  










exit()
import this
"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

"""








