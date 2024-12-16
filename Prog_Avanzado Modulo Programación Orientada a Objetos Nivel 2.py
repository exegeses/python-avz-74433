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
# ~ nuevo(0,estado='inicio',modulo=4)
import math
import datetime

####################################################################################################
#                                                                                                  #
#                                        Bases de datos                                            #
#                                                                                                  #
####################################################################################################

print(F'''{Fore.WHITE+Back.BLUE}
╔═════════════════════════════════════════════════════════════════════════════╗
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

def ya_hechos():
    obj = 9
    if isinstance(obj, int):
        print(f"{obj=} pertenece a la clase int")
    else:
        print(f"{obj=} NO pertenece a la clase int")
    print("*"*50)
    #····································································#
    obj = 9.5
    if isinstance(obj, int):
        print(f"{obj=} pertenece a la clase int")
    else:
        print(f"{obj=} NO pertenece a la clase int")
    print("*"*50)
    #····································································#
    obj = 9.5
    if isinstance(obj, (int,float)):#la coleccion de clases solo puede ser tupla (no listas))
        print(f"{obj=} pertenece a la clase int o float")
    else:
        print(f"{obj=} NO pertenece a las clases int ni float")
    print("*"*50)
    #····································································#


#####################################################################################################
    class MiPrimerClase:
        ingreso=1
        def __init__(self,nombre,apellido,titulo=""):
            self.gracia = f"{titulo}.{apellido},{nombre}".title()
            print(f"objeto '{MiPrimerClase.ingreso}' creado")
            MiPrimerClase.ingreso+=1
        def info(self):
            print (f"{self.gracia=}")
    #····································································#
    print("*"*50)
    obj=MiPrimerClase("juan","perez","ing")
    #····································································#
    print("*"*50)
    obj.info()
    print("*"*50)

    print (f"obj tiene el atributo/método gracia {hasattr(obj,'gracia')=}")
    print (f"obj tiene el atributo/método ingreso {hasattr(obj,'ingreso')=}")
    print (f"obj tiene el atributo/método info {hasattr(obj,'info')=}")
    print (f"obj tiene el atributo/método salida {hasattr(obj,'salida')=}")

    #····································································#
    print (f"Desde el obj contenido del atributo gracia {getattr(obj,'gracia')=}")
    print (f"Desde el obj contenido del atributo ingreso {getattr(obj,'ingreso')=}")
    #····································································#
    print("*"*50)
    #print (f"Desde el obj contenido del atributo salida {getattr(obj,'salida')=}")
    # obj, no tiene el atributo salida. Al no tener 3er parámetro da error
    print (f"Desde el obj contenido del atributo gracia  {getattr(obj,'salida', 'sin atributo ')=}")
    # obj, no tiene el atributo salida. Al si tener 3er parámetro lo imprime 'sin atributo
    print("*"*50)
    #····································································#
    print (f"Desde el obj contenido del atributo gracia {getattr(obj,'info')=}")#método, no atributo
    print("*"*50)

    setattr (obj,'ingreso',55)
    setattr (obj,'gracia',"Dra. Ana Maria")
    print (f"Desde el obj contenido del atributo gracia {getattr(obj,'gracia')=}")
    print (f"Desde el obj contenido del atributo gracia {getattr(obj,'ingreso')=}")
    print (f"Desde el obj contenido del atributo ingreso {getattr(MiPrimerClase,'ingreso')=}")

    #####################################################################################################
    class MiPrimerClase:
        ingreso=1
        def __init__(self,nombre,apellido,titulo=""):
            self.gracia = f"{titulo}.{apellido},{nombre}".title()
            print(f"objeto '{MiPrimerClase.ingreso}' creado")
            MiPrimerClase.ingreso+=1
        def info(self):
            print (f"{self.gracia=}")
    #····································································#
    print("*"*50)
    obj=MiPrimerClase("juan","perez","ing")
    #····································································#
    print("*"*50)
    obj.info()
    print("*"*50)
    # ~ setattr (obj,'ingreso',55)
    # ~ setattr (obj,'gracia',"Dra. Ana Maria")
    # ~ print("*"*50)
    print (f"Desde el obj contenido del atributo gracia {hasattr(obj,'gracia')=}")
    print (f"Desde el obj contenido del atributo gracia {hasattr(obj,'ingreso')=}")
    #····································································#
    print("*"*50)
    delattr (obj,'gracia')
    #····································································#
    print("*"*50)
    print (f"Desde el obj contenido del atributo gracia {hasattr(obj,'gracia')=}")
    #····································································#
    print("*"*50)
    delattr (MiPrimerClase,'ingreso')
    #····································································#
    print("*"*50)
    print (f"Desde el obj contenido del atributo ingreso {hasattr(obj,'ingreso')=}")
    print (f"Desde el obj contenido del atributo ingreso {hasattr(MiPrimerClase,'ingreso')=}")
    #····································································#
    print("*"*50)
    exit()
#####################################################################################################


    #····································································#
    for valor in range (1,10):
        obj=MiPrimerClase(f"juan{valor}",f"perez{valor}",f"ing{valor}")
    print("*"*50)
    #····································································#
    print (f"total de alumnos: {MiPrimerClase.ingreso}")
    print("*"*50)
    #····································································#
    #####################################################################################################

    class MiPrimerClase:
        ingreso=1

        def contador_personas( no_importa ):
            MiPrimerClase.ingreso +=1
            print (f"desde adentro de la clase: total de personas ingresadas {MiPrimerClase.ingreso}" )

    #····································································#
    print("*"*50)
    obj1=MiPrimerClase()
    obj1.contador_personas()
    #····································································#
    print("*"*50)
    obj2=MiPrimerClase()
    obj2.contador_personas()
    #····································································#
    print("*"*50)
    obj3=MiPrimerClase()
    obj3.contador_personas()
    #····································································#
    print("*"*50)
    obj4=MiPrimerClase()
    obj4.contador_personas()
    #····································································#
    print("*"*50)
    print (f"desde afuera de la clase: total de personas ingresadas {MiPrimerClase.ingreso}" )

    exit()


    #####################################################################################################

    class MiPub:
        edad=1
        nombre =""
        def entrada( quien ):
            print (f"{quien.edad=}")
            if quien.edad >=18:
                print (f"Bienvenido {quien.nombre}" )
            else:
                print (f"Lamentablemente {quien.nombre}, no puedo dejarte entras o me clausura la muni" )
    #····································································#
    print("*"*50)
    Juan=MiPub()
    Juan.nombre="Juan Manuel"
    Juan.edad=20
    Juan.entrada()
    #····································································#
    print("*"*50)
    Ana=MiPub()
    Ana.nombre="Ana Manuela"
    Ana.edad=25
    Ana.entrada()
    #····································································#
    print("*"*50)
    Luca=MiPub()
    Luca.nombre="Luca Garcia"
    Luca.edad=18
    Luca.entrada()
    #····································································#
    print("*"*50)
    Luli=MiPub()
    Luli.nombre="Luciana De Maria"
    Luli.edad=15
    Luli.entrada()
    #····································································#
    print("-"*50)
    Juan.entrada()
    Ana.entrada()
    Luca.entrada()
    Luli.entrada()
    print("-"*50)


    exit()

    print("*"*50)
    #####################################################################################################

    class MiPub:
        def __init__ (self,nombre,edad):
            self.nombre =nombre.upper()
            self.edad=round(edad)
        def entrada( self ):
            print (f"{self.edad=}")
            if self.edad >=18:
                print (f"Bienvenido {self.nombre}" )
            else:
                print (f"Lamentablemente {self.nombre}, no puedo dejarte entras o me clausura la muni" )
    #····································································#
    print("*"*50)
    Juan=MiPub(nombre="Juan Manuel",edad=20)
    Juan.entrada()
    #····································································#
    print("*"*50)
    Ana=MiPub(edad=25,nombre="Ana Manuela")
    Ana.entrada()
    #····································································#
    print("*"*50)
    Luca=MiPub("Luca Garcia",18)
    Luca.entrada()
    #····································································#
    print("*"*50)
    Luli=MiPub("Luciana De Maria",15)
    Luli.entrada()
    #····································································#
    print("-"*50)
    Juan.entrada()
    Ana.entrada()
    Luca.entrada()
    Luli.entrada()
    print("-"*50)
    objetos=[["Juan Manuel",20],["Ana Manuela",25],["Luca Garcia",18],["Luciana De Maria",15]]
    lista_objetos= []
    dic_objetos  = {}
    for nombre,edad in objetos:
        obj = MiPub(nombre,edad)
        lista_objetos.append(obj)
        dic_objetos[obj]=nombre
        print (f"objeto {obj}-{nombre=} creado")
    for objetos_desde_coleccion in dic_objetos.keys():
    #for objetos_desde_coleccion in lista_objetos:
        print("*"*50)
        objetos_desde_coleccion.entrada()
    exit()
    print("*"*50)

    #####################################################################################################

    class MiPub:
        objetos=[["Juan Manuel",20],["Ana Manuela",25],["Luca Garcia",18],["Luciana De Maria",15]]
        lista_objetos= []

        def __init__ (self,nombre,edad):
            self.nombre =nombre.upper()
            self.edad=round(edad)
            self.donde=False
        def __del__ (self):
            print ("+"*50)
            print (f"fue un gusto {self.nombre}. Adios")
        def entrada( self ):
            print (f"{self.edad=}")
            if self.edad >=18:
                print (f"Bienvenido {self.nombre}" )
                self.donde=True
            else:
                print (f"Lamentablemente {self.nombre}, no puedo dejarte entras o me clausura la muni" )
                self.donde=False

        def estado(self):
            if self.donde is True:
                print (f"{self.nombre} esta en el pub")
            else:
                print (f"{self.nombre} no se encuentra aqui")
    print("-"*50)


    #                   carga
    print("carga".center(40))
    for nombre,edad in MiPub.objetos:
        obj = MiPub(nombre,edad)
        MiPub.lista_objetos.append(obj)
        #dic_MiPub.objetos[obj]=nombre
        print (f"objeto {obj}-{nombre=} creado")

    #                   entrada
    print("estrada".center(40))
    for objetos_desde_coleccion in MiPub.lista_objetos:
        print("*"*50)
        objetos_desde_coleccion.entrada()
    #                   salida
    print("del".center(40))
    for objetos_desde_coleccion in MiPub.lista_objetos[::2]:
        MiPub.lista_objetos.remove(objetos_desde_coleccion)
        del objetos_desde_coleccion
    #                   estado
    print("estado".center(40))
    for objetos_desde_coleccion in MiPub.lista_objetos:
        print("*"*50)
        objetos_desde_coleccion.estado()
    #                   fin
    print("fin".center(40))
    exit()
    print("*"*50)
    #####################################################################################################
    class MiClase:
        def trabajo(self, a, b):
            resultado = a - b
            return resultado
    obj = MiClase()

    resultado = obj.trabajo(10, 3)
    print(f"Resultado original: {resultado}")
    resultado = obj.trabajo(3, 10)
    print(f"Resultado original: {resultado}")
    print ("creo el nuevo método")
    def trabajo_mejorado(self, a, b):
        if a > b:
            resultado = a - b
        elif a < b:
            resultado = b - a
        else:
            resultado = 0
        return resultado
    print ("asigno y sobreescribo el método original con el nuevo método")
    MiClase.trabajo = trabajo_mejorado
    resultado = obj.trabajo(10, 3)
    print(f"Resultado nuevo método: {resultado}")
    resultado = obj.trabajo(3, 10)
    print(f"Resultado nuevo método: {resultado}")
    exit()
    print("*"*50)
    #####################################################################################################
    class MiPub:
        def __init__ (self,nombre,edad):
            self.nombre =nombre.upper()
            self.edad=round(edad)
            print (f"objeto {self}-{self.nombre } creado")
        # ~ def entrada( self ):
            # ~ print (f"{self.edad=}")
            # ~ if self.edad >=18:
                # ~ print (f"Bienvenido {self.nombre}" )
            # ~ else:
                # ~ print (f"Lamentablemente {self.nombre}, no puedo dejarte entras o me clausura la muni" )

        @property
        def donde(self):
            print ("en property")
            if self.nombre is None:
                salida = f" {self.nombre} no han ingresado al pub"
            else:
                salida = f" {self.nombre} se esta diviertiendo en el pub ({self.edad})"
            return salida
        @donde.setter
        def donde(self,datos):
            print ("en setter")
            self.nombre =datos[0].upper()
            self.edad=round(datos[1])
        @donde.deleter
        def donde(self):
            print (f"en deleter adios {self.nombre}")
            del self


    objetos=[["Juan Manuel",20],["Ana Manuela",25],["Luca Garcia",18],["Luciana De Maria",15]]
    lista_objetos= []
    #------------------------------------------------------------------
    print ("carga original".center(40))
    for nombre,edad in objetos:
        obj = MiPub(nombre,edad)
        lista_objetos.append(obj)
    #------------------------------------------------------------------
    print ("mostrar todo lo cargado".center(40))
    for obj in lista_objetos:
        print (f"{obj.donde}")
    #------------------------------------------------------------------

    print("*"*50)
    print ("carga nuevo".center(40))
    obj=MiPub("Pancho",99)
    lista_objetos.append(obj)
    #------------------------------------------------------------------

    print("*"*50)
    print ("mostrar todo lo cargado".center(40))
    for obj in lista_objetos:
        print (f"{obj.donde}")
    #------------------------------------------------------------------


    print("*"*50)
    print ("renombrar con setter".center(40))
    print (lista_objetos[-1])
    datos = ("Francisco",19)
    lista_objetos[-1].donde=(datos)
    #------------------------------------------------------------------

    print("*"*50)
    print ("mostrar todo lo cargado".center(40))
    print(f"{lista_objetos}")
    for obj in lista_objetos:
        print (f"{obj.donde}")
    #------------------------------------------------------------------
    print("*"*50)
    for obj in lista_objetos[::2]:
        del obj.donde
        lista_objetos.remove(obj)

    print("*"*50)
    print ("mostrar todo lo cargado".center(40))
    print(f"{lista_objetos}")
    for obj in lista_objetos:
        print (f"{obj.donde}")


    exit()


    print("*"*50)
    #####################################################################################################
    import time
    class MiClase:
        _formatos_de_fechas={"aaaammdd":"{fecha.año}-{fecha.mes}-{fecha.dia}",
                             "ddmmaaaa":"{fecha.dia}-{fecha.mes}-{fecha.año}",
                             "mmddaaaa":"{fecha.mes}-{fecha.dia}-{fecha.año}"
                            }
        def __init__(self,año,mes,dia):#constructor
            self.año=año
            self.mes=mes
            self.dia=dia
        def __repr__(self):
            salida = f"fecha:  {self.dia} de {self.mes} de {self.año} "
            return salida
        def __str__(self):
            salida = f"a los {self.dia} dias del mes {self.mes} del año {self.año} "
            return salida
        def __format__ (self,codigo):
            codigo=codigo.lower()
            if codigo == "":
                codigo="ddmmaaaa"

            if codigo in MiClase._formatos_de_fechas.keys():
                fecha_formateada = self._formatos_de_fechas[codigo]
                salida = fecha_formateada.format(fecha=self)

            else:
                return (":sin datos")
            return salida

        def hoy ():
            today = time.localtime()
            return MiClase(today.tm_year,today.tm_mon,today.tm_mday)
    obj = MiClase(1969,7,16)
    print (f"salida desde clase {obj}")

    print (f"salida con formato ddmmaaaa {format(obj,'ddmmaaaa')}")
    print (f"salida con formato mmddaaaa {format(obj,'mmddaaaa')}")
    print (f"salida con formato aaaammdd {format(obj,'aaaammdd')}")
    print ("*"*50)
    obj_hoy = MiClase.hoy()
#------------------------------------------------------------------
    print (f"salida con formato ddmmaaaa {format(obj_hoy,'ddmmaaaa')}")
    print (f"salida con formato mmddaaaa {format(obj_hoy,'mmddaaaa')}")
    print (f"salida con formato aaaammdd {format(obj_hoy,'aaaammdd')}")
    exit()
    print("*"*50)
    #####################################################################################################
    class MiClase:
        def __init__(self, valor):
            self.valor = valor
        def __add__(self, new_self):
            return MiClase(self.valor + new_self.valor)
        def __sub__(self, new_self):
            return MiClase(self.valor - new_self.valor)
        def __mul__(self, new_self):
            return MiClase(self.valor * new_self.valor)
        def __truediv__(self, new_self):
            if new_self.valor == 0:
                print ("error")
                return MiClase(new_self.valor)
            return MiClase(self.valor / new_self.valor)

    num_1ro = MiClase(9)
    num_2do = MiClase(2)
    #------------------------------------------------------------------
    resultado = num_1ro + num_2do  #con + llama al  metodo  __add__ para sumar los objetos
    print (f"{num_1ro.valor}+{num_2do.valor}={resultado.valor}")
    print ("-"*50)
    #------------------------------------------------------------------
    resultado = num_1ro - num_2do  #con - llama al  metodo  __sub__ para restar los objetos
    print (f"{num_1ro.valor}-{num_2do.valor}={resultado.valor}")
    print ("-"*50)
    #------------------------------------------------------------------
    resultado = num_1ro * num_2do  #con * llama al  metodo  __sub__ para multiplicar los objetos
    print (f"{num_1ro.valor}*{num_2do.valor}={resultado.valor}")
    print ("-"*50)
    #------------------------------------------------------------------
    resultado = num_1ro / num_2do  #con / llama al  metodo  __truediv__ para dividir los objetos
    print (f"{num_1ro.valor}/{num_2do.valor}={resultado.valor}")
    print ("-"*50)
    #------------------------------------------------------------------
    num_2do = MiClase(0)
    #------------------------------------------------------------------
    resultado = num_1ro / num_2do  #con / llama al  metodo  __truediv__ para dividir los objetos
    print (f"{num_1ro.valor}/{num_2do.valor}={resultado.valor}")
    print ("-"*50)
    #------------------------------------------------------------------
    #####################################################################################################


class MiClase:
    def __init__(self, valor):
        self.valor = valor
    def __add__(self, new_value):
        if isinstance (self ,MiClase) and isinstance (new_value ,MiClase):
            salida = MiClase(self.valor + new_value.valor).valor
            print ("obj+obj")
        elif isinstance (self ,MiClase) and isinstance (new_value ,(int,float)):
            salida = MiClase(self.valor + new_value)
            print ("obj+valor")
        else:
            exit()
            raise "Error"
        return  salida

    def __radd__(self, new_value):
        print ("valor+obj")
        salida = MiClase(self.valor + new_value)
        return  salida


num_1ro = MiClase(9)
num_2do = MiClase(2)
#------------------------------------------------------------------
resultado = num_1ro + num_2do  #con + llama al  metodo  __add__ para sumar los objetos
print (f"{num_1ro.valor}+{num_2do.valor}={resultado}")
print ("-"*50)
#------------------------------------------------------------------
num_2do=8
resultado = num_1ro + num_2do
print (f"{num_1ro.valor}+{num_2do}={resultado.valor}")
print ("-"*50)
#------------------------------------------------------------------

num_1ro = 8
num_2do = MiClase(2)
resultado = num_1ro + num_2do
print (f"{num_1ro}+{num_2do.valor}={resultado.valor}")
print ("-"*50)
#------------------------------------------------------------------

"""
class MiClase:
    caja=0
    def __init__(self,nombre,socio):
        self.nombre = nombre
        self.socio  = socio
    def cobro(self):
        if self.socio is True:
            print ("debe abonar $1 - bono de ingreso al socio")
            self.entrada+=1
        else:
            print ("debe abonar $5 - Ticket de ingreso para no socios")
            self.entrada+=5
        return
    def __add__ (self,nombre):
        if self.nombre.upper()
"""


exit()

"""
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self.__edad = edad     # Atributo privado

    def obtener_nombre(self):
        return self._nombre

    def cambiar_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def obtener_edad(self):
        return self.__edad

    def cambiar_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad

persona = Persona("Pepe", 25)
print(f"{persona.obtener_nombre()=}")   # Acceso a través de método público
persona.cambiar_nombre("Ana")           # Modificación a través de método público
print(f"{persona.obtener_edad()=}")     # Acceso a través de método público
persona.cambiar_edad(22)                # Modificación a través de método público
print (f"{persona.__dict__}")


class MiPrimerClase:
    ingreso=1
    def __init__(self,nombre,apellido,titulo=""):
        self.gracia = f"{titulo}.{apellido},{nombre}".title()
        print(f"objeto '{MiPrimerClase.ingreso}' creado")
        MiPrimerClase.ingreso+=1
    def info(self):
        print (f"{self.gracia=}")

    def contador_personas(x):
        print (f"fdesde adentro de la clase: total de personas ingresadas {ingreso}" )

#····································································#
print("*"*50)
obj=MiPrimerClase("Ana","Marcos","Dra")
#····································································#
print("*"*50)
obj=MiPrimerClase("Juan","Perez","tecnico")
#····································································#
print("*"*50)
obj=MiPrimerClase("Luciana","Garcia","lic")
#····································································#
print("*"*50)
obj=MiPrimerClase("Andres","Gomez","ing")
#····································································#
print("*"*50)
print (f"fdesde afuera de la clase: total de personas ingresadas {ingreso}" )
contador_personas




class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo protegido
        self.__edad = edad     # Atributo privado

    def obtener_nombre(self):
        return self._nombre

    def cambiar_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def obtener_edad(self):
        return self.__edad

    def cambiar_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.__edad = nueva_edad

persona = Persona("Pepe", 25)
print(f"{persona.obtener_nombre()=}")   # Acceso a través de método público
persona.cambiar_nombre("Ana")           # Modificación a través de método público
print(f"{persona.obtener_edad()=}")     # Acceso a través de método público
persona.cambiar_edad(22)                # Modificación a través de método público
print (f"{persona.__dict__}")

exit()


class Objeto(object):
    def __init__(self, nombre, privado):
        self.nombre = nombre
        self.__privado = privado
    def comer(self):
        print("me hicieron dar ganas de pizza")
    def _xx(self):
        print("salida con _xx")
    def __yy(self):
        print("salida con __yy")
Objeto.comer(1)
print ("dic:",dir(Objeto))
print ("dict:",Objeto.__dict__)
objeto_1 = Objeto("Pepe", "canta en la ducha")
print ("Atributo privado:", objeto_1._Objeto__privado)
objeto_1._Objeto__privado = "no se baña"
print ("Atributo privado:", objeto_1._Objeto__privado)

objeto_1._xx()
objeto_1._Objeto__yy()








exit()
class MiClase:

    __mi_atributo = ""
    def __mi_metodo(self, parametros):
        print (f"{ __mi_atributo=} ")
        print (f"{parametros=} ")
objeto= MiClase()
objeto__mi_metodo = 99
objeto.MiClase.__mi_metodo(88)
exit()


class MiClase:
    contador = 0

    def __init__(self):
        MiClase.contador += 1

    @classmethod
    def obtener_contador(cls):
        return cls.contador

objeto1 = MiClase()
objeto2 = MiClase()
print(f"{MiClase.obtener_contador()=}")


exit()


class MiClase:
    def __init__(self, valor):
        self.valor = valor

    def imprimir_valor(self):
        print(f"{self.valor=}")

objeto = MiClase(42)
objeto.imprimir_valor()

exit()












class MiClase:
    def _metodo_protegido(self):
        print("Este es un método protegido.")

class SubClase(MiClase):
    def otro_metodo(self):
        self._metodo_protegido()  # Accediendo al método protegido desde la subclase

objeto = SubClase()
objeto.otro_metodo()

MiClase_metodo_protegido("x")
exit()





class Contador:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def __iter__(self):
        return self

    def __next__(self):
        if self.inicio >= self.fin:
            raise StopIteration
        actual = self.inicio
        self.inicio += 1
        return actual

contador = Contador(1, 11)
iterador = iter(contador)

print(f"1 {next(iterador)=}")
print(f"2 {next(iterador)=}")
print(f"3 {next(iterador)=}")
print(f"4 {next(iterador)=}")
print(f"5 {next(iterador)=}")

for num in iterador:
    print(f"next(iterador) = {num=}") # 6 a 10

exit()





def numeros_pares(maximo):
    num = 0
    while num < maximo:
        yield num
        num += 2

generador = numeros_pares(11)
print(f"1 {next(generador)=}")
print(f"2 {next(generador)=}")
print(f"3 {next(generador)=}")
print(f"4 {next(generador)=}")
print(f"5 {next(generador)=}")
print(f"6 {next(generador)=}")
print(f"7 {next(generador)=}")
exit()




nombres = ["Juan","María","Ana","Lucas","Luis", "Ariel"]
iterador_nombres = iter(nombres)

print(f"1 {next(iterador_nombres)=}")
print(f"2 {next(iterador_nombres)=}")
print(f"3 {next(iterador_nombres)=}")
print(f"4 {next(iterador_nombres)=}")
print(f"5 {next(iterador_nombres)=}")
print(f"6 {next(iterador_nombres)=}")
print(f"7 {next(iterador_nombres)=}")

exit()


def generador_pares(maximo):
    num = 0
    while num < maximo:
        yield num
        num += 2
gen = generador_pares(11)
for numero in gen:
    print(f"{numero=}")


exit()





mi_lista = [1, 2, 3, 4, 5]
iterador = iter(mi_lista)

for elemento in iterador:
    print(f"{elemento=}")

exit()









class EvenNumbers:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        even = self.current
        self.current += 2
        return even

even_iter = EvenNumbers(11)
for num in even_iter:
    print(f"{num=}")

"""
