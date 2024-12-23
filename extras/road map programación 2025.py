import os

def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
    # ~ print("\033[H\033[J", end="")
from colorama import *
def pausa():
    input("\tPresione enter para continuar")
limpiar();
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
║                                                                             ║
║                                                                             ║
║  ╔═════╗   ╔╗       ╔╗   ╔═════╗    ╔╗      ╦                               ║
║ ╔╝     ╚╗   ║       ║   ╔╝     ╚╗   ║╚╗     ║                               ║
║ ║       ║   ╚╗     ╔╝   ║       ║   ║ ╚╗    ║                               ║
║ ║       ║    ║     ║    ║       ║   ║  ╚╗   ║                               ║
║ ╠═══════╣    ╚╗   ╔╝    ╠═══════╣   ║   ╚╗  ║  ╠═════╣                      ║
║ ║       ║     ║   ║     ║       ║   ║    ╚╗ ║                               ║
║ ║       ║     ╚╗ ╔╝     ║       ║   ║     ╚╗║                               ║
║ ╩       ╩      ╚═╝      ╩       ╩   ╩      ╚╝                               ║
║                                                                             ║
║                                                                             ║
║                             ╔═══════╗   ╔═════╗  ╔══════╗    ╔═════╗        ║
║                                    ╔╝  ╔╝     ╚╗ ║      ╚╗  ╔╝     ╚╗       ║
║                                   ╔╝   ║       ║ ║       ║  ║       ║       ║
║                                  ╔╝    ║       ║ ║       ║  ║       ║       ║
║                               ╔══╝     ╠═══════╣ ║       ║  ║       ║       ║
║                              ╔╝        ║       ║ ║       ║  ║       ║       ║
║                             ╔╝         ║       ║ ║      ╔╝  ╚╗     ╔╝       ║
║                             ╚═══════╝  ╩       ╩ ╚══════╝    ╚═════╝        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝''')
pausa()
limpiar()
init()
print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║    Modulos IT -  Programacion                                               ║
║        Constantes y variables, tipos de datos.                              ║
║        Operadores lógicos y matemáticos.                                    ║
║        Estructuras de toma de decisiones.                                   ║
║        Estructuras de repeticiones.                                         ║
║        Procedimientos y funciones.                                          ║
║        Listas, tuplas, diccionarios.                                        ║
║        Algoritmos y estructuras de datos.                                   ║
║        Bases de datos                                                       ║
║               Conexión - Cursor                                             ║
║                      BBDD                                                   ║
║                      Tablas                                                 ║
║                      Campos (tipos de datos)                                ║
║                      Registros                                              ║
║               CRUD - ABM                                                    ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣{Style.RESET_ALL}
╠═════════════════════════════════════════════════════════════════════════════╣
║                                                                             ║
║    Road map de clases con Ariel                                             ║
║        Programación Modulo 1 - presentación e instalacion                   ║
║        Programación Modulo 2 - t obj_1ros operadores                        ║
║        Programación Modulo 3 - m flujo - if                                 ║
║        Programación Modulo 4 - entradas de datos                            ║
║        Programación Modulo 5 - m flujo - while                              ║
║        Programación Modulo 6 - colecciones - m flujo - for                  ║
║                                          ingresar                           ║
║                                          eliminar                           ║
║                                          modificar                          ║
║        Programación Modulo 7 - random - ternarios - comprension             ║
║        Programación Modulo 8 - funciones propias                            ║
║                                          parametro    | entrada - salida    ║
║                                          argumento                          ║
║                                          recursividad                       ║
║                                                                             ║
║        Programación Modulo 9 - lambda - o_sup                               ║
║                                        map(funcion_accion simple, coleccion)║
║                                        filter(funcion_booleana, coleccion)  ║
║                                        reduce(funcion-2 parametros entrada  ║
║                                                       1 parametro de salida)║
║                                                                             ║
║        Programación Modulo 10 - externos with open(nombre archivo, mode     ║
║                                                rb             r read        ║
║                                                wb             w write       ║
║                                                ab             a append      ║
║                                                xb?            x crea vacio  ║
║                                          binario pickle     json            ║
║                                                                             ║
║        Programación Modulo 10 - try except basico                           ║
║        Programación Modulo 11 - web                                         ║
║                                     Requests                                ║
║                                                                             ║
║        Programación Modulo 12 - BBDD                                        ║
║                               Estructura de dados                           ║
║                                   Conexión - Cursor                         ║
║                                          BBDD                               ║
║                                          Tablas                             ║
║                                          Campos (tipos de datos)            ║
║                                          Registros                          ║
║                                   CRUD - ABM                                ║
║                                          insert                             ║
║                                          select                             ║
║                                          update                             ║
║                                          delete                             ║
║                                   filtros                                   ║
║                                          where                              ║
║                                          like                               ║
║                                                                             ║
║        Programación Modulo 13 - GUI                                         ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}''')
#######################################################################################################
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
    limpiar()
######################################################################################################


print(f"""
 ##################################################################################################################
 #                                                                                                                #
 #                                                 PYTHON                                                         #
 #                                                                                                                #
 #                                       Variables,listas,diccionarios                                            #
 #                                               Salida: Print                                                    #
 #                                               Entrada: Input                                                   #
 #                                        Flujo:                                                                  #
 #                                          Condicionales: if else elif                                           #
 #                                          Bucles:                                                               #
 #                                                 while                                                          #
 #                                                 for                                                            #
 #                                                                                                                #
 ##################################################################################################################
 #                                                                                                                #
 #                                                                                                                #
 #                                                MODULO 1                                                        #
 #                        Tipos de datos y colecciones                                                            #
 #                        Operadores                                                                              #
 #                        Sentencias de Control                                                                   #
 #                        Funciones Built-in                                                                      #
 #                        Funciones                                                                               #
 #                        Ámbito, valor y referencia                                                              #
 #                        Argumento de longitud variable                                                          #
 #                                                                                                                #
 ##################################################################################################################
 # Los conceptos fundamentales de la programación                                                                 #
 # Cómo instalar Python y Geany                                                                                   #
 # Cuál es la estructura de un programa                                                                           #
 # Qué tipos de programas hay                                                                                     #
 # Cómo ejecutar un programa de Python                                                                            #
 # Cómo crear un programa básico de Python                                                                        #
 # Los conceptos de expresión y variable                                                                          #
 # Cómo utilizar la consola interactiva                                                                           #
 # Cómo utilizar la terminal                                                                                      #
 # Distinguir entre programación, lenguaje de programación, código, aplicación e intérprete y sus conceptos       #
 # Manejar Geany   - Visual Studio code                                                                           #
 # Ejecutar archivos de Python                                                                                    #
 # Utilizar la consola interactiva                                                                                #
 # Diseñar expresiones y definir variables                                                                        #
 # Crear un pequeño programa en Python                                                                            #
 # Manejar la terminal                                                                                            #
 # Qué es un tipo de dato                                                                                         #
 # Cuáles son los tipos de dato básicos                                                                           #
 # Operaciones aritméticas y lógicas                                                                              #
 # Comparaciones entre variables y expresiones                                                                    #
 # Condicionales                                                                                                  #
 # Comentarios                                                                                                    #
 # Cómo ingresar datos a través de la consola                                                                     #
 # Crear variables de distintos tipos de dato                                                                     #
 # Ejecutar operaciones aritméticas sobre números enteros                                                         #
 # Realizar comparaciones simples y complejas                                                                     #
 # Dirigir el flujo de un programa                                                                                #
 # Solicitar datos al usuario                                                                                     #
 # El concepto de lista                                                                                           #
 #                              coleccion de elementos separados por comas []                                     #
 # Cómo añadir e insertar elementos en una lista                                                                  #
 #                              insert/append                                                                     #
 # Cómo simular matrices                                                                                          #
 #                              []    [ [ ] , [ ] ]                                                               #
 ##################################################################################################################""")
pausa()
print(f"""
 ##################################################################################################################
 #                                                                                                                #
 #                                               REPASO PYTHON                                                    #
 #                                                                                                                #
 #                                                Colecciones                                                     #
 #                                                                                                                #
 #                                               Programming II                                                   #
 #                                                                                                                #
 ##################################################################################################################
 # El concepto y los distintos tipos de bucles y cómo implementarlos        while ~for /range                     #
 # Conversiones entre tipos de dato                      str , int, float                                         #
 # Crear listas y matrices                                                                                        #
 # Añadir elementos al final de una lista o insertarlos en una posición arbitraria                                #
 # Calcular el número de elementos de una lista                                                                   #
 # Repetir la ejecución de un bloque de código vía bucles                                                         #
 # Convertir números enteros a cadena                                                                             #
 # Convertir cadenas a números enteros                                                                            #
 # Introducción al Paradigma de Objetos                                                                           #
 # Qué es y cómo implementar una función                                                                          #
 # Definir funciones con argumentos                                                                               #
 # Establecer un valor de retorno para las funciones                                                              #
 # Qué es y cómo crear un diccionario                                                                             #
 # Operaciones de entrada y salida para diccionarios                                                              #
 # Crear tus propias funciones                                                                                    #
 # Organizar mejor el código y evitar su repetición                                                               #
 # Identificar las funciones incorporadas del lenguaje                                                            #
 # Crear tus propios diccionarios                                                                                 #
 # Agregar y modificar elementos de un diccionario                                                                #
 ##################################################################################################################""")
pausa()
print(f"""
 ##################################################################################################################
 #                                                                                                                #
 #                                                 PYTHON                                                         #
 #                                                                                                                #
 #                                                 Funciones                                                      #
 #                                                                                                                #
 #                                               Programming III                                                  #
 #                                                                                                                #
 ##################################################################################################################
 #                                                                                                                #
 #                                                                                                                #
 #                                                MODULO 2                                                        #
 #                         Funciones de orden superior y anónimas                                                 #
 #                         Capturar y lanzar excepciones                                                          #
 #                         Características y Operaciones sobre Cadenas de Caracteres                              #
 #                         Entrada y salida , archivos                                                            #
 #                         Módulos y paquetes                                                                     #
 #                                                                                                                #
 ##################################################################################################################
 # funciones                                                                                                      #
 # parametros/argumentos de entrada                                                                               #
 # return salida y salida multiples                                                                               #
 # recursividad                                                                                                   #
 # funciones de funciones                                                                                         #
 # lambda                                                                                                         #
 # map                                                                                                            #
 # filter                                                                                                         #
 # string                                                                                                         #
 # dir(str())                                                                                                     #
 # modulos propios                                                                                                #
 # Archivos externos : Lectura, escritura, append                                                                 #
 # Archivos  txt                                                                                                  #
 #           json                                                                                                 #
 #           xls/xlsm/xlsx      openpyxl                                                                          #
 #           pickle                                                                                               #
 #                                                                                                                #
 ##################################################################################################################""")
pausa()
print(f"""
 ##################################################################################################################
 #                                                                                                                #
 #                                                 PYTHON                                                         #
 #                                                                                                                #
 #                                      Programacion Orientada a Objetos                                          #
 #                                                                                                                #
 #                                               Programming IV                                                   #
 #                                                                                                                #
 ##################################################################################################################
 #                                                                                                                #
 #                                                                                                                #
 #                                                MODULO 3                                                        #
 #                         Clases y objetos                                                                       #
 #                         Encapsulamiento, herencia y polimorfismo                                               #
 #                                                                                                                #
 ##################################################################################################################
 # class                                                                                                          #
 # __init__                                                                                                       #
 # self                                                                                                           #
 # Atributos                                                                                                      #
 # métodos                                                                                                        #
 # Encapsulamiento                                                                                                #
 # Herencia                                                                                                       #
 # Herencias múltiples                                                                                            #
 # Polimorfismo                                                                                                   #
 #                                                                                                                #
 ##################################################################################################################""")
pausa()
print(f"""
 ##################################################################################################################
 #                                                                                                                #
 #                                                 PYTHON                                                         #
 #                                                                                                                #
 #                                      Programacion Orientada a Objetos                                          #
 #                                                                                                                #
 #                                               Programming V                                                    #
 #                                                                                                                #
 ##################################################################################################################
 #                                                                                                                #
 #                                                                                                                #
 #                                                MODULO 3                                                        #
 #                         Instalar módulos de terceros                                                           #
 #                         Scripting                                                                              #
 #                         Argumentos de programa                                                                 #
 #                         Sistema de archivos                                                                    #
 #                         Ejecución de comandos                                                                  #
 #                                                                                                                #
 ##################################################################################################################
 # importar modulos                                                                                               #
 # pip                                                                                                            #
 # import modulo                                                                                                  #
 # import modulo as alias                                                                                         #
 # form modulo import *                                                                                           #
 # form modulo import clase / funcion                                                                             #
 #   datetime                                                                                                     #
 #   os                                                                                                           #
 #   system                                                                                                       #
 #   psutil                                                                                                       #
 #   tabulate                                                                                                     #
 #   prettytable                                                                                                  #
 #   pprint                                                                                                       #
 #   math                                                                                                         #
 #                                                                                                                #
 ##################################################################################################################""")
pausa()
print(f"""
 ##################################################################################################################
 #                                                                                                                #
 #                                                 PYTHON                                                         #
 #                                                                                                                #
 #                                             Bases de Datos                                                     #
 #                                                                                                                #
 #                                             Programming VI                                                     #
 #                                                                                                                #
 ##################################################################################################################
 #                                                                                                                #
 #                                                                                                                #
 #                                                MODULO 4                                                        #
 #                         SQLite                                                                                 #
 #                              instalación                                                                       #
 #                              dbBrowser                                                                         #
 #                              Archivos db                                                                       #
 #                              C.R.U.D.                                                                          #
 #                                    base de datos crear borrar   (mediantemanejo de archivos)                   #
 #                                    tablas crear borrar modificar                                               #
 #                                    rows crear borrar modificar                                                 #
 #                                    datos/filas insertar borrar modificar                                       #
 #                                                                                                                #
 #                                                                                                                #
 #                                                                                                                #
 ##################################################################################################################
 # SQLite                                                                                                         #
 #        instalación y conectores  sqlite3                                                                       #
 #                                                                                                                #
 #      create table                                                                                              #
 #      drop table                                                                                                #
 #      alter table                                                                                               #
 #      insert into                                                                                               #
 #      delete                                                                                                    #
 #      update                                                                                                    #
 #      select                                                                                                    #
 #          where                                                                                                 #
 #      fetchall/many/one                                                                                         #
 #                                                                                                                #
 # CRUD                                                                                                           #
 #                                                                                                                #
 # Inyección de código SQL y cómo prevenirla.                                                                     #
 #                                                                                                                #
 ##################################################################################################################""")
pausa()
print(f"""
 ##################################################################################################################
 #                                                                                                                #
 #                                                 PYTHON                                                         #
 #                                                                                                                #
 #                                             Bases de Datos                                                     #
 #                                                                                                                #
 #                                             Programming VII                                                    #
 #                                                                                                                #
 ##################################################################################################################
 #                                                                                                                #
 #                                                                                                                #
 #                                                MODULO 4                                                        #
 #                                                                                                                #
 #                         MySQL                                                                                  #
 #                              instalación                                                                       #
 #                              workbench - xampp /lampp/mampp                                                    #
 #                              Servidores                                                                        #
 #                              Puertos (3306)                                                                    #
 #                              C.R.U.D.                                                                          #
 #                                    base de datos crear borrar                                                  #
 #                                    tablas crear borrar modificar                                               #
 #                                    rows crear borrar modificar                                                 #
 #                                    datos/filas insertar borrar modificar                                       #
 #                                                                                                                #
 #                                                                                                                #
 ##################################################################################################################
 # MySQL                                                                                                          #
 #        instalación y conectores  mysql.connector mysql pymysql sqlalchemy                                      #
 #                                                                                                                #
 #      create database                                                                                           #
 #      drop  database                                                                                            #
 #      create table                                                                                              #
 #      drop table                                                                                                #
 #      alter table                                                                                               #
 #      insert into                                                                                               #
 #      delete                                                                                                    #
 #      update                                                                                                    #
 #      select                                                                                                    #
 #          where                                                                                                 #
 #      fetchall/many/one                                                                                         #
 #                                                                                                                #
 # CRUD                                                                                                           #
 #                                                                                                                #
 # Inyección de código SQL y cómo prevenirla.                                                                     #
 #                                                                                                                #
 ##################################################################################################################""")
pausa()
print(f"""
 ##################################################################################################################
 #                                                                                                                #
 #                                                 PYTHON                                                         #
 #                                                                                                                #
 #                                                  HTML                                                          #
 #                                                                                                                #
 #                                            Programming VIII                                                    #
 #                                                                                                                #
 ##################################################################################################################
 #                                                                                                                #
 #                                                                                                                #
 #                                                MODULO 5                                                        #
 #                                                                                                                #
 #   Qué es un servicio web.                                                                                      #
 #   El protocolo HTTP.                                                                                           #
 #   La arquitectura REST.                                                                                        #
 #   La librería Requests.                                                                                        #
 #   Interacción con un servicio web desde Python.                                                                #
 #   Automatizar el envío de un formulario web.                                                                   #
 #                                                                                                                #
 ##################################################################################################################
 #                                                                                                                #
 #   import requests                                                                                              #
 #                                                                                                                #
 #   requests.get(url)                                                                                            #
 #   res.json()                                                                                                   #
 #   token                                                                                                        #
 #   endpoint                                                                                                     #
 #                                                                                                                #
 #                                                                                                                #
 #                   requests sobre localhost.py                                                                  #
 #                                                                                                                #
 #                método HTTP     Descripción                                                                     #
 #                ● GET      Recuperar un recurso existente.                                                      #
 #                ● POST     Crear un nuevo recurso.                                                              #
 #                ● PUT      Actualizar un recurso existente.                                                     #
 #                ● DELETE   Eliminar un recurso.                                                                 #
 #                ● PATCH    Actualizar parcialmente un recurso existente.                                        #
 #                                                                                                                #
 #                                                                                                                #
 #   FLASK                                                                                                        #
 #         from flask import Flask                                                                                #
 #                                    render_template                                                             #
 #                                    jsonify                                                                     #
 #                                    redirect                                                                    #
 #                                    url_for                                                                     #
 #                                    request                                                                     #
 #                                                                                                                #
 #                                                                                                                #
 ##################################################################################################################""")
pausa()
print(f"""
 ##################################################################################################################
 #                                                                                                                #
 #                                                 PYTHON                                                         #
 #                                                                                                                #
 #                                                  API                                                           #
 #                                                                                                                #
 #                                             Programming IX                                                     #
 #                                                                                                                #
 ##################################################################################################################
 #                                                                                                                #
 #                                                                                                                #
 #                                                MODULO 6                                                        #
 #                                                                                                                #
 #     Desarrollo avanzado con Tcl/Tk vía el módulo “tkinter”.                                                    #
 #     Botones, Cajas de texto, Etiquetas.                                                                        #
 #     Menús.                                                                                                     #
 #     Listas.                                                                                                    #
 #     Convertir un script de Python a un archivo ejecutable.                                                     #
 #     Entornos Virtuales                                                                                         #
 #                                                                                                                #
 #                                                                                                                #
 ##################################################################################################################
 # import tkinter as tk                                                                                           #
 # from tkinter import tk                                                                                         #
 # tkinter, ttk                                                                                                   #
 # tkinter, ttk                                                                                                   #
 #  objeto = Tk.tk() instanciacion de objetos de clases importadas                                                #
 #  Frame(ws)                                                                                                     #
 #      pack()                                                                                                    #
 #      grid()                                                                                                    #
 #      place()                                                                                                   #
 #   x , y                                                                                                        #
 #   width , height                                                                                               #
 #  .config                                                                                                       #
 #  .label                                                                                                        #
 #  .button                                                                                                       #
 #  .entry                                                                                                        #
 #  .title                                                                                                        #
 #  .geometry                                                                                                     #
 #  .Treeview                                                                                                     #
 #                                                                                                                #
 #  .get                                                                                                          #
 #  .set                                                                                                          #
 #                                                                                                                #
 ##################################################################################################################""")
pausa()

