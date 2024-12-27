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
║                            _____________________                            ║
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
        if inicial is True:
            dic_datos= {**dic_datos}
        elif inicial is False:
            dic_datos= {**dic_datos, "database":nombre_DDBB}
        print (f"-------------------{dic_datos=}")
        salida = f"""mysql.connector.connect( {dic_datos} )"""
        print (salida)
        connection = mysql.connector.connect (**dic_datos)
        print (f"conectado a la base de datos {nombre_DDBB}")
    return connection.cursor()
######################################################################################################
######################################################################################################
def crear_base():
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

    cursor = conectar_base_de_datos(inicial=True)#           sqlite // mysql
    if base_de_datos == "S":#   SQLite
        print               ("se crea en un archivo al generar la conexion")
    else:#                      MySQL

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
    
    query= (f"""CREATE TABLE IF NOT EXISTS {nombre_tabla_productos}(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                                        descripcion VARCHAR(255) NOT NULL,
                                                        precio FLOAT,
                                                        codigo TEXT,
                                                        vencimiento DATE ) """)#literal
    if base_de_datos == "M": # MySQL
        query=query.replace("INTEGER","INT").replace("AUTOINCREMENT","AUTO_INCREMENT")#.replace("TEXT","VARCHAR (255)")

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
    query = f"""INSERT INTO  {nombre_tabla_productos}
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
    query=f"""INSERT INTO  {nombre_tabla_productos}  (descripcion, precio, codigo, vencimiento) """
    if base_de_datos == "S":#   SQLite
        query +=  "VALUES( ?, ?, ?, ?)"
    else:#                      MySQL
        query +=  "VALUES(%s,%s,%s,%s)"

    """
SQLite         VALUES( ?, ?, ?, ?)"
MySQL          VALUES(%s,%s,%s,%s)"
    """
    #   query=f"""INSERT INTO  {nombre_tabla_productos}  (descripcion, precio, codigo, vencimiento) VALUES(?,?,?,?)"""
    #   query=f"""INSERT INTO  {nombre_tabla_productos}  (descripcion, precio, codigo, vencimiento) VALUES(%s,%s,%s,%s)"""
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


    query = f"""INSERT INTO  {nombre_tabla_productos}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) """
    if base_de_datos == "S":#   SQLite
        query +=  "VALUES( ?, ?, ?, ?)"
    else:#                      MySQL
        query +=  "VALUES(%s,%s,%s,%s)"

    """
SQLite         VALUES( ?, ?, ?, ?)"
MySQL          VALUES(%s,%s,%s,%s)"
    """
    #   query = f"""INSERT INTO  {nombre_tabla_productos}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) VALUES(?,?,?,?);"""
    #   query = f"""INSERT INTO  {nombre_tabla_productos}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) VALUES(%s,%s,%s,%s);"""
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
    # ~ cursor.execute(query,proy)
    # ~ connection.commit()
    pausa()
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

    try:
        print             (query,proy)
        cursor.executemany(query,proy)# ~ cursor.execute(query,datos) + many --->SQL no python
    except Exception as error_sql:
        print (f"hay un error {error_sql}")
    connection.commit()
    print(cursor.rowcount, "record inserted in pool.")
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
        dato_fecha_str = dato_fecha.isoformat()

        # Ejecutar la consulta con la fecha convertida
        cursor.execute(query, (dato_desc, dato_precio, dato_codigo, dato_fecha_str))# sqlite3 o  MySql
        connection.commit()
        print(cursor.rowcount, "record inserted.")
######################################################################################################
def leer_tabla():
    pausa()
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
║                      leemos todos los datos de {nombre_tabla_productos}                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    cursor = conectar_base_de_datos()#           sqlite // mysql
    print(f"ME TRAIGO 'TODA' LA BASE DE DATOS")
    query = f"SELECT * FROM {nombre_tabla_productos}; "
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    for linea in datos_desde_sql:
        print (linea)
    pausa()
    print(f"""
    LUEGO CON 'TODA' LA BASE DE DATOS CARGADA EN PYTHON
    SELECCIONA SOLO CODIGO 'A1'""")
    for linea in datos_desde_sql:
        if str(linea[3]).upper()=="A1":
            print ("dato: ",linea)
    pausa()
    limpiar()

    query = f"SELECT * FROM {nombre_tabla_productos} WHERE {nombre_columna_3} = 'A1'"
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    print(f" ME TRAIGO SOLO CODIGO 'A1' DE LA BASE DE DATOS")
    print(f"{query=}")
    for linea in datos_desde_sql:
        print ("dato: ",linea)

    pausa()
    limpiar()

    print(f" ME TRAIGO SOLO DESCRIPCIÓN QUE EN ALGUN LADO CONTENGA 'A' DE LA BASE DE DATOS")
    query = f"SELECT * FROM {nombre_tabla_productos} WHERE {nombre_columna_3} LIKE '%A%'"
    cursor.execute(query)
    #print (cursor,type(cursor), dir (cursor))
    datos_desde_sql = cursor.fetchall()
    print(f"{query=}")
    print("A.....")
    for linea in datos_desde_sql:
        print ("dato: ",linea)

    pausa()
    limpiar()
    print(f" ME TRAIGO SOLO DESCRIPCIÓN QUE TERMINE CON 'A' DE LA BASE DE DATOS")
    query = f"SELECT {nombre_columna_2} FROM {nombre_tabla_productos} WHERE {nombre_columna_1} LIKE '%A'"
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

    query = "SELECT * FROM {nombre_tabla_productos} WHERE '' "
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

    query ="SELECT * FROM {nombre_tabla_productos} "
    query ="SELECT * FROM {nombre_tabla_productos} WHERE precio BETWEEN 10 AND  100 and codigo like '%Z' "
    query ="SELECT * FROM {nombre_tabla_productos} WHERE codigo IN 'H2O','S1','A1' "
    query ="SELECT * FROM {nombre_tabla_productos} WHERE codigo like '%H%' "
    inicio = input ("INgrese las primeras letras del producto a buscar:")
    inicio = inicio +"%"
    '''

    inicio = "A%"
    query =(f"SELECT * FROM {nombre_tabla_productos} WHERE descripcion like '{inicio}' ")
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

    query = f"UPDATE {nombre_tabla_productos} SET {nombre_columna_3} = 'T_lta' WHERE {nombre_columna_1} = 'Tomates' "
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
    query = f"DELETE FROM {nombre_tabla_productos}  WHERE {nombre_columna_1} = 'Sal'"# and {columna2} = '{dato2}'
    cursor.execute(query )
    print(cursor.rowcount, "record(s) affected")
    query = f"DELETE FROM {nombre_tabla_productos}  WHERE {nombre_columna_1} = "

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
        query= f"DROP TABLE IF EXISTS  {nombre_tabla_productos}"
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
            cursor.execute(f"DROP DATABASE IF EXISTS {nombre_DDBB}")
            cursor.close()
            connection.close()
            print (f"base de datos  {nombre_DDBB} eliminada ")
        except Exception as Error:
            print (f"base de datos  {nombre_DDBB} no se pudo eliminar por la excepcion:\n {Error} ")
    pausa()
######################################################################################################
    limpiar()
import openpyxl
import random
def pack2_tablas():
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
║                      leemos todos los datos de {nombre_tabla_productos}                     ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    
    # ~ vista_nombre = "vista"
    cursor = conectar_base_de_datos()#           sqlite // mysql
    if base_de_datos == "S":#   SQLite
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    else:#                      MySQL
        cursor.execute("SHOW TABLES;")
    tablas = cursor.fetchall()
    print ("tablas en base de datos:")
    for tabla in tablas:
        print(f"\t{tabla[0]}")
    pausa()
    #---------------------------------------------------------------------------------------
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
    limpiar()
    cursor = conectar_base_de_datos()#           sqlite // mysql

    print(f"""{Fore.WHITE+Back.BLUE}
    ╔═════════════════════════════════════════════════════════════════════════════╗
    ║                                                                             ║
    ║   para no tener problemas con lo anteriro borramos la tabla de la base I    ║
    ║                                                                             ║
    ║                   e insertamos los datos nuevamente                         ║
    ║                                                                             ║
    ╚═════════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}""")
    try:
        query= f"DROP TABLE IF EXISTS  {nombre_tabla_productos}"
        print                           (query)
        resultado=cursor.execute        (query)

        print ("cursor.execute:",resultado)
        print(cursor.rowcount, "record(s) affected")
        print (f"tabla  {nombre_tabla_productos} eliminada ")
    except Exception as Error:
        print (f"tabla  {nombre_tabla_productos} no se pudo eliminar por la excepcion:\n {Error} ")
    
    query = (f"""CREATE TABLE IF NOT EXISTS {nombre_tabla_productos} (
                                                            {nombre_columna_1} TEXT NOT NULL,
                                                            {nombre_columna_2} FLOAT,
                                                            {nombre_columna_3} VARCHAR(255) PRIMARY KEY NOT NULL,
                                                            {nombre_columna_4} DATE )""")

    if base_de_datos == "M":#   MySQL
        query =  query.replace("AUTOINCREMENT","AUTO_INCREMENT").replace("INTEGER","INT")#.replace("TEXT","VARCHAR (255)")
    print (f"query={query}")
    cursor.execute(query)
    
    

    query = f"""INSERT INTO  {nombre_tabla_productos}  ({nombre_columna_1}, {nombre_columna_2}, {nombre_columna_3}, {nombre_columna_4}) """
    if base_de_datos == "S":#   SQLite
        query +=  "VALUES( ?, ?, ?, ?)"
    else:#                      MySQL
        query +=  "VALUES(%s,%s,%s,%s)"

    """
SQLite         VALUES( ?, ?, ?, ?)"
MySQL          VALUES(%s,%s,%s,%s)"
    """

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

    try:
        print             (query,proy)
        cursor.executemany(query,proy)# ~ cursor.execute(query,datos) + many --->SQL no python
    except Exception as error_sql:
        print (f"hay un error {error_sql}")
    connection.commit()
    query= f"""
            CREATE TABLE IF NOT EXISTS {nombre_tabla_stock} (cantidad INT ,
                                                            codigo_producto VARCHAR(255),
                                                            FOREIGN KEY (codigo_producto) REFERENCES {nombre_tabla_productos}(codigo)
                )"""
    if base_de_datos == "M":#   MySQL
        query =  query.replace("AUTOINCREMENT","AUTO_INCREMENT").replace("INTEGER","INT")#.replace("TEXT","VARCHAR (255)")
    print (f"query={query}")
    cursor.execute(query)

    print (f"{query=}")
    pausa()
    print(cursor.rowcount, "record(s) affected")
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
    #---------------------------------------------------------------------------------------
    # Insertar datos de stock con cantidades aleatorias (suponiendo que ya existen productos)
    cursor.execute(f"SELECT codigo FROM {nombre_tabla_productos}")
    productos = cursor.fetchall()

    print (f"{productos}")
    pausa()
    for producto in productos:
        codigo = producto[0]
        
        cantidad = random.randint(1, 100)  # Genera una cantidad aleatoria entre 1 y 100
        print (f"{codigo=} - {cantidad=} ")
        query= (f"""
            INSERT OR IGNORE INTO {nombre_tabla_stock} (codigo_producto, cantidad)      VALUES (?, ?)  """)#cambiar si es mysql
        """---------------------------------------------------------------------------------------------------------------------
                    SQLite                                      INSERT OR IGNORE INTO
                    MySQL                                       INSERT IGNORE INTO
                                                                      ^
                                                                      |_ OR solo en sqlite
        """
        if base_de_datos == "M":#   MySQL
            query =  query.replace("INSERT OR","INSERT").replace("?","%s")
        print (f"{query}")
        cursor.execute(query, (codigo, cantidad))
        connection.commit()
        print(cursor.rowcount, "record(s) affected")
    print(cursor.rowcount, "record(s) affected")
    pausa()
    #---------------------------------------------------------------------------------------
    limpiar()

    cursor = conectar_base_de_datos()#           sqlite // mysql
    query = f"""
                CREATE TABLE IF NOT EXISTS {nombre_tabla_proveedores} (
                                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                        nombre VARCHAR(255) NOT NULL,
                                                        email VARCHAR(255) NOT NULL,
                                                        direccion TEXT,
                                                        telefono VARCHAR(20),
                                                        codigo_producto VARCHAR(255),
                                                        FOREIGN KEY (codigo_producto) REFERENCES {nombre_tabla_productos}(codigo)
                )"""
    if base_de_datos == "M":#   MySQL
        query =  query.replace("INTEGER","INT").replace("AUTOINCREMENT","AUTO_INCREMENT")
    cursor.execute(query)
    print (f"{query}")
    connection.commit()
    connection.close()
    pausa()
######################################################################################################
    limpiar()
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
    nombre_tabla_stock = "stock"
    try:
        query=f"DROP VIEW IF EXISTS {vista_nombre}"
        cursor.execute(query)
    except Exception as error_:
        print (f"la vista no existe {error_}")
    if base_de_datos == "S":
        query=f"""CREATE VIEW IF NOT EXISTS {vista_nombre} AS"""
    else:
        query=f"""CREATE VIEW {vista_nombre} AS"""
    query += f"""
                SELECT p.codigo AS codigo, p.precio, s.cantidad AS stock
                FROM {nombre_tabla_productos} p
                JOIN {nombre_tabla_stock} s ON p.codigo = s.codigo_producto"""
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
    cursor.execute(query)
    connection.commit()
    
    nombre_tabla_stock = "stock"
    # ~ vista_nombre = "vista"
    cursor.execute(f"SELECT * FROM {vista_nombre};")
    datos_en_vista = cursor.fetchall()
    print (f"{datos_en_vista}")
    pausa()
    
    connection.close()
    pausa()
######################################################################################################
    limpiar()
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
    cursor = conectar_base_de_datos()#           sqlite // mysql
    # Exportar datos de la vista a un archivo Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Datos de Stock"

    # Escribir los encabezados
    ws.append(["codigo_producto", "precio", "stock"])

    # Escribir los datos
    cursor.execute(f"SELECT * FROM {vista_nombre}")
    filas = cursor.fetchall()

    #----------------------------------------

    # ~ agregar columna total (stock x precio)

    #----------------------------------------
    for fila in filas:
        ws.append(fila)
        print (f"{fila=}")

    # Guardar el archivo Excel
    wb.save("datos_stock.xlsx")

    # Cerrar la conexión
    connection.commit()
    connection.close()
    print("Datos exportados buscar en la carpeta 'datos_stock.xlsx'")
    pausa()
    #---------------------------------------------------------------------------------------
    limpiar()

############################################################################################
############################################################################################
############################################################################################

def crear_procedimiento_obtener_stock():
    try:
        # Conexión a la base de datos MySQL
        cursor = conectar_base_de_datos()#           sqlite // mysql
        if base_de_datos == "S":
            # Seleccionar productos con stock bajo
            cursor.execute("""
                                SELECT codigo_producto, cantidad
                                FROM stock
                                WHERE cantidad <= 20
                            """)# -- Puedes ajustar este valor a lo que consideres "stock bajo"
            # Obtener los resultados
            stock_bajo = cursor.fetchall()
            # Mostrar el listado de productos con stock bajo
            if stock_bajo:
                print("Listado de productos con stock bajo:")
                for codigo, cantidad in stock_bajo:
                    print(f"Código: {codigo}, Cantidad: {cantidad}")
            else:
                print("No hay productos con stock bajo.")
        else:
            # Crear el procedimiento almacenado en MySQL
            procedimiento = """
            CREATE PROCEDURE ObtenerStockBajo()
            BEGIN
                SELECT codigo_producto, cantidad
                FROM stock
                WHERE cantidad <= 20;  -- Puedes ajustar este valor a lo que consideres "stock bajo"
            END
            """
            cursor.execute(procedimiento)
            print("Procedimiento almacenado 'ObtenerStockBajo' creado exitosamente.")


        # Commit para confirmar los cambios en la base de datos
        connection.commit()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    except sqlite3.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
    pausa()
    #---------------------------------------------------------------------------------------
    limpiar()

############################################################################################
def obtener_stock_bajo():
    try:
        # Conexión a la base de datos MySQL
        cursor = conectar_base_de_datos()#           sqlite // mysql

        # Ejecutar el procedimiento almacenado
        cursor.callproc('ObtenerStockBajo')

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

    except Exception as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()
    pausa()
    #---------------------------------------------------------------------------------------
    limpiar()

############################################################################################
############################################################################################
############################################################################################
############################################################################################
############################################################################################


opcion = ""
dic_datos ={}
nombre_DDBB      = "it_bbdd_2025_12"
nombre_tabla_productos     = "productos"
nombre_columna_1 = "descripcion"
nombre_columna_2 = "precio"
nombre_columna_3 = "codigo"
nombre_columna_4 = "vencimiento"
nombre_tabla_stock = "stock"
vista_nombre = "vista"
nombre_tabla_proveedores= "proveedores"
nombre_tabla=""
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

    print(f"""{Fore.WHITE+Back.BLUE+cartel+Style.RESET_ALL}""")
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
    13) obtener_stock_bajo
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
            obtener_stock_bajo()
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



