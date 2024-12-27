#######################################################################################################
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
from colorama import *
#######################################################################################################
limpiar()
from datetime import datetime, date, time
# ~ pausa();limpiar();#(0,estado='inicio',modulo=4)
import math
import datetime
import pandas 

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

base_de_datos=""

while base_de_datos not in ["S","M"]:
    base_de_datos = input("Seleccione entre:\n\tM) para MySQL\n\tS) para SQLite   :""").upper()
limpiar()


match (base_de_datos):
    case "S":
        cartel="""
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
╚═════════════════════════════════════════════════════════════════════════════╝"""
        limpiar()
        print(f"""{Fore.WHITE+Back.BLUE+cartel+Style.RESET_ALL}""")
        import sqlite3
    case "M":

        ####################################################################################################
        
        cartel="""
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
╚═════════════════════════════════════════════════════════════════════════════╝"""
        limpiar()
        print(f"""{Fore.WHITE+Back.BLUE+cartel+Style.RESET_ALL}""")
        try:
            import mysql.connector
        except Exception as error_:
            print ("la libreria mysql.connector, no esta disponible. Paso a descargarla e instalarla")
            import pip
            pip.main(['install', 'mysql-connector-python'])
        from mysql.connector import Error
        from mysql.connector import errorcode
        # ~ try:
            # ~ import pymysql
            # ~ import pymysql.cursors
        # ~ except Exception as error_:
            # ~ import pip
            # ~ pip.main(['install', 'pymysql'])
            # ~ import pymysql
        # ~ import pymysql.cursors
        # ~ try:
            # ~ import sqlachemy
        # ~ except Exception as error_:
            # ~ import pip
            # ~ pip.main(['install', 'sqlachemy'])
            # ~ import sqlachemy
        # ~ import sqlachemy
print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

pausa()
limpiar()
import datetime
hoy = datetime.date.today()
print(hoy)
def carga_datos_mysql(**dic_datos):
    usuario = input ("ingrese el usuario: ¿'root'?:")
    if usuario == "":
        usuario = "root"
    password_de_msql= input ("ingrese el password: ¿'2025'?:")
    if password_de_msql == "":
        password_de_msql = "2025"
    host= input ("ingrese el donde esta la base de datos (host) ¿'localhost'?:")
    if host == "":
        host = "localhost"
    #---------------------------------------------------------------------------------------------
    return {"host": host ,"user": usuario , "passwd": password_de_msql}
######################################################################################################
def conectar_base_de_datos(inicial=False):
    global nombre_DDBB
    global dic_datos
    global connection
    try:
        connection.close()
    except:
        pass
    if base_de_datos == "S":#   SQLite
        #---------------------------------------------------------------------------------------------
        connection = sqlite3.connect(f'{nombre_DDBB}.db')
        # PREGUNTA AL SISTEMA OPERATIVO LOS ARCHIVOS ",DB" ( BBDD) QUE TIENE, LUEGO SI LA QUE VOY A USAR ESTA EN LA COLECCION
        # import os
        # if os.path.isfile(f'{nombre_DDBB}.db'):
        #       si existe
        #else:
        #       no existe la creo

        #---------------------------------------------------------------------------------------------
    elif base_de_datos == "M":#                      MySQL
        if len(dic_datos)==0 :
            dic_datos= carga_datos_mysql(**dic_datos)
        if inicial is False:
            dic_datos= {**dic_datos, "database":nombre_DDBB}
        print (f"-------------------{dic_datos=}")
        salida = f"""mysql.connector.connect( {dic_datos} )"""
        print (salida)
        connection = mysql.connector.connect (**dic_datos)
        print (f"conectado a la base de datos {nombre_DDBB}")
    return connection.cursor()
######################################################################################################
def crear_base():
    global dic_datos
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
║                 ╔══════╗    ╔═════╗    ╔═════╗   ╔═══════╗                  ║
║                 ║      ╚╗  ╔╝     ╚╗  ╔╝     ╚╗  ║                          ║
║                 ║       ║  ║       ║  ║          ║                          ║
║                 ║      ╔╝  ║       ║  ╚╗         ║                          ║
║                 ╠══════╣   ╠═══════╣   ╚═════╗   ╠══════╣                   ║
║                 ║      ╚╗  ║       ║         ╚╗  ║                          ║
║                 ║      ╔╝  ║       ║  ╚╗     ╔╝  ║                          ║
║                 ╚══════╝   ╩       ╩   ╚═════╝   ╚═══════╝                  ║
║                                                                             ║
║                                  (crear)                                    ║
║                                                                             ║
║                   creamos la base de datos si no existe                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    
    if base_de_datos == "S":#   SQLite
        print               ("se crea en un archivo al generar la conexion")
    else:#                      MySQL                        
        cursor = conectar_base_de_datos(True)#           sqlite // mysql
        query = f"CREATE DATABASE IF NOT EXISTS {nombre_DDBB}"#string
        print               (query)
        cursor.execute      (query)
        cursor.close()
        connection.close()
    pausa()
######################################################################################################
def crear_tablas():
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
║                                  (crear)                                    ║
║                      creamos las tablas y columnas                          ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    print ("Conectamos con SQLite")
    ######################################################################################################

    print ("CREATE TABLE")
    print ("CREATE COLUMN")
    cursor = conectar_base_de_datos()#           sqlite // mysql

    '''
    nombre_DDBB      = "IT_bbdd_2025"
    nombre_tabla     = "IT_Mi_Tabla"
    nombre_columna_1 = "descripcion"
    nombre_columna_2 = "precio"
    nombre_columna_3 = "codigo"
    nombre_columna_4 = "vencimiento"

    query= (f"""CREATE TABLE IF NOT EXISTS {nombre_tabla}
                                                
                                                        descripcion VARCHAR(255) NOT NULL,
                                                        precio FLOAT,
                                                        codigo TEXT,
                                                        vencimiento DATE ) """)#literal
    '''

    #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-##

    if base_de_datos == "S":  # SQLite
        query = f"""CREATE TABLE IF NOT EXISTS {nombre_tabla} (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                                    {nombre_columna_1} VARCHAR(255) NOT NULL,
                                                                    {nombre_columna_2} FLOAT,
                                                                    {nombre_columna_3} TEXT NOT NULL,
                                                                    {nombre_columna_4} DATE
                                                                )"""
    else:  # MySQL
        query = f"""CREATE TABLE IF NOT EXISTS {nombre_tabla} (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                                                    {nombre_columna_1} VARCHAR(255) NOT NULL,
                                                                    {nombre_columna_2} FLOAT,
                                                                    {nombre_columna_3} TEXT NOT NULL,
                                                                    {nombre_columna_4} DATE
                                                                )"""

    # ~ #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-##

    # ~ query= (f"""CREATE TABLE IF NOT EXISTS {nombre_tabla}(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                        # ~ descripcion VARCHAR(255) NOT NULL,
                                                        # ~ precio FLOAT,
                                                        # ~ codigo TEXT,
                                                        # ~ vencimiento DATE ) """)#literal
    # ~ if base_de_datos == "M": # MySQL
        # ~ query=query.replace("INTEGER","INT").replace("AUTOINCREMENT","AUTO_INCREMENT")#.replace("TEXT","VARCHAR (255)")


    """---------------------------------------------------------------------------------------------------------------------
                SQLite                                      (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                MySQL                                       (id INT     PRIMARY KEY AUTO_INCREMENT NOT NULL,
                                                                  ^                     ^
                                                                  |_ INT x INTEGER      |_AUTOINCREMENT x AUTO_INCREMENT
    """

    print               (query)
    cursor.execute      (query)
    cursor.close()
    connection.close()
    pausa()
######################################################################################################
def insertar_datos():
    limpiar()
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
    print ("Conectamos con SQLite")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    print ("RECORD INSERT")
    query = f"""INSERT INTO  {nombre_tabla}
                                        (descripcion, precio, codigo, vencimiento)
                                  VALUES('Galletitas', 222 , 'Titas','2025-01-01')"""
    try:
        print           (query)
        cursor.execute  (query)
    except Exception as error_sql:
        print (f"hay un error {error_sql}")
    connection.commit()
    print(cursor.rowcount, "record inserted.")
    pausa()
    limpiar()
    print(f"""{Fore.WHITE+Back.GREEN}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos un dato por intermedio de comodines         ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    query=f"""INSERT INTO  {nombre_tabla}  (descripcion, precio, codigo, vencimiento) """
    if base_de_datos == "S":#   SQLite
        query +=  "VALUES( ?, ?, ?, ?)"
    else:#                      MySQL
        query +=  "VALUES(%s,%s,%s,%s)"

    """
SQLite         VALUES( ?, ?, ?, ?)"
MySQL          VALUES(%s,%s,%s,%s)"
    """
    #   query=f"""INSERT INTO  {nombre_tabla}  (descripcion, precio, codigo, vencimiento) VALUES(?,?,?,?)"""
    #   query=f"""INSERT INTO  {nombre_tabla}  (descripcion, precio, codigo, vencimiento) VALUES(%s,%s,%s,%s)"""
    proy=('Alfajores', 88 , 'ALF','2025-01-01')
    try:
        print           (query,proy)
        cursor.execute  (query,proy)
    except Exception as error_sql:
        print (f"hay un error {error_sql}")
    connection.commit()
    print(cursor.rowcount, "record inserted.")
    pausa()
    limpiar()
    ######################################################################################################
    print(f"""{Fore.WHITE+Back.GREEN}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de comodines     ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")


    query = f"""INSERT INTO  {nombre_tabla}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) """
    if base_de_datos == "S":#   SQLite
        query +=  "VALUES( ?, ?, ?, ?)"
    else:#                      MySQL
        query +=  "VALUES(%s,%s,%s,%s)"

    """
SQLite         VALUES( ?, ?, ?, ?)"
MySQL          VALUES(%s,%s,%s,%s)"
    """
    #   query = f"""INSERT INTO  {nombre_tabla}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) VALUES(?,?,?,?);"""
    #   query = f"""INSERT INTO  {nombre_tabla}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) VALUES(%s,%s,%s,%s);"""
    print   (f'columnas_SQLite = ',query)
    try:
        cursor.execute  (query, ("Chocolates-", 9999 , "Choc", '2025-06-15'))
        # ~ connection.commit()#     <-------  eliminar
        cursor.execute  (query, ("Fideos-", 30 , "f1-", '2025-06-15'))
        # ~ connection.commit()#     <-------  eliminar
        cursor.execute(query,   ("Arroz-", 25 , "A1-", '2025-08-15'))
        # ~ connection.commit()#     <-------  eliminar
        cursor.execute(query,   ("Agua-", 20 , "H2O-", '2025-09-15'))
        # ~ connection.commit()#     <-------  eliminar
        cursor.execute(query,   ("Tomates-", 15 , "T1-", '2025-02-15'))
        # ~ connection.commit()#     <-------  eliminar
        cursor.execute(query,   ("Sal-", 10, "S1-", '2025-10-15'))
        # ~ connection.commit()#     <-------  eliminar
        cursor.execute(query,   ("cacao-", 30 , "choco-", '2025-11-15'))
        # ~ connection.commit()#     <-------  eliminar
        cursor.execute(query,   ("gelatina-", 25 , "hl-", '2025-12-15'))
        # ~ connection.commit()#     <-------  eliminar
        cursor.execute(query,   ("flan-", 20 , "flan-", '2025-01-15'))
        connection.commit()#     <-------                               No eliminar
        print(cursor.rowcount, "record inserted.")
    except Exception as error_sql:
        print (f"hay un error {error_sql}")
    pausa()
    limpiar()
    ######################################################################################################
    print(f"""{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de listas 1 a 1  ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    print   (f'con for columnas_SQLite = ',query)
    proy= ( ("Chocolates",  99 , "Choc-"  , '2025-06-15'),
            ("Fideos"    , 300 , "f1--"   , '2025-06-15'),
            ("Arroz"     , 250 , "A1--"   , '2025-08-15'),
            ("Agua"      , 200 , "H2O--"  , '2025-09-15'),
            ("Tomates"   , 105 , "T1--"   , '2025-11-22'),
            ("Sal"       , 100 , "S1--"   , '2025-10-15'),
            ("cacao"     , 300 , "choco--", '2025-11-15'),
            ("gelatina"  , 205 , "hl--"   , '2025-12-15'),
            ("flan"      , 200 , "flan--" , '2025-01-15'))
    # ~ query = f"""INSERT INTO  {nombre_tabla}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) """
    for datos in proy:
        try:
            cursor.execute(query,datos)
        except Exception as error_sql:
            print (f"hay un error {error_sql}")
    connection.commit()# <-------------------------------------------------destabular
    print(cursor.rowcount, "record inserted.")
    pausa()
    limpiar()
    print(f"""{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos varios dato por intermedio de lista directa ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    proy = [
                ("Tomates2"  , 15 , "T1---" , '2025-07-15'),
                ("Sal2"      , 10 , "S1---" , '2025-02-15'),
                ("Fideos2"   , 30 , "f1---" , '2025-01-15'),
                ("Arroz2"    , 25 , "A1---" , '2025-04-15'),
                ("Agua2"     , 20 , "H2O---", '2025-07-15'),
                ("Ajies2"    , 15 , "T1---" , '2025-02-15'),
                ("Pimienta2" , 10 , "S1---" , '2025-01-15'),
                ("Cafe2"     , 30 , "f1---" , '2025-04-15'),
                ("Yerba2"    , 25 , "A1---" , '2025-07-15'),
                ("Te2"       , 20 , "H2O---", '2025-02-25'),
                ("Pan2"      , 15 , "T1---" , '2025-01-15'),
                ("Queso2"    , 10 , "S1---" , '2025-12-15')
            ]
    # ~ query = f"""INSERT INTO  {nombre_tabla}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) """
    try:
        print             (query,proy)
        cursor.executemany(query,proy)# ~ cursor.execute(query,datos) + many --->SQL no python
    except Exception as error_sql:
        print (f"hay un error {error_sql}")
    connection.commit()
    cant_ins =cursor.rowcount
    
    if cant_ins==len(proy):
        print ("todo bien")
    else:
        print ("datos no ingresados")
    
    print(cant_ins, "record inserted in pool.")
    ###################################################################################################
    pausa()
    limpiar()
    print(f"""{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                      insertamos manualmente                                 ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")

    while True:
        print("Ingreso de datos a mano ")
        pausa()
        dato_desc=""
        while not (5<=len(dato_desc)<=255):
            dato_desc  = input ("Ingrese la descripcion (+ de 5 caracteres) del producto ('ZZZZZ' para Salir): ").upper()
        if dato_desc.startswith ("ZZZZZ"):
            break

        dato_precio = ""
        while not dato_precio.replace(".","").isdecimal():
            dato_precio=input("ingrese el precio: ")
        dato_precio=float (dato_precio)


        dato_codigo = ""
        while not (dato_codigo.replace(" ","").isalnum() and len(dato_codigo)<=255):
            dato_codigo=input("ingrese el cod.prod (alnum): ")
        dato_codigo= int (dato_precio)
        #from datatime import date, deltatime
        dato_fecha = datetime.date.today()
        # Crear un delta de 60 días
        delta = datetime.timedelta(days=60)

        # Sumar el delta a la fecha actual
        nueva_fecha = dato_fecha + delta

        print(f"Fecha actual: {dato_fecha}")
        print(f"Fecha después de 60 días: {nueva_fecha}")
        dato_fecha_str = nueva_fecha.isoformat()

        # Ejecutar la consulta con la fecha convertida
        cursor.execute(query, (dato_desc, dato_precio, dato_codigo, dato_fecha_str))# sqlite3 o  MySql
        connection.commit()
        print(cursor.rowcount, "record inserted.")
######################################################################################################
def leer_tabla():
    limpiar()
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
║                      leemos todos los datos de Mi_Tabla                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    print(f"ME TRAIGO 'TODA' LA BASE DE DATOS")
    query = f"SELECT * FROM {nombre_tabla}; "
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    
    for linea in datos_desde_sql:
        print (linea)
    pausa()
    
    print("*"*50)
    print(f"""
    {nombre_columna_1 = }
    {nombre_columna_2 = }
    {nombre_columna_3 = }
    {nombre_columna_4 = }
    """)
    print("*"*50)
    pausa()
    
    
    
    print(f"""
    LUEGO CON 'TODA' LA BASE DE DATOS CARGADA EN PYTHON
    SELECCIONA SOLO CODIGO 'A1'""")
    for linea in datos_desde_sql:
        if linea[3].upper()=="A1":
            print ("dato: ",linea)
    pausa()


    query = f"SELECT * FROM {nombre_tabla} WHERE {nombre_columna_3} = 'A1'"
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    print(f" ME TRAIGO SOLO CODIGO 'A1' DE LA BASE DE DATOS")
    print(f"{query=}")
    for linea in datos_desde_sql:
        print ("dato: ",linea)

    pausa()

    print(f" ME TRAIGO SOLO DESCRIPCIÓN QUE EN ALGUN LADO CONTENGA 'A' DE LA BASE DE DATOS")
    query = f"SELECT * FROM {nombre_tabla} WHERE {nombre_columna_3} LIKE '%A%'"
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    print(f"{query=}")
    print("A.....")
    for linea in datos_desde_sql:
        print ("dato: ",linea)

    pausa()
    print(f" ME TRAIGO SOLO DESCRIPCIÓN QUE TERMINE CON 'A' DE LA BASE DE DATOS")
    query = f"SELECT {nombre_columna_2} FROM {nombre_tabla} WHERE {nombre_columna_1} LIKE '%A'"
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    print(f"{query=}")
    print(".....A")
    for linea in datos_desde_sql:
        print ("dato: ",linea)
    '''
    nombre_columna_1 = "descripcion"
    nombre_columna_2 = "precio"
    nombre_columna_3 = "codigo"
    nombre_columna_4 = "vencimiento"

    query = "SELECT * FROM {nombre_tabla} WHERE '' "
    -- WHERE vencimiento >= '2024-10-01' AND vencimiento <= '2025-05-01'
    -- WHERE vencimiento >= '2024-10-01' OR  vencimiento <= '2025-05-01'
    -- WHERE NOT (vencimiento >= '2025-01-01' OR  vencimiento <= '2025-01-01')
    -- WHERE codigo IN ('H2O','S1','A1')
    -- WHERE precio BETWEEN 10 AND  100
    -- WHERE precio BETWEEN 10 AND  100
    -- WHERE descripcion like 'A%'
    -- WHERE descripcion like '%r%'-- #                    % cualquier cantidad de caracteres
    -- WHERE descripcion like 'A___z'-- #Arroz             _ un solo caracter
    -- WHERE descripcion REGEXP  '^A'-- #                  REGULAR EXPRESION ^inicio, fin^, | or, [caracteres] entres estos , [a-h] entre a y h
    -- WHERE descripcion IS NULL
    -- WHERE descripcion IS NOT NULL

    query ="SELECT * FROM {nombre_tabla} "
    query ="SELECT * FROM {nombre_tabla} WHERE precio BETWEEN 10 AND  100 and codigo like '%Z' "
    query ="SELECT * FROM {nombre_tabla} WHERE codigo IN 'H2O','S1','A1' "
    query ="SELECT * FROM {nombre_tabla} WHERE codigo like '%H%' "
    inicio = input ("INgrese las primeras letras del producto a buscar:")
    inicio = inicio +"%"
    
    
-- SELECT dn.nombre_donante AS nombre_donante, MAX(d.monto) AS maximo_donado
-- FROM donacion d
-- JOIN donantes dn ON d.id_donante = dn.id_donante  
-- GROUP BY dn.nombre_donante  
-- ORDER BY maximo_donado DESC -- LIMIT 5;

    
    
    '''

    inicio = "A%"
    query =(f"SELECT * FROM {nombre_tabla} WHERE descripcion like '{inicio}' ")
    print               (query)
    cursor.execute      (query)
    prod = cursor.fetchall()
    for linea in prod:
        print (f"filtrados {linea}")
    pausa()
    limpiar()
    cursor.close()
    connection.close()
######################################################################################################
def actualizar_datos():
    limpiar()
    print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    cursor = conectar_base_de_datos()#           sqlite // mysql

    query = f"""UPDATE {nombre_tabla} SET {nombre_columna_3} = 'T_lta' 
                WHERE {nombre_columna_1} = 'Tomates' """
    print (query)
    cursor.execute(query)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()
######################################################################################################
def borrar_datos():
    limpiar()
    print(f"""{Fore.WHITE+Back.BLUE}
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
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    query = f"DELETE FROM {nombre_tabla}  WHERE {nombre_columna_1} = 'Sal'"# and {columna2} = '{dato2}'
    cursor.execute(query )
    print(cursor.rowcount, "record(s) affected")
    query = f"DELETE FROM {nombre_tabla}  WHERE {nombre_columna_1} = "

    if base_de_datos == "S":#   SQLite
        query +=  " ? "
    else:#                      MySQL
        query +=  "%s "
    """
SQLite         ?   "
MySQL          %s  "
    """

    proy = ("Te", ) # VA una coma para generar una lista
    print         (query , proy)
    cursor.execute(query , proy)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()
    #--------------------------------------------------------------------
    proy = ("pizza", ) # VA una coma para generar una lista
    print         (query , proy)
    cursor.execute(query , proy)
    connection.commit()
    print(cursor.rowcount, "record(s) affected")
    pausa()
######################################################################################################
def borrar_tablas():
    limpiar()
    cursor = conectar_base_de_datos()#           sqlite // mysql

    print(f"""{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║                         borramos la tabla de la base                        ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    try:
        query= f"DROP TABLE IF EXISTS  {nombre_tabla}"
        print                           (query)
        resultado=cursor.execute        (query)

        print ("cursor.execute:",resultado)
        print(cursor.rowcount, "record(s) affected")
        print (f"tabla  {nombre_tabla} eliminada ")
    except Exception as Error:
        print (f"tabla  {nombre_tabla} no se pudo eliminar por la excepcion:\n {Error} ")
    pausa()
######################################################################################################
def borrar_base():
    limpiar()
    cursor = conectar_base_de_datos()#           sqlite // mysql
    print(f"""{Fore.WHITE+Back.BLUE}
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
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    """
SQLite        no puede eliminarse desde dentro "
MySQL         se elimina con drop "
    """
    if base_de_datos == "S":#   SQLite
        print ("borramos base por archivos")
        try:
            #sqlite3.connect(f'{nombre_DDBB}.db')
            os.remove(f'{nombre_DDBB}.db')
        except:
            print("el archivo esta abierto o no existe")
    else:#                      MySQL
        print ("borramos base por puerto 3306")
        try:
            limpiar()
            cursor = conectar_base_de_datos()#           sqlite // mysql
            cursor.execute(f"DROP DATABASE IF EXISTS {nombre_DDBB} ;")
            cursor.close()
            connection.close()
            print (f"base de datos  {nombre_DDBB} eliminada ")
        except Exception as Error:
            print (f"base de datos  {nombre_DDBB} no se pudo eliminar por la excepcion:\n {Error} ")
    pausa()

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


opcion = ""
dic_datos={}
nombre_DDBB      = "IT_bbdd_2025_lunes_y_viernes"
nombre_tabla     = "IT_Mi_Tabla"
nombre_columna_1 = "descripcion"
nombre_columna_2 = "precio"
nombre_columna_3 = "codigo"
nombre_columna_4 = "vencimiento"

while opcion !="0":
    limpiar()
    print("""\033[1;37;44m\n
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
╚═════════════════════════════════════════════════════════════════════════════╝\033[0m
    """)
    print(f"""{Fore.WHITE+Back.BLUE+cartel+Style.RESET_ALL}""")
# ~ print(cursor.rowcount, "record inserted in pool.")
    print ("\n\n\n");
    print ("1) Create - Crear base");
    print ("2) Create - Crear tablas");
    print ("3) Insert - Insertar datos");
    print ("4) Read   - Leer datos");
    print ("5) Update - Actualizar datos");
    print ("6) Delete - Borrar datos");
    print ("7) Delete - Borrar tablas");
    print ("8) Delete - Borrar BBDD");

    print ("0) Salir del programa")
    opcion=input("Ingrese la opción seleccionada :").upper()
    if opcion == "1":
        crear_base()
    elif opcion == "2":
        crear_tablas()
    elif opcion == "3":
        insertar_datos()
    elif opcion == "4":
        leer_tabla()
    elif opcion == "5":
        actualizar_datos()
    elif opcion == "6":
        borrar_datos()
    elif opcion == "7":
        borrar_tablas()
    elif opcion == "8":
        borrar_base()
    elif opcion == "0":
        exit()
    else:
        print("opcion incorrecta")
