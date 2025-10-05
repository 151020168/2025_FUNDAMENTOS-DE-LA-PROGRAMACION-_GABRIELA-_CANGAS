# --- PARTE 1: ESCRITURA DE ARCHIVO DE TEXTO ---

# Nombre del archivo a crear y manipular
nombre_archivo = "my_notes.txt"

# Abrimos el archivo en modo escritura ('w'). Si el archivo existe, su contenido anterior se borra.
# Usamos 'with' para asegurar que el archivo se cierre automáticamente al salir del bloque.
try:
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo_escritura:
        # Escribimos las tres líneas de notas personales solicitadas.
        # Es importante añadir '\n' para que cada nota quede en una línea separada.
        archivo_escritura.write("Nota 1: Recordar comprar café de grano el viernes.\n")
        archivo_escritura.write("Nota 2: El proyecto X debe revisarse antes del lunes.\n")
        archivo_escritura.write("Nota 3: Llamar a Juan sobre la reunión pendiente.\n")

    print(f"--- Escritura completada en '{nombre_archivo}' ---")

except IOError:
    print(f"Error: No se pudo escribir en el archivo {nombre_archivo}.")

# --- PARTE 2: LECTURA DE ARCHIVO DE TEXTO ---

print("\n--- Leyendo contenido línea por línea ---")

# Abrimos el archivo en modo lectura ('r').
try:
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo_lectura:

        # Inicializamos un contador para llevar la cuenta de las líneas leídas
        contador_linea = 1

        # Usamos un bucle while junto con el método readline() para leer línea por línea.
        # readline() devuelve una cadena vacía ('') cuando llega al final del archivo (EOF).
        while True:
            # Leemos la siguiente línea del archivo
            linea = archivo_lectura.readline()

            # Verificamos si hemos llegado al final del archivo
            if not linea:
                break

            # Mostramos la línea leída en la consola. Usamos .strip() para eliminar el '\n' final.
            print(f"Línea {contador_linea}: {linea.strip()}")

            contador_linea += 1

    # El archivo se cierra automáticamente al salir del bloque 'with', cumpliendo con el requisito de cierre.
    print("\n--- Lectura finalizada y archivo cerrado ---")

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado para lectura.")
except IOError:
    print(f"Error: Ocurrió un problema al leer el archivo {nombre_archivo}.")