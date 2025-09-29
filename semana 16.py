# Tarea: Trabajo con Archivos de Texto en Python
#Nombre:Belgica Licto
#Docente:Llerena Ocaña Luis Antonio
# Este programa crea un archivo de texto, escribe notas personales,
# luego lee el contenido línea por línea y lo muestra en consola.

# ----------- Escritura en archivo -----------
# Abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales
archivo.write("Nota 1: Recordar revisar el proyecto de matemáticas.\n")
archivo.write("Nota 2: Practicar ejercicios de Python para la clase.\n")
archivo.write("Nota 3: Preparar el informe sobre Sigchos.\n")

# Cerramos el archivo después de escribir
archivo.close()

# ----------- Lectura del archivo -----------
# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos y mostramos el contenido línea por línea
linea = archivo.readline()  # Leemos la primera línea
while linea != "":  # Mientras haya contenido en la línea
    print(linea.strip())  # Imprimimos la línea sin salto de línea extra
    linea = archivo.readline()  # Leemos la siguiente línea

# Cerramos el archivo después de leer
archivo.close()
