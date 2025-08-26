# Programa 2: Ordenación de una fila en una matriz bidimensional
# Autor: Belgica Jomayra
# Fecha: 25/08/2025

# Definimos una matriz 3x3
matriz = [
    [5, 8, 2],
    [9, 3, 7],
    [6, 4, 1]
]

def bubble_sort(fila):
    """
    Ordena una lista (fila) con el algoritmo Bubble Sort en orden ascendente.
    """
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Fila a ordenar (ejemplo: fila 1 → segunda fila de la matriz)
fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la fila seleccionada
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz después de ordenar la fila", fila_a_ordenar)
for fila in matriz:
    print(fila)
