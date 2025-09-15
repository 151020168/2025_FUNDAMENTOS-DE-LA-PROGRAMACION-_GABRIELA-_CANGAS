def calcular_temperatura_promedio(datos_ciudades):
    """
    Calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    Args:
        datos_ciudades (dict): Un diccionario donde las claves son los nombres de las ciudades
                               y los valores son listas de temperaturas semanales.

    Returns:
        dict: Un diccionario donde las claves son los nombres de las ciudades
              y los valores son sus temperaturas promedio.
    """
    promedios_por_ciudad = {}
    for ciudad, temperaturas in datos_ciudades.items():
        if temperaturas:  # Asegurarse de que la lista de temperaturas no esté vacía
            promedio = sum(temperaturas) / len(temperaturas)
            promedios_por_ciudad[ciudad] = promedio
        else:
            promedios_por_ciudad[ciudad] = 0  # O algún otro valor indicativo de datos faltantes
    return promedios_por_ciudad

# Ejemplo de uso con los datos proporcionados
datos_ejemplo = {
    "Ciudad1": [20, 22, 21, 23],
    "Ciudad2": [28, 30, 29, 31],
    "Ciudad4": [18, 19, 17, 20]
}

promedios = calcular_temperatura_promedio(datos_ejemplo)
print(promedios)