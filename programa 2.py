def bubble_sort_fila(matriz, indice_fila):
    """
    Ordena una fila específica de una matriz bidimensional en orden ascendente
    utilizando el algoritmo Bubble Sort.

    Args:
        matriz (list of list): La matriz bidimensional a modificar.
        indice_fila (int): El índice de la fila que se va a ordenar.

    Returns:
        None: La matriz se modifica in-place.
    """
    if not (0 <= indice_fila < len(matriz)):
        print("Error: Índice de fila fuera de rango.")
        return

    fila_a_ordenar = matriz[indice_fila]
    n = len(fila_a_ordenar)

    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            # Recorrer la lista de 0 a n-i-1
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if fila_a_ordenar[j] > fila_a_ordenar[j + 1]:
                fila_a_ordenar[j], fila_a_ordenar[j + 1] = fila_a_ordenar[j + 1], fila_a_ordenar[j]

def imprimir_matriz(matriz, titulo="Matriz"):
    """Imprime la matriz de forma legible."""
    print(f"\n--- {titulo} ---")
    for fila in matriz:
        print(fila)
    print("----------------")

# Matriz bidimensional de ejemplo (3x3)
mi_matriz_original = [
    [1, 5, 9],
    [3, 7, 2],
    [8, 4, 6]
]

# Índice de la fila que se desea ordenar
fila_a_ordenar_idx = 1 # Ordenaremos la segunda fila (índice 1)

# Crear una copia de la matriz original para mostrarla después de la ordenación
matriz_para_ordenar = [fila[:] for fila in mi_matriz_original] # Copia profunda

# Mostrar la matriz original
imprimir_matriz(mi_matriz_original, "Matriz Original")

# Ordenar la fila especificada
bubble_sort_fila(matriz_para_ordenar, fila_a_ordenar_idx)

# Mostrar la matriz con la fila ordenada
imprimir_matriz(matriz_para_ordenar, f"Matriz con Fila {fila_a_ordenar_idx} Ordenada")
