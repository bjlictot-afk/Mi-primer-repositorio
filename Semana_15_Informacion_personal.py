# Tarea: Trabajando con Diccionarios en Python
# Autor: Belgica Jomayra Licto Timbila
# Ing:Llerena Ocaña Luis Antonio

# 1) Crear un Diccionario
informacion_personal = {
    "nombre": "Belgica Licto",
    "edad": 21,
    "ciudad": "Latacunga",
    "profesion": "Estudiante de Tecnologías de la Información"
}
print("1) Diccionario inicial:")
print(informacion_personal)

# 2) Acceder y Modificar Valores
print("\n2) Valor actual de 'ciudad':", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Lago Agrio"   # cambiamos Latacunga por Lago Agrio
print("   Nuevo valor de 'ciudad':", informacion_personal["ciudad"])

# 3) Agregar o modificar la clave 'profesion'
informacion_personal["profesion"] = "Ingeniera en Tecnologías de la Información"
print("\n3) Profesión actualizada:", informacion_personal["profesion"])

# 4) Verificar Existencia de Claves y agregar 'telefono' si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0969752115"  # número ficticio
    print("\n4) La clave 'telefono' no existía, se agregó:", informacion_personal["telefono"])

# 5) Eliminar la clave 'edad'
informacion_personal.pop("edad", None)
print("\n5) La clave 'edad' fue eliminada.")

# 6) Imprimir el Diccionario Final
print("\n6) Diccionario final resultante:")
print(informacion_personal)


