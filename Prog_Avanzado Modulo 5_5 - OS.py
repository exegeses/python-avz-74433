import os
def limpiar():
    os.system('cls' if os.name == "ce" or os.name == "nt" or os.name == "dos"  else 'clear')

def pausa():
    input("\tPresione una tecla para continuar")
import random
limpiar();

print("""\033[1;37;44m\n
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║                             Operative system                                ║
║                             ----------------                                ║
║                      Existencia de archivos o directorios (booleanas)       ║
║                      Manejo de carpetas o directorios                       ║
║                                archivos                                     ║
╚═════════════════════════════════════════════════════════════════════════════╝
\033[0;m""");
def ya_hechos():
    pass


    import os
    if os.path.isfile("temporario.tmp"):
        print (f"'temporario' existe cono archivo ")
        os.remove("temporario.tmp")
        print ("archivo eliminado")
    else:
        print (f"'temporario' no existe cono archivo ")
        with open("temporario.tmp","w") as io_obj:
            io_obj.write("texto a borrar")
        print ("archivo creado")

    if os.path.isdir("temporario.dir"):
        print (f"'temporario' existe cono directorio")
        os.rmdir("temporario.dir")
        print ("directorio eliminado")
    else:
        print (f"'temporario' no existe cono directorio")
        os.mkdir("temporario.dir")
        print ("directorio creado")
    print(f"Directorio actual:{directorio_actual}")
    #··················································································
    pausa()
    limpiar()

    import os
    directorio_actual = os.getcwd()
    print(f"Directorio actual:{directorio_actual}")

    #··················································································
    pausa()
    limpiar()

    import os
    directorio_actual = os.getcwd()
    contenido_directorio_actual =os.listdir(directorio_actual)
    print(f"Contenido del directorio actual:{contenido_directorio_actual}")
    for registro in contenido_directorio_actual:
        print (f"{registro}")
    #··················································································
    pausa()
    limpiar()

    # ~ import os
    # ~ directorio_actual = os.getcwd()
    # ~ nuevo_directorio = f"{directorio_actual}/nueva_carpeta"
    # ~ #nuevo_directorio = f"{directorio_actual}\\nueva_carpeta"
    # ~ os.mkdir(nuevo_directorio)
    # ~ print(f"nueva carpeta creada:\n{nuevo_directorio}")
    # ~ #··················································································
    pausa()
    limpiar()

    import os
    directorio_actual = os.getcwd()
    nombre_original = f"{directorio_actual}/nueva_carpeta"
    nombre_nuevo    = f"{directorio_actual}/carpeta_nueva"
    os.rename(nombre_original,nombre_nuevo)
    print(f"Cambio de nombre de carpeta :\n{nombre_original}  a {nombre_nuevo}" )
    #··················································································
    pausa()
    limpiar()

    import os
    directorio_actual = os.getcwd()
    # ~ directorio = f"{directorio_actual}/nueva_carpeta"
    directorio = f"{directorio_actual}/carpeta_nueva"
    os.rmdir(directorio)
    print(f"Se elimino la carpeta :\n{directorio} " )
    #··················································································
    pausa()
    limpiar()

    import os
    archivo="temp.tmp"
    with open(archivo,"w") as io_obj:
        io_obj.write("texto a borrar")
    os.remove(archivo)
    print(f"Se elimino el archivo :\n{archivo} " )
    #··················································································
    pausa()
    limpiar()

    import os
    directorio_actual = os.getcwd()
    print(f"Directorio actual:{directorio_actual}")
    directorio = f"{directorio_actual}/carpeta_nueva"
    if not os.path.isdir(directorio):
        print (f"El directorio de destino {directorio} no existe")
        print ("lo creamos")
        os.mkdir (directorio)
    os.chdir (directorio)
    directorio_actual = os.getcwd()
    print(f"Directorio actual:{directorio_actual}")
    #··················································································
    pausa()
    limpiar()
    import time
    directorio_actual = os.getcwd()
    directorio = f"{directorio_actual}/carpeta_nueva"
    if not os.path.isdir(directorio):
        print (f"El directorio de destino {directorio} no existe")
        print ("lo creamos")
        os.mkdir (directorio)
    archivo="temp.tmp"
    with open(f"{directorio}/{archivo}","w") as io_obj:
        io_obj.write("texto a borrar")
    #   ambos generan la misma salida
    #   total = f"{directorio}/{archivo}"
    total = os.path.join(directorio, archivo)
    print (f"{total}")
    directorio, nombre_archivo = os.path.split(total)
    tamaño_archivo = os.path.getsize(total)
    fecha_modific_archivo = os.path.getmtime(total)
    print(f"Directorio:{directorio}")
    print(f"Nombre de archivo:{nombre_archivo}")
    print(f"Tamaño de archivo:{tamaño_archivo} bytes")
    print(f"Fecha modifición del archivo:{time.ctime(fecha_modific_archivo)}")
    #··················································································
    pausa()
    limpiar()
origen = os.getcwd()


for directorio_actual, subdirectorios, archivos in os.walk(origen):
    print("Directorio actual:", directorio_actual)
    print("Subdirectorios:", subdirectorios)
    print("Archivos:", archivos)


exit()

objeto_python ="""
Rima XXI
¿Qué es poesía?, dices, mientras clavas
en mi pupila tu pupila azul,
¡Qué es poesía! ¿Y tú me lo preguntas?
Poesía... eres tú.
"""

"""
RIMA XXIII
Por una mirada, un mundo;
por una sonrisa, un cielo;
por un beso... ¡Yo no sé
qué te diera por un beso!

Rima XXX
Asomaba a sus ojos una lágrima
y a mi labio una frase de perdón;
habló el orgullo y se enjugo su llanto
y la frase en mis labios expiró.
Yo voy por un camino: ella, por otro;
pero al pensar en nuestro mutuo amor,
yo digo aún, ¿por qué callé aquel día?
Y ella dirá, ,¿por qué no lloré yo?

Rima XXXV
¡No me admiró tu olvido! Aunque de un día,
me admiró tu cariño mucho más;
porque lo que hay en mí que vale algo,
eso... ni lo pudiste sospechar.

Rima XXXVIII
Los suspiros son aire y van al aire.
Las lágrimas son agua y van al mar.
Dime, mujer, cuando el amor se olvida,
¿sabes tú adónde va?

"""
