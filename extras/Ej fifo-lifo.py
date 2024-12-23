

import json
import random
import os
try:
    from colorama import *
except Exception as error_:
    import pip
    pip.main(['install', 'colorama'])
    from colorama import *
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tPresione enter para continuar")
limpiar();
#################################################################
def ya_hechos():
    pass
# ~ 16) SEC_4) FIFO / LIFO  Las funciones FIFO y LIFO 

import random
#----------------------------------------------------------------------------
def FIFO_compra(ingresos, cantidad):
    semana = 1
    while cantidad > 0 and ingresos:
        mercaderia = ingresos.pop(0) 
        if cantidad >= mercaderia:
            cantidad -= mercaderia
            print(f"Comprando {mercaderia} unidades de mercadería de la semana {semana} (FIFO)")
        else:
            print(f"No hay suficiente mercadería en la semana {semana} (FIFO)")
            break
        semana += 1
#----------------------------------------------------------------------------
def LIFO_compra(ingresos, cantidad):
    semana = 1
    while cantidad > 0 and ingresos:
        mercaderia = ingresos.pop() 
        if cantidad >= mercaderia:
            cantidad -= mercaderia
            print(f"Comprando {mercaderia} unidades de mercadería de la semana {semana} (LIFO)")
        else:
            print(f"No hay suficiente mercadería en la semana {semana} (LIFO)")
            break
        semana += 1
#----------------------------------------------------------------------------
# Datos de ejemplo: ingresos de mercadería por semana
ingresos_semanales = [100, 150, 80, 200]

salida = ingresos_semanales.pop(0)
print (f"""
fifo{ingresos_semanales=}
{salida=}
""")
ingresos_semanales = [100, 150, 80, 200]
# ~ ultimo_lugar = len (ingresos_semanales)
# ~ indice_ultimo = ultimo_lugar-1
# ~ alida = ingresos_semanales.pop(indice_ultimo)
salida = ingresos_semanales.pop()
print (f"""
lifo{ingresos_semanales=}
{salida=}
""")
ingresos_semanales = [100, 150, 80, 200]




ingresos_semanales = [100, 150, 80, 200]



# Convertir la lista en una cola y una pila
cola_ingresos = ingresos_semanales.copy() 
pila_ingresos = ingresos_semanales.copy() 
# Simular compras utilizando LIFO
print("\nCompra utilizando LIFO:")
LIFO_compra(pila_ingresos, 400)
# Simular compras utilizando FIFO
print("Compra utilizando FIFO:")
FIFO_compra(cola_ingresos, 400)









