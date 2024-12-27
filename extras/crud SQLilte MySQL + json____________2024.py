####################################################################################################
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
    limpiar()
from colorama import *
####################################################################################################
limpiar()
from datetime import datetime, date, time
import math
import datetime
import json
import openpyxl
import random
########################################################################
def leer_json(archivo="instalador_2024"):
    with open(f"{archivo}.json" ,"r") as objeto_json:
        diccionario_salida = json.load(objeto_json)
    return diccionario_salida
########################################################################

def grabar_json (archivo="instalador_2024",**diccionario_entrada):
    with open(f"{archivo}.json", mode="w",encoding='utf-8') as obj_json:
        json.dump(diccionario_entrada, obj_json, ensure_ascii=False, indent=4 )
        print ("exito")
########################################################################

####################################################################################################
####################################################################################################
#                                                                                                  #
#                                        Bases de datos                                            #
#                                                                                                  #
####################################################################################################

print(F'''{Fore.WHITE+ Style.BRIGHT + Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║              ╦     ╔═════╗     ╔═══╦═══╗   ╔═══════╗     ╔═════╗            ║
║              ║    ╔╝     ╚╗        ║       ║            ╔╝     ╚╗           ║
║              ║    ║                ║       ║            ║       ║           ║
║              ║    ╚╗               ║       ║            ║       ║           ║
║              ║     ╚═════╗         ║       ╠══════╣     ╠═══════╣           ║
║              ║           ╚╗        ║       ║            ║       ║           ║
║              ║    ╚╗     ╔╝        ║       ║            ║       ║           ║
║              ╩     ╚═════╝         ╩       ╚═══════╝    ╩       ╩           ║
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
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
https://www.sqlite.org/2024/sqlite-dll-win-x64-3460100.zip
https://www.sqlite.org/2024/sqlite-tools-win-x64-3460100.zip
https://download.sqlitebrowser.org/DB.Browser.for.SQLite-v3.13.0-win64.msi

''')
pausa()
limpiar()
import datetime
hoy = datetime.date.today()
print(hoy)


# ~ grabar_json(**diccionario_instalacion)
diccionario_instalacion= leer_json()


base_de_datos=""
while base_de_datos not in ["S","M"]:
    base_de_datos = input("Seleccione entre:\n\tM) para MySQL\n\tS) para SQLite""").upper()

match (base_de_datos):
    case "S":
        print("""\033[1;37;44m\n
        ╔═════════════════════════════════════════════════════════════════════════════╗
        ║                                                                             ║
        ║      ╔═════╗       ╔═════╗       ╦           ╦   ╔═══╦═══╗   ╔═══════╗      ║
        ║     ╔╝     ╚╗     ╔╝     ╚╗      ║           ║       ║       ║              ║
        ║     ║       ║     ║       ║      ║           ║       ║       ║              ║
        ║     ╚╗            ║       ║      ║           ║       ║       ║              ║
        ║      ╚══════╗     ║       ║      ║           ║       ║       ╠═════╣        ║
        ║             ║     ║       ║      ║           ║       ║       ║              ║
        ║     ╚╗     ╔╝     ╚╗    ╔╦╝      ║           ║       ║       ║              ║
        ║      ╚═════╝       ╚════╝╚═╝     ╚═══════╝   ╩       ╩       ╚═══════╝      ║
        ║                                                                             ║
        ╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
        """);
        import sqlite3
    case "M":

        ####################################################################################################
        print("""\033[1;37;44m\n
        ╔═════════════════════════════════════════════════════════════════════════════╗
        ║                                                                             ║
        ║     ╔╗      ╔╗     ╦       ╦      ╔═════╗       ╔═════╗       ╦             ║
        ║     ║╚╗    ╔╝║     ╚╗     ╔╝     ╔╝     ╚╗     ╔╝     ╚╗      ║             ║
        ║     ║ ╚╗  ╔╝ ║      ╚╗   ╔╝      ║       ║     ║       ║      ║             ║
        ║     ║  ╚╗╔╝  ║       ╚╗ ╔╝       ╚╗            ║       ║      ║             ║
        ║     ║   ╚╝   ║        ╚╦╝         ╚══════╗     ║       ║      ║             ║
        ║     ║        ║         ║                 ║     ║       ║      ║             ║
        ║     ║        ║         ║         ╚╗     ╔╝     ╚╗    ╔╦╝      ║             ║
        ║     ╩        ╩         ╩          ╚═════╝       ╚════╝╚═╝     ╚═══════╝     ║
        ║                                                                             ║
        ╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
        """);
        try:
            import mysql.connector
        except Exception as error_:
            import pip
            pip.main(['install', 'mysql-connector-python'])
        from mysql.connector import Error
        from mysql.connector import errorcode
        from mysql.connector import IntegrityError
print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                                                                             ║
║              Conexión al server SQLite                                      ║
║              Conexión a la base de datos                                    ║
║              Conexión a la coleccion                                        ║
║              CRUD (Create-Read-Update-Delete) en SQLite                     ║
║                              Create Database                                ║
║                              Create Table                                   ║
║                              Insert                                         ║
║                              Select                                         ║
║                              Where                                          ║
║                              Where col like '%xx%'                          ║
║                              Order By     ASC DESC                          ║
║                              Delete                                         ║
║                              Drop Table                                     ║
║                              Update                                         ║
║                              Limit                                          ║
║                              Join                                           ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0;m
""");
pausa()


######################################################################################################
def conectar_base_de_datos():
    global connection
    if base_de_datos == "S":#   SQLite
        connection = sqlite3.connect(f'{diccionario_instalacion ["base_de_datos"]}.db')
    else:#                      MySQL
        
        connection = mysql.connector.connect(**diccionario_instalacion ["conexion"] )
        print (f"""mysql.connector.connect(
                    host= {diccionario_instalacion ["conexion"]["host"]},
                    user= {diccionario_instalacion ["conexion"]["user"]} ,
                    passwd= {diccionario_instalacion ["conexion"]["passwd"]})""")
        try:
            query = f"USE {diccionario_instalacion ['base_de_datos']}"
            cursor=connection.cursor()
            resultado =cursor.execute   (query)
            print (f"conectamos o cambiamos a la base de datos {query} ")
            print (f"desde sql {resultado}")
        except:
            print("método 'use' aun no disponible")
    return connection.cursor()

######################################################################################################
def crear_base():
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║       ╔═════╗    ╔══════╗   ╔═══════╗   ╔═════╗   ╔═══╦═══╗   ╔═══════╗     ║
║      ╔╝     ╚╗   ║      ╚╗  ║          ╔╝     ╚╗      ║       ║             ║
║      ║           ║       ║  ║          ║       ║      ║       ║             ║
║      ║           ║      ╔╝  ║          ║       ║      ║       ║             ║
║      ║           ╠════╦═╝   ╠═════╣    ╠═══════╣      ║       ╠═════╣       ║
║      ║           ║    ╚╗    ║          ║       ║      ║       ║             ║
║      ╚╗     ╔╝   ║     ╚╗   ║          ║       ║      ║       ║             ║
║       ╚═════╝    ╩      ╚╝  ╚═══════╝  ╩       ╩      ╩       ╚═══════╝     ║
║                                  (crear)                                    ║
║                                                                             ║
║                   creamos la base de datos si no existe                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
""")

    cursor = conectar_base_de_datos()#           sqlite // mysql
    if base_de_datos == "S":#   SQLite
        print               ("se crea en un archivo al generar la conexion")
    else:#                      MySQL

        query = f"CREATE DATABASE IF NOT EXISTS {diccionario_instalacion ['base_de_datos']}"
        print               (query)
        cursor.execute      (query)
        cursor.close
        connection.close
    cursor.close
    connection.close

    pausa()
######################################################################################################
def crear_tablas():
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║       ╔═════╗    ╔══════╗   ╔═══════╗   ╔═════╗   ╔═══╦═══╗   ╔═══════╗     ║
║      ╔╝     ╚╗   ║      ╚╗  ║          ╔╝     ╚╗      ║       ║             ║
║      ║           ║       ║  ║          ║       ║      ║       ║             ║
║      ║           ║      ╔╝  ║          ║       ║      ║       ║             ║
║      ║           ╠════╦═╝   ╠═════╣    ╠═══════╣      ║       ╠═════╣       ║
║      ║           ║    ╚╗    ║          ║       ║      ║       ║             ║
║      ╚╗     ╔╝   ║     ╚╗   ║          ║       ║      ║       ║             ║
║       ╚═════╝    ╩      ╚╝  ╚═══════╝  ╩       ╩      ╩       ╚═══════╝     ║
║                                  (crear)                                    ║
║                      creamos las tablas y columnas                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    print ("Conectamos con SQLite")
    ######################################################################################################

    print ("CREATE TABLE")
    print ("CREATE COLUMN")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    for cada_tabla in diccionario_instalacion ["tablas"]:
        columnas = ""
        for clave, valor in  diccionario_instalacion['tablas'][cada_tabla].items():
            columnas += f""" {clave} { valor}"""
        if base_de_datos == "M":
             columnas = columnas.replace("INTEGER", "INT").replace("AUTOINCREMENT", "AUTO_INCREMENT").replace("?", "%s")
        print (f"{columnas=}")
        query= (f"""CREATE TABLE IF NOT EXISTS {cada_tabla} ({columnas}  );""")
        print (f"{query=}")
        """
                    SQLite                                      (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    MySQL                                       (id INT     PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                                                      ^                     ^
                                                                      |_ INT x INTEGER      |_AUTOINCREMENT x AUTO_INCREMENT
        """
        cursor.execute      (query)
        
    cursor.close
    connection.close
    pausa()

######################################################################################################
def insertar_datos():
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║      ╦    ╦ ╔═══╗      ╔═════╗     ╔═══════╗    ╔══════╗    ╔═══╦═══╗       ║
║      ║    ╠═╝   ╚═╗   ╔╝     ╚╗    ║            ║      ╚╗       ║           ║
║      ║    ║       ║   ║            ║            ║       ║       ║           ║
║      ║    ║       ║   ╚╗           ║            ║      ╔╝       ║           ║
║      ║    ║       ║    ╚══════╗    ╠═════╣      ╠════╦═╝        ║           ║
║      ║    ║       ║           ║    ║            ║    ╚╗         ║           ║
║      ║    ║       ║   ╚╗     ╔╝    ║            ║     ╚╗        ║           ║
║      ╩    ╩       ╩    ╚═════╝     ╚═══════╝    ╩      ╚╝       ╩           ║
║                                  (insertar)                                 ║
║                                                                             ║
║                      insertamos un dato directamente                        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    print ("Conectamos con SQLite")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    ######################################################################################################
    print("""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de listas 1 a 1  ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)


    try:
       
        nombre_tabla_productos = list(diccionario_instalacion['tablas'].keys())[0]
        query = f"""INSERT INTO  {nombre_tabla_productos}  (descripcion, precio, codigo, vencimiento) 
                    VALUES('Galletitas', 222 , 'Titas','2025-01-01')"""
        print               (query)
        cursor.execute      (query)
        
        connection.commit()
        pausa()
        limpiar()
        
        query = f"""INSERT INTO  {nombre_tabla_productos}  (descripcion, precio, codigo, vencimiento) 
                    VALUES( ?, ?, ?, ?)"""
        if base_de_datos == "M":
            query = query.replace("?", "%s")
            
        print   (f'columnas_SQLite = ',query)
        proy= ( ("Chocolates",   99 , "A1",     '2025-06-15'),
                ("Fideos",      300 , "B1",     '2025-06-15'),
                ("Arroz",       250 , "C1",     '2025-08-15'),
                ("Agua",        200 , "D1",     '2025-09-15'),
                ("Tomates",     105 , "E1",     '2025-02-15'),
                ("Sal",         100 , "F1",     '2025-10-15'),
                ("Cacao",       300 , "G1",     '2025-11-15'),
                ("Gelatina",    205 , "H1",     '2025-12-15'),
                ("Flan",        200 , "I1",     '2024-01-15'))
        for datos in proy:
            cursor.execute(query,datos)
        connection.commit()# <-------------------------------------------------destabular
        print(cursor.rowcount, "record inserted.")

        limpiar()
        print("""\033[1;37;44m\n
        ╔═════════════════════════════════════════════════════════════════════════════╗
        ║                                                                             ║
        ║                      insertamos varios dato por intermedio de lista directa ║
        ║                                                                             ║
        ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
        """)

        proy = [
                ("Peras",       15 , "A2",      '2025-07-15'),
                ("Salsa tomate",10 , "B2",      '2024-02-15'),
                ("Pan",         30 , "C2",      '2024-01-15'),
                ("Kiwi",        25 , "K2",      '2024-04-15'),
                ("Cola 2l",     20 , "L2",      '2025-07-15'),
                ("Ajies",       15 , "M2",      '2024-02-15'),
                ("Pimienta",    10 , "N2",      '2024-01-15'),
                ("Cafe",        30 , "O2",      '2024-04-15'),
                ("Yerba",       25 , "P2",      '2025-07-15'),
                ("Te",          20 , "Q2",      '2024-02-25'),
                ("Pan",         15 , "R2",      '2024-01-15'),
                ("Queso",       10 , "S2",      '2024-02-15')
                ]
        #cursor.execute(query,datos)
        cursor.executemany(query,proy)
        connection.commit()
        print(cursor.rowcount, "record inserted in pool.")
        ###################################################################################################
        pausa()
        limpiar()
        

    except IntegrityError as error:
        # Verifica si es un error de entrada duplicada
        if error.errno == 1062:  # Código 1062 indica error de clave duplicada
            print("Advertencia: Entrada duplicada, se omite la inserción.")
        else:
            # Para otros tipos de errores de integridad, relanza el error
            raise
    pausa()
######################################################################################################
def leer_tabla():
    pausa()
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                  ╔══════╗   ╔═══════╗   ╔═════╗   ╔══════╗                  ║
║                  ║      ╚╗  ║          ╔╝     ╚╗  ║      ╚╗                 ║
║                  ║       ║  ║          ║       ║  ║       ║                 ║
║                  ║      ╔╝  ║          ║       ║  ║       ║                 ║
║                  ╠════╦═╝   ╠═════╣    ╠═══════╣  ║       ║                 ║
║                  ║    ╚╗    ║          ║       ║  ║       ║                 ║
║                  ║     ╚╗   ║          ║       ║  ║      ╔╝                 ║
║                  ╩      ╚╝  ╚═══════╝  ╩       ╩  ╚══════╝                  ║
║                                   (leer)                                    ║
║                                                                             ║
║                      leemos todos los datos de Mi_Tabla                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    cursor = conectar_base_de_datos()#           sqlite // mysql
    cursor.execute(f"SELECT * FROM  { list(diccionario_instalacion['tablas'].keys())[0]} ") 
    #print (cursor,type(cursor), dir (cursor))
    for linea in cursor:
        print (linea)
    pausa()
    '''
    -- WHERE `vencimiento` >= '2025-01-01' AND  `vencimiento` <= '2025-01-01';
    -- WHERE `vencimiento` >= '2024-01-01' OR  `vencimiento` <= '2025-01-01';
    -- WHERE NOT (`vencimiento` >= '2024-01-01' OR  `vencimiento` <= '2025-01-01');
    -- WHERE codigo IN ('H2O','S1','A1');
    -- WHERE precio BETWEEN 10 AND  100;
    -- WHERE precio BETWEEN 10 AND  100;
    -- WHERE descripcion like 'A%';
    -- WHERE descripcion like '%r%';-- #                    % cualquier cantidad de caracteres
    -- WHERE descripcion like 'A___z';-- #Arroz             _ un solo caracter
    -- WHERE descripcion REGEXP  '^A';-- #                  REGULAR EXPRESION ^inicio, fin^, | or, [caracteres] entres estos , [a-h] entre a y h
    -- WHERE descripcion IS NULL;
    -- WHERE descripcion IS NOT NULL;
    '''
    # ~ cursor.execute("SELECT * FROM  {nombre_tabla_productos} ")
    # ~ cursor.execute("SELECT * FROM  {nombre_tabla_productos} WHERE precio BETWEEN 10 AND  100; ")
    # ~ cursor.execute("SELECT * FROM  {nombre_tabla_productos} WHERE codigo IN ('H2O','S1','A1'); ")
    cursor.execute(F"SELECT * FROM  { list(diccionario_instalacion['tablas'].keys())[0]} WHERE descripcion like 'A%'; ")


    prod = cursor
    for linea in prod:
        print (f"filtrados {linea}")
    pausa()
    limpiar()
    cursor.close
    connection.close
######################################################################################################
def actualizar_datos():
    limpiar()
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║     ╦       ╦   ╔══════╗   ╔══════╗      ╔═════╗   ╔═══╦═══╗   ╔═══════╗    ║
║     ║       ║   ║      ╚╗  ║      ╚╗    ╔╝     ╚╗      ║       ║            ║
║     ║       ║   ║       ║  ║       ║    ║       ║      ║       ║            ║
║     ║       ║   ║      ╔╝  ║       ║    ║       ║      ║       ║            ║
║     ║       ║   ╠══════╝   ║       ║    ╠═══════╣      ║       ╠═════╣      ║
║     ║       ║   ║          ║       ║    ║       ║      ║       ║            ║
║     ╚╗     ╔╝   ║          ║      ╔╝    ║       ║      ║       ║            ║
║      ╚═════╝    ╩          ╚══════╝     ╩       ╩      ╩       ╚═══════╝    ║
║                                (actualizar)                                 ║
║                                                                             ║
║                      Actualizamos datos de la Base/tabla                    ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    cursor = conectar_base_de_datos()#           sqlite // mysql
    query = f"UPDATE {nombre_tabla_productos} SET {nombre_columna_3} = 'T_lta' WHERE {nombre_columna_1} = 'Tomates' "
    print (query)
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()

######################################################################################################
def borrar_datos():
    limpiar()
    print(f"""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║     ╔══════╗    ╔═══════╗   ╦           ╔═══════╗  ╔═══╦═══╗   ╔═══════╗    ║
    ║     ║      ╚╗   ║           ║           ║              ║       ║            ║
    ║     ║       ║   ║           ║           ║              ║       ║            ║
    ║     ║       ║   ║           ║           ║              ║       ║            ║
    ║     ║       ║   ╠═════╣     ║           ╠═════╣        ║       ╠═════╣      ║
    ║     ║       ║   ║           ║           ║              ║       ║            ║
    ║     ║      ╔╝   ║           ║           ║              ║       ║            ║
    ║     ╚══════╝    ╚═══════╝   ╚═══════╝   ╚═══════╝      ╩       ╚═══════╝    ║
    ║                                  (eliminar)                                 ║
    ║                                                                             ║
    ║                         borramos datos de la base                           ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    cursor = conectar_base_de_datos()#           sqlite // mysql
    

    query = f"DELETE FROM {nombre_tabla_productos}  WHERE {nombre_columna_1} = 'Sal'"# and {columna2} = '{dato2}'
    
    print           (query )
    cursor.execute  (query )
    print(cursor.rowcount, "record(s) affected")
    query = f"DELETE FROM {nombre_tabla_productos}  WHERE {nombre_columna_1} = "
    if base_de_datos == "S":#   SQLite
        query +=  " ? ;"
    else:#                      MySQL
        query +=  "%s ;"
    """
SQLite         ?  ; "
MySQL          %s ; "
    """

    proy = ("te", ) # VA una coma para generar una lista
    cursor.execute(query , proy)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()

######################################################################################################
def borrar_tablas():
    limpiar()
    cursor = conectar_base_de_datos()#           sqlite // mysql

    print("""\033[1;37;44m\n
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                         borramos la tabla de la base                        ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    
    nombre_tabla_productos=  list(diccionario_instalacion['tablas'].keys())[0]
    try:
        query= f"DROP TABLE IF EXISTS {nombre_tabla_productos};"
        print                           (query)
        resultado=cursor.execute        (query)
        print ("cursor.execute:",resultado)
        print(cursor.rowcount, "record(s) affected")
        print (f"tabla  {nombre_tabla_productos} eliminada ")
    except Exception as Error:
        print (f"tabla  {nombre_tabla_productos} no se pudo eliminar por la excepcion:\n {Error} ")
    pausa()
######################################################################################################
def borrar_base():
    limpiar()
    cursor = conectar_base_de_datos()#           sqlite // mysql
    print(f"""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                  ╔══════╗  ╔══════╗    ╔═════╗   ╔══════╗                   ║
║                  ║      ╚╗ ║      ╚╗  ╔╝     ╚╗  ║      ╚╗                  ║
║                  ║       ║ ║       ║  ║       ║  ║       ║                  ║
║                  ║       ║ ║      ╔╝  ║       ║  ║      ╔╝                  ║
║                  ║       ║ ╠════╦═╝   ║       ║  ╠══════╝                   ║
║                  ║       ║ ║    ╚╗    ║       ║  ║                          ║
║                  ║      ╔╝ ║     ╚╗   ╚╗     ╔╝  ║                          ║
║                  ╚══════╝  ╩      ╚╝   ╚═════╝   ╩                          ║
║                                  (borrar)                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    nombre_DDBB=  diccionario_instalacion['base_de_datos']
    nombre_tabla_productos=  list(diccionario_instalacion['tablas'].keys())[0]
    """
SQLite        no puede eliminarse desde dentro "
MySQL         se elimina con drop "
    """
    if base_de_datos == "S":#   SQLite
        print ("borramos base por archivos")
        try:
            os.remove(f'{nombre_DDBB}')
        except:
            print("el archivo esta abierto o no existe")
    else:#                      MySQL
        print ("borramos base por puerto 3306")
        try:

            limpiar()
            cursor = conectar_base_de_datos()#           sqlite // mysql
            cursor.execute(f"DROP DATABASE IF EXISTS {nombre_DDBB} ;")
            cursor.close
            connection.close
            print (f"base de datos  {nombre_DDBB} eliminada ")
        except Exception as Error:
            print (f"base de datos  {nombre_DDBB} no se pudo eliminar por la excepcion:\n {Error} ")
    pausa()
######################################################################################################

def pack2_tablas():
    limpiar()
    
    print(f"""{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║       ╔═════╗    ╔══════╗   ╔═══════╗   ╔═════╗   ╔═══╦═══╗   ╔═══════╗     ║
║      ╔╝     ╚╗   ║      ╚╗  ║          ╔╝     ╚╗      ║       ║             ║
║      ║           ║       ║  ║          ║       ║      ║       ║             ║
║      ║           ║      ╔╝  ║          ║       ║      ║       ║             ║
║      ║           ╠════╦═╝   ╠═════╣    ╠═══════╣      ║       ╠═════╣       ║
║      ║           ║    ╚╗    ║          ║       ║      ║       ║             ║
║      ╚╗     ╔╝   ║     ╚╗   ║          ║       ║      ║       ║             ║
║       ╚═════╝    ╩      ╚╝  ╚═══════╝  ╩       ╩      ╩       ╚═══════╝     ║
║                                                                             ║
║           ╔═══╦═══╗    ╔═════╗   ╔══════╗   ╦           ╔═════╗             ║
║               ║       ╔╝     ╚╗  ║      ╚╗  ║          ╔╝     ╚╗            ║
║               ║       ║       ║  ║       ║  ║          ║       ║            ║
║               ║       ║       ║  ║      ╔╝  ║          ║       ║            ║
║               ║       ╠═══════╣  ╠══════╣   ║          ╠═══════╣            ║
║               ║       ║       ║  ║      ╚╗  ║          ║       ║            ║
║               ║       ║       ║  ║      ╔╝  ║          ║       ║            ║
║               ╩       ╩       ╩  ╚══════╝   ╚═══════╝  ╩       ╩            ║
║                                                                             ║
║                                                                             ║
║                                                                             ║
║                            ╔══╦══╗        ╔══╦══╗                           ║
║                               ║              ║                              ║
║                               ║              ║                              ║
║                               ║              ║                              ║
║                               ║              ║                              ║
║                               ║              ║                              ║
║                               ║              ║                              ║
║                            ╚══╩══╝        ╚══╩══╝                           ║
║                                  (crear)                                    ║
║                      creamos las tablas y columnas                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    
    
    
    
    
    """
    nombre_DDBB=     diccionario_instalacion ['base_de_datos']
    nombre_tabla_productos=  list(diccionario_instalacion['tablas'].keys())[0]
    nombre_tabla_stock=      list(diccionario_instalacion['tablas'].keys())[1]
    stock_columna_1=  list(diccionario_instalacion['tablas'][nombre_tabla_stock].keys())[0]
    stock_columna_2=  list(diccionario_instalacion['tablas'][nombre_tabla_stock].keys())[1]
    stock_columna_3=  list(diccionario_instalacion['tablas'][nombre_tabla_stock].keys())[2]
    stock_columna_4=  list(diccionario_instalacion['tablas'][nombre_tabla_stock].keys())[3]
    

            "id": "INTEGER AUTOINCREMENT PRIMARY KEY NOT NULL,",
            "lote": "INTEGER NOT NULL,",
            "codigo_producto": "VARCHAR(255) NOT NULL,",
            "cantidad": "INTEGER NOT NULL,",
            "FOREIGN KEY":"(codigo_producto) REFERENCES productos(codigo)"
    """
    # ~ nombre_tabla_productos=  list(diccionario_instalacion['tablas'].keys())[0]
    
    print("*"*50)
    print(f"""
    {stock_columna_1 = }
    {stock_columna_2 = }
    {stock_columna_3 = }
    {stock_columna_4 = }
    """)
    print("*"*50)
    print(f"""{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                  ╔══════╗   ╔═══════╗   ╔═════╗   ╔══════╗                  ║
║                  ║      ╚╗  ║          ╔╝     ╚╗  ║      ╚╗                 ║
║                  ║       ║  ║          ║       ║  ║       ║                 ║
║                  ║      ╔╝  ║          ║       ║  ║       ║                 ║
║                  ╠════╦═╝   ╠═════╣    ╠═══════╣  ║       ║                 ║
║                  ║    ╚╗    ║          ║       ║  ║       ║                 ║
║                  ║     ╚╗   ║          ║       ║  ║      ╔╝                 ║
║                  ╩      ╚╝  ╚═══════╝  ╩       ╩  ╚══════╝                  ║
║                                   (leer)                                    ║
║                                                                             ║
║                      leemos todos los datos de {nombre_tabla_productos}                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
   

    cursor = conectar_base_de_datos()#           sqlite // mysql
    if base_de_datos == "S":#   SQLite
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        # Listar todas las tablas en la base de datos
        tablas = cursor.fetchall()
        print("Tablas en base de datos:")

        for tupla in tablas:
            nombre_tablas = tupla[0]
            print(f"{nombre_tablas}-----------------------------------")

            # Mostrar columnas de la tabla actual
            cursor.execute(f"PRAGMA table_info({nombre_tablas});")
            columnas = cursor.fetchall()

            print("Columnas y tipos de datos:")
            for columna in columnas:
                nombre_columna = columna[1]  # En PRAGMA, el nombre de la columna está en el índice 1
                tipo_dato = columna[2]       # En PRAGMA, el tipo de dato está en el índice 2
                print(f"\t{nombre_columna} - {tipo_dato}")

        # Cerrar la conexión a la base de datos
    
    else:#                      MySQL
        cursor.execute("SHOW TABLES;")
        tablas = cursor.fetchall()
        print ("tablas en base de datos:")
        for tupla in tablas:
            nombre_tablas= tupla[0]
            print(f"{nombre_tablas}-----------------------------------")
            # Mostrar columnas de la tabla actual
            cursor.execute(f"SHOW COLUMNS FROM {nombre_tablas};")
            columnas = cursor.fetchall()

            print("Columnas y tipos de datos:")
            for columna in columnas:
                stock_columna = columna[0]
                tipo_dato = columna[1]
                print(f"\t{stock_columna} - {tipo_dato}")
    print ("^"*100)
    pausa()
    limpiar()
    #---------------------------------------------------------------------------------------
    """
    stock-----------------------------------
    Columnas y tipos de datos:
            id - int
            lote - int
            codigo_producto - varchar(255)
            cantidad - int
query="INSERT IGNORE INTO stock (id, lote, codigo_producto) VALUES (2397, 'K2', 50);"
    """
    print(f"""
    {nombre_tabla_stock = }
    {stock_columna_1 = }
    {stock_columna_2 = }
    {stock_columna_3 = }
    {stock_columna_4 = }
    ---------------------------------------
    {nombre_tabla_productos = }
    """)
    print("*"*50)
    cursor.execute(f"SELECT codigo FROM {nombre_tabla_productos} ;")
    productos = cursor.fetchall()
    print(f"""{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║      ╦    ╦ ╔═══╗      ╔═════╗     ╔═══════╗    ╔══════╗    ╔═══╦═══╗       ║
║      ║    ╠═╝   ╚═╗   ╔╝     ╚╗    ║            ║      ╚╗       ║           ║
║      ║    ║       ║   ║            ║            ║       ║       ║           ║
║      ║    ║       ║   ╚╗           ║            ║      ╔╝       ║           ║
║      ║    ║       ║    ╚══════╗    ╠═════╣      ╠════╦═╝        ║           ║
║      ║    ║       ║           ║    ║            ║    ╚╗         ║           ║
║      ║    ║       ║   ╚╗     ╔╝    ║            ║     ╚╗        ║           ║
║      ╩    ╩       ╩    ╚═════╝     ╚═══════╝    ╩      ╚╝       ╩           ║
║                                  (insertar)                                 ║
║                                                                             ║
║                      insertamos un dato directamente                        ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    for producto in productos:
        lote = random.randint(1111, 9999)  # Genera una cantidad aleatoria entre 1 y 100
        codigo_producto= producto[0]
        cantidad = random.randint(1, 100)  # Genera una cantidad aleatoria entre 1 y 100
        query= (f"""INSERT OR IGNORE INTO {nombre_tabla_stock} ({stock_columna_2}, {stock_columna_3}, {stock_columna_4}) VALUES ({lote}, '{codigo_producto}', {cantidad});""" )#cambiar si es mysql
        if base_de_datos == "M":#   MySQL
            query =  query.replace("?","%s").replace("OR IGNORE","IGNORE")
        print (f"{query=}")
        cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()
    limpiar()
######################################################################################################
def vista():
    # Crear vista con código, precio y stock
    print(f"""{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║       ╔═════╗    ╔══════╗   ╔═══════╗   ╔═════╗   ╔═══╦═══╗   ╔═══════╗     ║
║      ╔╝     ╚╗   ║      ╚╗  ║          ╔╝     ╚╗      ║       ║             ║
║      ║           ║       ║  ║          ║       ║      ║       ║             ║
║      ║           ║      ╔╝  ║          ║       ║      ║       ║             ║
║      ║           ╠════╦═╝   ╠═════╣    ╠═══════╣      ║       ╠═════╣       ║
║      ║           ║    ╚╗    ║          ║       ║      ║       ║             ║
║      ╚╗     ╔╝   ║     ╚╗   ║          ║       ║      ║       ║             ║
║       ╚═════╝    ╩      ╚╝  ╚═══════╝  ╩       ╩      ╩       ╚═══════╝     ║
║                                                                             ║
║                  ╦        ╦   ╦  ╔════════╗  ╦              ╦               ║
║                  ╚╗      ╔╝   ║  ║           ╚╗            ╔╝               ║
║                   ║      ║    ║  ║            ║            ║                ║
║                   ╚╗    ╔╝    ║  ║            ╚╗    ╔╗    ╔╝                ║
║                    ║    ║     ║  ╠═════╣       ║    ║║    ║                 ║
║                    ╚╗  ╔╝     ║  ║             ╚╗  ╔╝╚╗  ╔╝                 ║
║                     ╚╗╔╝      ║  ║              ╚╗╔╝  ╚╗╔╝                  ║
║                      ╚╝       ╩  ╚═══════╝       ╚╝    ╚╝                   ║
║                                                                             ║
║                      creamos las tablas y columnas                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

    cursor = conectar_base_de_datos()#           sqlite // mysql
    query= f"DROP VIEW IF EXISTS {vista_nombre};"
    if base_de_datos == "M":#   MySQL 
        query =  query.replace("IF NOT EXISTS","")
    print         (query)
    cursor.execute(query)
    
    # Crear vista con código, precio y stock
    print(f"""{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                    ══════╗  ╔═════╗   ╦    ╦ ╔═══╗                          ║
║                          ║ ╔╝     ╚╗  ║    ╠═╝   ╚═╗                        ║
║                          ║ ║       ║  ║    ║       ║                        ║
║                          ║ ║       ║  ║    ║       ║                        ║
║                          ║ ║       ║  ║    ║       ║                        ║
║                          ║ ║       ║  ║    ║       ║                        ║
║                  ╚╗     ╔╝ ╚╗     ╔╝  ║    ║       ║                        ║
║                   ╚═════╝   ╚═════╝   ╩    ╩       ╩                        ║
║                                  (borrar)                                   ║
║                                                                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")


    query=(f"""
                CREATE VIEW {vista_nombre} AS
                SELECT p.codigo AS cod_unico, p.precio as p_costo, s.cantidad AS stock
                FROM {nombre_tabla_productos} p
                JOIN {nombre_tabla_stock} s ON p.codigo = s.codigo_producto
            """)
    print         (query)
    cursor.execute(query)
    pausa()
    limpiar()
    #---------------------------------------------------------------------------------------
    # Crear vista con código, precio y stock
    query=(f""" SELECT * FROM  {vista_nombre} ;""")
    print         (query)
    cursor.execute(query)
    productos = cursor.fetchall()
    for producto in productos:
        print (f"{producto=}")
    
    pausa()
    limpiar()
######################################################################################################
def xlsx():
    print(f"""{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║       ╔═════╗    ╔══════╗   ╔═══════╗   ╔═════╗   ╔═══╦═══╗   ╔═══════╗     ║
║      ╔╝     ╚╗   ║      ╚╗  ║          ╔╝     ╚╗      ║       ║             ║
║      ║           ║       ║  ║          ║       ║      ║       ║             ║
║      ║           ║      ╔╝  ║          ║       ║      ║       ║             ║
║      ║           ╠════╦═╝   ╠═════╣    ╠═══════╣      ║       ╠═════╣       ║
║      ║           ║    ╚╗    ║          ║       ║      ║       ║             ║
║      ╚╗     ╔╝   ║     ╚╗   ║          ║       ║      ║       ║             ║
║       ╚═════╝    ╩      ╚╝  ╚═══════╝  ╩       ╩      ╩       ╚═══════╝     ║
║                                                                             ║
║             ╦       ╦      ╦           ╔═════╗     ╦       ╦                ║
║             ╚╗     ╔╝      ║          ╔╝     ╚╗    ╚╗     ╔╝                ║
║              ╚╗   ╔╝       ║          ║             ╚╗   ╔╝                 ║
║               ╚╗ ╔╝        ║          ╚╗             ╚╗ ╔╝                  ║
║               ╔╝ ╚╗        ║           ╚═════╗       ╔╝ ╚╗                  ║
║              ╔╝   ╚╗       ║                 ╚╗     ╔╝   ╚╗                 ║
║             ╔╝     ╚╗      ║          ╚╗     ╔╝    ╔╝     ╚╗                ║
║             ╩       ╩      ╩═══════    ╚═════╝     ╩       ╩                ║
║                                                                             ║
║                                                                             ║
╠═════════════════════════════════════════════════════════════════════════════╣
║       pip install pillow                                                    ║
║       pip install openpyxl                                                  ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    # Exportar datos de la vista a un archivo Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Datos de Stock"

    # Escribir los encabezados
    ws.append(["codigo", "precio", "stock"])

    # Escribir los datos
    
    cursor = conectar_base_de_datos()#           sqlite // mysql
    cursor.execute(f"SELECT * FROM {vista_nombre}")
    filas = cursor.fetchall()

    #----------------------------------------

    # ~ agregar columna total (stock x precio)

    #----------------------------------------
    for fila in filas:
        ws.append(fila)

    # Guardar el archivo Excel
    wb.save("datos_stock.xlsx")

    # Cerrar la conexión
    connection.commit()
    connection.close()
    print("Datos exportados buscar en la carpeta 'datos_stock.xlsx'")

    pausa()
    limpiar()
############################################################################################
############################################################################################
############################################################################################

def crear_procedimiento_obtener_stock():
    try:
        # Conexión a la base de datos MySQL
        cursor = conectar_base_de_datos()#           sqlite // mysql

        # Seleccionar productos con stock bajo
        query=(f"""
                    SELECT {stock_columna_3}, {stock_columna_4}
                    FROM {nombre_tabla_stock}
                    WHERE {stock_columna_4} <= 20 ;
                """)# -- Puedes ajustar este valor a lo que consideres "stock bajo"        
        if base_de_datos == "S":
            # Obtener los resultados
            print(f"query={query}")
            cursor.execute(query)
            stock_bajo = cursor.fetchall()
            # Mostrar el listado de productos con stock bajo
            if stock_bajo:
                print("Listado de productos con stock bajo:")
                for codigo, cantidad in stock_bajo:
                    print(f"Código: {codigo}, Cantidad: {cantidad}")
            else:
                print("No hay productos con stock bajo.")
            pausa()
        else:
            try:
                drop= f"DROP PROCEDURE  {nombre_proc};"
                print         (drop)
                cursor.execute(drop)
            except :
                pass
            #---------------------------------------------------------------------------------------
            # Crear el procedimiento almacenado en MySQL
            # ~ CREATE PROCEDURE IF NOT EXISTS {nombre_proc}()
            procedimiento = f"""
            CREATE PROCEDURE {nombre_proc}()
            BEGIN
                {query}
            END
            """
            print(f"procedimiento: {procedimiento}")
            cursor.execute(procedimiento)
            print(f"Procedimiento almacenado '{nombre_proc}' creado exitosamente.")


        # Commit para confirmar los cambios en la base de datos
        connection.commit()
    # ~ except mysql.connector.Error as err:
        # ~ print(f"Error: {err}")
    # ~ excer4pt sqlite3.Error as err:
        # ~ print(f"Error: {err}")
    except Exception as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
    pausa()
    #---------------------------------------------------------------------------------------
    limpiar()

############################################################################################
def obtener_stock_bajo_proc_almacenado():
    cursor = conectar_base_de_datos()#           sqlite // mysql
    if base_de_datos == "S":#   
        print ("SQLite no acepta procedimiento almacenado")
        query=(f"""
            SELECT {stock_columna_3}, {stock_columna_4}
            FROM {nombre_tabla_stock}
            WHERE {stock_columna_4} <= 20
        """)# -- Puedes ajustar este valor a lo que consideres "stock bajo"        
        # Obtener los resultados
        print(f"query={query}")
        cursor.execute(query)
        stock_bajo = cursor.fetchall()
        # Mostrar el listado de productos con stock bajo
        if stock_bajo:
            print("Listado de productos con stock bajo:")
            for codigo, cantidad in stock_bajo:
                print(f"Código: {codigo}, Cantidad: {cantidad}")
        else:
            print("No hay productos con stock bajo.")
        print ("SQLite no acepta procedimiento almacenado")
        pausa()
        return
    try:
        # Ejecutar el procedimiento almacenado
        cursor.callproc(nombre_proc)
        # Obtener los resultados
        for result in cursor.stored_results():
            stock_bajo = result.fetchall()
        # Mostrar el listado de productos con stock bajo
        if stock_bajo:
            print("Listado de productos con stock bajo:")
            for codigo, cantidad in stock_bajo:
                print(f"Código: {codigo}, Cantidad: {cantidad}")
        else:
            print("No hay productos con stock bajo.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()
    pausa()
    #---------------------------------------------------------------------------------------
    limpiar()
def google_cloud():
    '''
    # Crear vista con código, precio y stock
    query=(f""" SELECT * FROM  {vista_nombre} ;""")
    print         (query)
    df = pd.read_sql(query, conn)
    for producto in df.iterrows():
        print (f"{producto=}")
    
    connection.close()

    # Abrir la hoja de Google Sheets y escribir los datos
    spreadsheet = client.open("desde_sql")  # Reemplaza con el nombre de tu archivo de Google Sheets
    worksheet = spreadsheet.worksheet("vista_sql")  # Reemplaza con el nombre de la pestaña donde quieres guardar los datos

    # Escribir el DataFrame en Google Sheets
    set_with_dataframe(worksheet, df)
    print("Datos guardados en Google Sheets correctamente.")

    Autenticación y autorización: Configura gspread con las credenciales del archivo JSON para que puedas acceder a Google Sheets.
    Conexión a la base de datos SQL: Establece la conexión a tu base de datos y carga los datos en un DataFrame.
    Escribir en Google Sheets: Utiliza set_with_dataframe para escribir los datos en la hoja de cálculo en la pestaña que elijas.
    Consideraciones
    Si necesitas actualizar los datos en lugar de sobrescribirlos, puedes adaptar el código para borrar el contenido previo de la hoja antes de cargar el nuevo DataFrame.
    Asegúrate de que el archivo JSON de credenciales está seguro y que no lo compartes públicamente.
    Este script debería almacenar tus datos de SQL en Google Sheets de manera efectiva.
    '''
    import pandas as pd
    from sqlalchemy import create_engine
    import gspread
    from gspread_dataframe import set_with_dataframe

    host= {diccionario_instalacion ["conexion"]["host"]}
    user= {diccionario_instalacion ["conexion"]["user"]} 
    passwd= {diccionario_instalacion ["conexion"]["passwd"]}

    # Parámetros de conexión
    # ~ host = "localhost"
    # ~ user = "root"
    # ~ passwd = "2025"
    # ~ nombre_DDBB = "IT_bbdd_2025_2" 

    # Configuración de conexión con SQLAlchemy
    db_url = f"mysql+pymysql://{user}:{passwd}@{host}/{nombre_DDBB}"
    engine = create_engine(db_url)

    # Consulta de datos en la base de datos con SQLAlchemy y Pandas
    query = "SELECT * FROM vista"
    df = pd.read_sql(query, engine)

    # Cerrar la conexión
    engine.dispose()

    # Conexión a Google Sheets
    gc = gspread.oauth()  # Esto abrirá una ventana para autenticación en Google
    hoja = gc.open("Nombre_de_tu_Hoja_de_Calculo").sheet1

    # Escribir el DataFrame en Google Sheets
    set_with_dataframe(hoja, df)
    
    
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
opcion = ""
nombre_DDBB=     diccionario_instalacion ['base_de_datos']
nombre_tabla_productos=  list(diccionario_instalacion['tablas'].keys())[0]
nombre_columna_1=  list(diccionario_instalacion['tablas'][nombre_tabla_productos].keys())[0]
nombre_columna_2=  list(diccionario_instalacion['tablas'][nombre_tabla_productos].keys())[1]
nombre_columna_3=  list(diccionario_instalacion['tablas'][nombre_tabla_productos].keys())[2]
nombre_columna_4=  list(diccionario_instalacion['tablas'][nombre_tabla_productos].keys())[3]
"""
        "productos": {
            "codigo": "VARCHAR(255) PRIMARY KEY NOT NULL,",
            "descripcion": "TEXT NOT NULL,",
            "precio": "FLOAT,",            
            "vencimiento": "DATE"
        },"""
nombre_tabla_stock=      list(diccionario_instalacion['tablas'].keys())[1]
stock_columna_1=  list(diccionario_instalacion['tablas'][nombre_tabla_stock].keys())[0]
stock_columna_2=  list(diccionario_instalacion['tablas'][nombre_tabla_stock].keys())[1]
stock_columna_3=  list(diccionario_instalacion['tablas'][nombre_tabla_stock].keys())[2]
stock_columna_4=  list(diccionario_instalacion['tablas'][nombre_tabla_stock].keys())[3]
"""
        "stock": {
            "id": "INTEGER AUTOINCREMENT PRIMARY KEY NOT NULL,",
            "lote": "INTEGER NOT NULL,",
            "codigo_producto": "VARCHAR(255) NOT NULL,",
            "cantidad": "INTEGER NOT NULL,",
            "FOREIGN KEY":"(codigo_producto) REFERENCES productos(codigo)"
        },"""
vista_nombre = "vista"
nombre_proc  = "ObtenerStockBajo"
while opcion !="0":
    limpiar()
    print(f"""{Fore.WHITE+Back.GREEN}
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                 ╔═════╗    ╔══════╗    ╦       ╦    ╔══════╗                ║
║                ╔╝     ╚╗   ║      ╚╗   ║       ║    ║      ╚╗               ║
║                ║           ║       ║   ║       ║    ║       ║               ║
║                ║           ║      ╔╝   ║       ║    ║       ║               ║
║                ║           ╠════╦═╝    ║       ║    ║       ║               ║
║                ║           ║    ╚╗     ║       ║    ║       ║               ║
║                ╚╗     ╔╝   ║     ╚╗    ╚╗     ╔╝    ║      ╔╝               ║
║                 ╚═════╝    ╩      ╚╝    ╚═════╝     ╚══════╝                ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

# ~ print(cursor.rowcount, "record inserted in pool.")
    print ("""
    1) Create - Crear base
    2) Create - Crear tablas
    3) Insert - Insertar datos                    A
    4) Read   - Leer datos
    5) Update - Actualizar datos                  M
    6) Delete - Borrar datos                      B
    7) Delete - Borrar tablas
    8) Delete - Borrar BBDD
    9) tabla stock +
    10) vista
    11) xlsx (Excel - Calc)
    12) crear_procedimiento_obtener_stock
    13) obtener_stock_bajo_proc_guardado
    14) google
    0) Salir del programa""")
    opcion=input("Ingrese la opción seleccionada :").upper()
    match(opcion):
        case "1":
            crear_base()
        case "2":
            crear_tablas()
        case "3":
            insertar_datos()
        case "4":
            leer_tabla()
        case "5":
            actualizar_datos()
        case "6":
            borrar_datos()
        case "7":
            borrar_tablas()
        case "8":
            borrar_base()
        case "9":
            pack2_tablas()
        case "10":
            vista()
        case "11":
            xlsx()
        case "12":
            crear_procedimiento_obtener_stock()
        case "13":
            obtener_stock_bajo_proc_almacenado()
        case "14":
            google_cloud()
        case "0":
            exit()
        case other: # case _:
            print("opcion incorrecta")
############################################################################################
#  Python : print, input, for, while, def, if/else/elif, try/except                        #
#      POO                                                                                 #
#  SQL:     connection, cursor, create, insert, delete, select, drop, update               #
#      NEXT         alter, procedimientos                                                  #
############################################################################################
import this



