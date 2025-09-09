def calcular_promedios(datos):
    """
    Calcula el promedio de temperaturas por ciudad.

    Parámetros:
    datos (dict): Diccionario con ciudades como claves y listas de temperaturas como valores.
                  Cada lista representa las temperaturas semanales de esa ciudad.

    Retorna:
    dict: Diccionario con las ciudades y sus temperaturas promedio.
    """

    promedios = {}  # Diccionario vacío para guardar resultados
    for ciudad, temperaturas in datos.items():  # Recorremos cada ciudad y sus temperaturas
        promedio = sum(temperaturas) / len(temperaturas)  # Fórmula del promedio
        promedios[ciudad] = promedio  # Guardamos el promedio en el diccionario
    return promedios


# Datos de ejemplo: Quito, Lago Agrio y Esmeraldas (4 semanas cada ciudad)
temperaturas = {
    "Quito": [18, 20, 19, 17,19],
    "Lago Agrio": [25, 27, 26, 28,30],
    "Esmeraldas": [29, 30, 31, 28,29],
    "Cuenca": [15,17,16,18,15],
}

# Probamos la función
promedios = calcular_promedios(temperaturas)

# Mostramos los resultados
for ciudad, promedio in promedios.items():
    print(f"La temperatura promedio en {ciudad} es {promedio:.2f} °C")
