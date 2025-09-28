# Crear un Diccionario inicial
informacion_personal = {
    "nombre": "Gabriela Cangas",
    "edad": 31,
    "ciudad": "Quito",
    "profesion": "Psiquiatra"
}

print("Diccionario Inicial:")
print(informacion_personal)

# Acceder y Modificar Valores:

# 1. Acceder y modificar "ciudad"
informacion_personal["ciudad"] = "Guayaquil"

# 2. Agregar una nueva clave-valor (Nota: la instrucción pide agregar "profesion"
# pero ya existe. Asumiré que se refiere a agregar otra clave, por ejemplo, "email")
# Si la instrucción literal es agregar "profesion", simplemente se sobrescribe:
informacion_personal["profesion"] = "Economista" # Sobrescribiendo el valor existente

print("\nDespués de modificar ciudad y profesión:")
print(informacion_personal)

# Verificar Existencia de Claves:

# 1. Verificar si "telefono" existe
if "telefono" not in informacion_personal:
    # 2. Si no existe, agregarla
    informacion_personal["telefono"] = "0991234567"

print("\nDespués de verificar y agregar teléfono:")
print(informacion_personal)

# Eliminar una Clave:

# Eliminar la clave "edad"
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el Diccionario Final
print("\nDiccionario Final:")
print(informacion_personal)