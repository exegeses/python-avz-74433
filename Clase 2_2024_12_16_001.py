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
import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')
def pausa():
    input("\tEnter para continuar")
    limpiar()
#######################################################################################################
pausa()
limpiar()


'''
        Te damos la bienvenida al curso de Python Programming
        Organización del curso
        Instructivo de Instalación
        Glosario - Terminología a utilizar
        Python y herramientas
        Acerca de Python
        Instalaciones y Hola Mundo!
        Introducción y cuestiones básicas
        Tipo de datos y colecciones
        Operadores
        Sentencias de control
        Funciones primera parte
        Funciones Built-in (integradas)
                A=abs(),aiter(),all(),any(),anext(),ascii()
                B=bin(),bool(),breakpoint(),bytearray(),bytes()
                C=callable(),chr(),classmethod(),compile(),complex()
                D=delattr(),dict(),dir(),divmod()
                E,enumerate(),eval(),exec()
                F=filter(),float(),format(),frozenset()
                G=getattr(),globals()
                H=hasattr(),hash(),help(),hex()
                I=id(),input(),int(),isinstance(),issubclass(),iter()
                L=len(),list(),locals()
                M=map(),max(),memoryview(),min()
                N=next()
                O=object(),oct(),open(),ord()
                P=pow(),print(),property()
                R=range(),repr(),reversed(),round()
                S=set(),setattr(),slice(),sorted(),staticmethod(),str(),sum(),super()
                T=tuple(),type()
                V=vars()
                Z=zip()
                _=__import__()
            condicionales = if elif else, match case, ¿while?
            bucles = while, for
'''



# ~ int x = 8;

x = 8
print (f""" 
{x=}
{type(x)=}
{id(x)=}


""")
print ("*"*50)
x = 9
print (f""" 
{x=}
{type(x)=}
{id(x)=}
""")


print ("*"*50)
x = "Ariel"
print (f""" 
{x=}
{type(x)=}
{id(x)=}
""")
print ("*"*50)
lista = [ "Ariel",8,9,10]
print (f""" 
{lista=}
{type(lista)=}
{id(lista)=}
""")
lista.append("fin")
print (f""" 
{lista=}
{type(lista)=}
{id(lista)=}
""")
print (f""" 
{lista[0]=}
{type(lista[0])=}
{id(lista[0])=}
""")

print (f""" 
{lista[1]=}
{type(lista[1])=}
{id(lista[1])=}
""")


print (f""" 
{lista[2]=}
{type(lista[2])=}
{id(lista[2])=}
""")




print (f""" 
{lista[3]=}
{type(lista[3])=}
{id(lista[3])=}
""")

pausa()
limpiar()

x =8 
print (f""" 
{x=}
{type(x)=}
{id(x)=}
{dir(x)=}
""")
"""
<class 'int'>
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 
------------------------------------------------------------------
'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
"""
pausa()
print ("*"*50)
x =8.5 
print (f""" 
{x=}
{type(x)=}
{id(x)=}
{dir(x)=}
""")
"""
<class 'float'>
['__abs__', '__add__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__int__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__pos__', '__pow__', '__radd__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 
------------------------------------------------------------------
'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
"""
pausa()

print ("*"*50)
x = "Ariel"
print (f""" 
{x=}
{type(x)=}
{id(x)=}
{dir(x)=}
""")
"""
<class 'str'>
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',

------------------------------------------------------------------
 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
------------------------------------------------------------------
estilo
'capitalize', 'casefold', 'lower','swapcase', 'title',  'upper'

lugar


'center', 'ljust','rjust', 

"""

"""

condicionales / booleanos

 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'startswith', 'endswith']
"""



x ="876"

print (f"{x.isdigit()}")
if x.isdigit() is True:
    x = int(x)
    
print (f"""
{x=}
{type(x)=}
""")


x ="8,76"
print (f"""
ojo tiene coma
{x=}
{type(x)=}
""")

x = x.replace(',','.',1)
print (f"""
{x=}
{type(x)=}
""")



nombre_real = input ("ingrese su nombre real:")
if nombre_real.replace(" ","").isalpha():
    print (f"{nombre_real} - ok")
else:
    print (f"{nombre_real} - no se acepta")
    
print ("*"*50)    
# ########################################################################
nombre_real = ""

#while not (nombre_real.isalpha().replace(" ","") ):
#por orden de parametros (logica) 
# porque cualquier is da una booleana que no tiene replace como metodo
while not (nombre_real.replace(" ","").isalpha() ):
    print (f"{nombre_real} - no se acepta")
    nombre_real = input ("ingrese su nombre real:")
else:
    print (f"{nombre_real} - ok")

print ("*"*50)    
# ########################################################################

print (f"{x.replace('.','',1).isdigit()}")
if x.replace('.','',1).isdigit() is True:
    x = float(x)
else:
    print ("no puedo convertir el str")

print (f"""
{x=}
{type(x)=}
""")
print ("*"*50)    
# ########################################################################






x= "hOLA mUNDO it L Y V 11HS"
x= x.swapcase()
print (f"{x=}")


"""

replace
 'replace',

"""





"""
otros

 'count', 'encode', 'expandtabs', 'join', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'rfind', 'rindex',  'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', , 'strip', 'translate',  'zfill']
"""

x = "Hola mundo IT 2024"
print (f"{x=}")
print (f"{x.capitalize()=}")
print (f"{x.casefold()=}")
print (f"{x.lower()=}")
print (f"{x.swapcase()=}")
print (f"{x.title()=}")
print (f"{x.upper()=}")

炩牁牉牊牬牰牳牮 = 33

print (炩牁牉牊牬牰牳牮)

print (f"{x=}")
print (f"x.center(50)|{x.center(50)}|")
print (f"x.ljust(50) |{x.ljust(50)}|")
print (f"x.rjust(50) |{x.rjust(50)}|")


print (f"x.center(50).upper()   |{x.center(50).upper()}|")
print (f"x.swapcase().rjust(50) |{x.swapcase().rjust(50)}|")



pausa()










print ("x=",x,"\ntype(x)=",type(x),"\nid=", id(x))


x = "Ariel"




palabras_reservadas=           {
            "False":             "Valor booleano, resultado de operaciones de comparación u operaciones lógicas en Python.",
            "None":              "Representa a un valor nulo.",
            "True":              "Valor booleano, igual que false, resultado de operaciones de comparación u operaciones lógicas en Python.",
            "__peg_parser__":    "Llamado huevo de pascua, relacionado con el lanzamiento del nuevo analizador PEG no está definido aún.",
            "And":               "Operador lógico.",
            "As":                "Se utiliza para crear un alias al importar un módulo.",
            "Assert":            "Se utiliza con fines de depuración.",
            "Async":             "Proporcionada por la biblioteca ‘asyncio' en Python. Se utiliza para escribir código concurrente en Python.",
            "Await":             "Proporcionada por la biblioteca ‘asyncio' en Python. Se utiliza para escribir código concurrente en Python.",
            "Break":             "Se utiliza en el interior de los bucles for y while para alterar su comportamiento normal.",
            "Class":             "Se usa para definir una nueva clase definida por el usuario.",
            "Continue":          "Se utiliza en el interior de los bucles for y while para alterar su comportamiento normal.",
            "Def":               "Se usa para definir una función definida por el usuario.",
            "Del":               "Se usa para eliminar un objeto.",
            "Elif":              "Se usa en declaraciones condicionales, igual ‘else' e ‘if.",
            "Else":              "Se usa en declaraciones condicionales, igual ‘elif' e ‘if'.",
            "Except":            "Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que ‘raise' y ‘try'.",
            "Finally":           "Su uso garantiza que el bloque de código dentro de él se ejecute incluso si hay una excepción no controlada.",
            "For":               "Se usa para hacer bucles. Generalmente lo usamos cuando sabemos la cantidad de veces que queremos que se ejecute ese bucle.",
            "From":              "Se usa para importar partes específicas de un módulo.",
            "Global":            "Se usa para declarar una variable global.",
            "If":                "Se usa en declaraciones condicionales, igual ‘else' y ‘elif'.",
            "Import":            "Se usa para importar un módulo.",
            "In":                "Se usa para comprobar si un valor está presente en una lista, tupla, etc. Devuelve True si el valor está presente, de lo contrario devuelve False.",
            "Is":                "Se usa para probar si las dos variables se refieren al mismo objeto.  Devuelve True si los objetos son idénticos y False si no.",
            "Lambda":            "Se usa para crear una función .",
            "Nonlocal":          "Se usa para declarar una variable no local.",
            "Not":               "Operador lógico.",
            "Or":                "Operador lógico.",
            "Pass":              "Se usa como declaración nula en Python. No pasa nada cuando se ejecuta. Se utiliza como marcador de posición.",
            "Raise":             "Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que ‘except y ‘try'.",
            "Return":            "Se usa dentro de una función para salir y devolver un valor.",
            "Try":               "Se usa para crear excepciones, qué hacer cuando ocurre una excepción, igual que 'raise' y 'except'.",
            "While":             "Se usa para realizar bucles.",
            "With":              "Se usa para simplificar el manejo de excepciones.",
            "Yield":             "Se usa dentro de una función al igual que ‘return', salvo que ‘yield' devuelve un generador."}
for p,v in palabras_reservadas.items():
    print (f"{p} -> {v}")
pausa()
listas=[ 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
tuplas=( 'count', 'index', )
dic={1:'clear', 2:'copy', 3:'fromkeys', 4:'get', 5:'items', 6:'keys', 7:'pop', 8:'popitem', 9:'setdefault', 10:'update', 11:'values'}

print('''
        Operadores matemáticos
                Nombre     Ejemplo   Resultado
        ________________________________________________
        +        Suma       5 + 6      11
        -        Resta      10 - 2      8
        *   Multiplicación  3 * 10     30
        /   División        5 / 2     2.5
        %   Módulo(Resto)   9 % 2       1
        **  Exponente       10 ** 2   100
        // División Entera  9 // 2      4
''')

print('''
        Operadores de asignación
                Ejemplo     Equivalente Resultado
        ________________________________________________
        =       x = 10       x = 10        10
        +=      x += 5       x = x + 5     15
        -=      x -= 2       x = x - 2     13
        *=      x *= 2       x = x * 2     26
        /=      x /= 2       x = x / 2     13
        //=     x //= 2      x = x // 2     6
        **=     x **= 2      x = x ** 2    36
        %=      x %= 2       x = x % 2      0
''')

print('''
        Operadores de condición o relacionales
                Nombre Ejemplo  si x=10   Resultado
        ________________________________________________
        ==       Igual          x == 6      False
        !=       Distinto       x != 8      True
        >        Mayor          x > 4       True
        <        Menor          x < 3       False
        >=       Mayor igual    x >= 20     False
        <=       Menor igual    x <= 5      True
''')

print('''
        Operadores lógicos
                Acción
        ________________________________________________
        and      Devuelve True si ambos elementos son True
        or       Devuelve True si al menos un elemento es True
        not      Devuelve el contrario, True si es Falso y viceversa

        Operador Especiales
                Acción
        ________________________________________________
        is       Devuelve True / False > x is False
        in       Devuelve True / False  x pertenece al conjunto

        Operador de Walrus
                Acción
        ________________________________________________
        print(dato:="Hola") #asigna al mismo tiempo que imprime
        print(dato)
''')

print(dato:="Hola")
print(f"{dato=}")
while not ( v:=input("Continuo?:").upper()=='S'):print("solo S/N")
print (f"{v=}, {type(v)=}")

input("Enter para continuar......")

print('''
        Operador a nivel bit , bitwise
        ______________________________
            Los operadores a nivel de bit son operadores que actúan sobre números enteros, pero usando su representación binaria. 
            Si no sabes cómo se representa un número en forma binaria, no hace falta que te hagas mucho problema, ya que estos operadores no se 
                usan tan frecuentemente como los otros. 
            Su uso puede ser más empleado en lenguajes de bajo nivel, y Python no es un lenguaje de esas características. 
            Pero no está de más conocerlos.
                    Operador            Acción
                        |       OR      bit a bit
                        &       AND     bit a bit
                        ~       NOT     bit a bit
                        ^       XOR     bit a bit
                        >>   Desplazamiento bit a la derecha
                        <<   Desplazamiento bit a la izquierda
''')
# ~ Funciones built-in (integradas o preconstruidas)

# ~ Condicional IF - ELIF - ELSE
# ~ Operador Ternario es una cláusula if-else que se define en una sola línea
cant = 1
print(f"comamos {cant} ","helado " if cant==1 else "helados")

# ~ Bucle WHILE
# ~ Bucle FOR
# ~     Break y Continue
# ~ Funciones propias
        # ~ estructura

input("Enter para continuar......")
def funcion():
    pass

def nombre_funcion(argumentos):
    # código
    return retorno
# ~ Argumentos por defecto
def imprimir_mensaje(mensaje="No has escrito nada."):
    print(f"{mensaje=}")

# ~ Documentación en funciones
def sumar(a, b):
    """
    docstring
        suma los dos argumentos de entrada y retorna es resultado
    """
    resultado =  a + b
    return resultado
print(f"{sumar(6,2)=}")
print(f"{sumar.__doc__=}")

input("Enter para continuar......")
# ~ Ámbito de las variables

global variable# no aconsejable

variable = 10
def funcion():
    global variable
    variable = 5
print(f"{variable=}")
funcion()
print(f"{variable=}")
# ~ Paso por valor y por referencia
def funcion(entrada):
    entrada.append(40)
dato = [10, 20, 30]
funcion(dato)
print(f"{dato=}")
print('''
        Argumentos de longitud variable 
        Al declarar la función con un parámetro *, hará que los argumentos, sean la cantidad que fueran, lleguen individualmente y que una vez recibido 
            la función lo empaquete en una tupla de manera automática.
        Atención: No confundir * con los punteros en otros lenguajes de programación, no tiene nada que ver 
        ¡En Python existen los punteros a memoria!
''')
def sumar(*args):
    print(f"{args=}")
    print(f"{type(args)=}")
    total = 0
    for n in args:
        total += n
    return total
l=sumar(10,0,5,4)
print(f"{l=}")
print('''
        El doble asterisco ** (usualmente acompañado por el nombre kwargs) captura cualquier keyword argument que no haya sido definido junto con la función. 
        Los argumentos capturados por este operador son almacenados, como dijimos, en un diccionario que tiene como claves los strings que representan los 
            nombres de los argumentos, y como valor, el valor del argumento. 
        Este operador debe ir al final de la definición de otros parámetros, si los hubiera.
''')
# ~ Ejemplo:
def sumar(**kwargs):
    print(f"{kwargs=}")
    print(f"{type(kwargs)=}")
    total = 0
    for n in kwargs:
        total+= kwargs[n]

    print(f"{total=}")
sumar(a=5, b=20, c=23)
# ~ Orden para usar diferentes argumentos
def funcion(a,b,*args,c=100,**kwargs):
    print(f"{a=}\t\t\t{type(a)=}")
    print(f"{b=}\t\t\t{type(b)=}")
    print(f"{args=}\t\t\t{type(args)=}")
    print(f"{c=}\t\t\t{type(c)=}")
    print(f"{kwargs=}\t\t\t{type(kwargs)=}")

######################################

def superior(funcion,lista):
    nueva = []
    for n in lista:
        nueva.append(funcion(n))
    return nueva


######################################

print(f"{superior(lambda x : x**3,[1,2,3])=}")
print()

input("Enter para continuar......")

'''
Las palabras clave assert, try, except, finally y raise están relacionadas con las excepciones, y nos permiten tratar el qué hacer 
cuando las cosas no salen como esperamos. El siguiente código intenta hacer un cast de cadena a entero, manejando un posible error.
Si x="10" el casteo se realiza sin problemas, ya que es posible representar esa cadena como un entero. 
Sin embargo hay que estar preparados siempre para lo peor.
Si x="a" no se podría hacer int() y tendríamos un error. 
Si no manejamos este error, el programa se pararía, y esto no es algo deseable. 
El uso de try, except y finally nos permite controlar dicho error y actuar en consecuencia sin que el programa se pare.

'''
