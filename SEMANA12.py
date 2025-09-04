#Tarea: Iteración de arreglos multidimensionales con bucles anidados
#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
#Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
#Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.

# Registro de temperaturas diarias en diferentes ciudades
# Estructura de la matriz 3D:
# [ciudad][semana][día]

# Lista de ciudades
ciudades = ["Lago Agrio", "Quito", "Esmeraldas"]

# Creamos una matriz 3D de ejemplo con temperaturas ficticias
# 2 semanas, 7 días por semana
temperaturas = [
    [   # Lago Agrio
        [25, 26, 27, 28, 26, 27, 25],  # Semana 1
        [24, 25, 26, 27, 25, 26, 24]   # Semana 2
    ],
    [   # Quito
        [18, 20, 19, 21, 20, 22, 19],  # Semana 1
        [17, 19, 20, 21, 18, 20, 19]   # Semana 2
    ],
    [   # Esmeraldas
        [28, 29, 30, 29, 28, 30, 31],  # Semana 1
        [27, 28, 29, 28, 27, 29, 30]   # Semana 2
    ]
]

# Cálculo de promedios
for i in range(len(ciudades)):  # Iterar ciudades
    print(f"\nPromedios de temperatura para {ciudades[i]}:")
    for j in range(len(temperaturas[i])):  # Iterar semanas
        suma = 0
        for k in range(len(temperaturas[i][j])):  # Iterar días
            suma += temperaturas[i][j][k]
        promedio = suma / len(temperaturas[i][j])
        print(f"  Semana {j+1}: {promedio:.2f} °C")
