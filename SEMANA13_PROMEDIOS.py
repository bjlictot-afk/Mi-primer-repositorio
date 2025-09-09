#Tarea Individual: Desarrollo de Función para Calcular Temperaturas Promedio en Python
#Nombre:Belgica Licto
#Docente:ING.Llerena Ocaña Luis Antonio
#Semana_13
def calcular_promedios(datos):
    """
    Calcula el promedio de temperaturas por ciudad.

    Parámetros:
    datos (dict): Diccionario con ciudades como claves y listas de temperaturas como valores.
                  Cada lista representa las temperaturas semanales de esa ciudad.

    Retorna:
    dict: Diccionario con las ciudades y sus temperaturas promedio.
    """
    promedios = {}  # Diccionario para guardar resultados
    for ciudad, temperaturas in datos.items():  # Recorre cada ciudad y sus temperaturas
        promedio = sum(temperaturas) / len(temperaturas)  # Calcula el promedio
        promedios[ciudad] = promedio  # Guarda el promedio en el diccionario
    return promedios


# Datos de ejemplo: 3 ciudades con 4 semanas cada una
temperaturas = {
    "Quito": [18, 20, 19, 17],
    "Lago Agrio": [25, 27, 26, 28],
    "Esmeraldas": [29, 30, 31, 28],
}

# Probamos la función
promedios = calcular_promedios(temperaturas)

# Mostramos los resultados
for ciudad, promedio in promedios.items():
    print(f"La temperatura promedio en {ciudad} es {promedio:.2f} °C")
