# Programa 1: Búsqueda en una matriz bidimensional
# Autor: Belgica Jomayra
# Fecha: 25/08/2025

# Definimos una matriz 3x3
matriz = [
    [5, 8, 2],
    [9, 3, 7],
    [6, 4, 1]
]

def buscar_valor(matriz, valor):
    """
    Busca un valor en la matriz y retorna su posición si existe.
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  # Retorna fila y columna
    return None

# Valor a buscar
valor_buscado = 7
posicion = buscar_valor(matriz, valor_buscado)

# Resultados
print("Matriz:")
for fila in matriz:
    print(fila)

if posicion:
    print(f"\n✅ El valor {valor_buscado} se encontró en la posición (fila {posicion[0]}, columna {posicion[1]}).")
else:
    print(f"\n❌ El valor {valor_buscado} no se encontró en la matriz.")
