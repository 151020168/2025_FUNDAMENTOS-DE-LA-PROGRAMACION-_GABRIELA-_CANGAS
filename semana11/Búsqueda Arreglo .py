def buscar_en_matriz(matriz, valor_buscado):

    """

    Busca un valor específico en una matriz bidimensional.



    Args:

        matriz (list of list): La matriz bidimensional a buscar.

        valor_buscado (int or float): El valor a encontrar.



    Returns:

        tuple or None: Una tupla (fila, columna) si el valor se encuentra,

                       None en caso contrario.

    """

    for fila_idx, fila in enumerate(matriz):

        for col_idx, valor in enumerate(fila):

            if valor == valor_buscado:

                return (fila_idx, col_idx)

    return None



# Matriz bidimensional de ejemplo (3x3)

mi_matriz = [

    [1, 5, 9],

    [3, 7, 2],

    [8, 4, 6]

]



# Valor que deseas buscar

valor_a_encontrar = 7



# Realizar la búsqueda

posicion = buscar_en_matriz(mi_matriz, valor_a_encontrar)



# Mostrar el resultado

if posicion:

    print(f"El valor {valor_a_encontrar} se encontró en la posición: Fila {posicion[0]}, Columna {posicion[1]}")

else:

    print(f"El valor {valor_a_encontrar} no se encontró en la matriz.")



# Ejemplo con un valor que no está en la matriz

valor_no_encontrado = 10

posicion_no_encontrada = buscar_en_matriz(mi_matriz, valor_no_encontrado)



if posicion_no_encontrada:

    print(f"El valor {valor_no_encontrado} se encontró en la posición: Fila {posicion_no_encontrada[0]}, Columna {posicion_no_encontrada[1]}")

else:

    print(f"El valor {valor_no_encontrado} no se encontró en la matriz.")