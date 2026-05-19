def contar_palabras_archivo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            total = len(palabras)
            return total
    except FileNotFoundError:
        print(f"El archivo en la ruta '{ruta_archivo}' no existe.")
        return 0
    
if __name__ == "__main__":
    nombre_archivo = "texto.txt"
    resultado = contar_palabras_archivo(nombre_archivo)

    if resultado > 0:
        print(f"El archivo '{nombre_archivo}' tiene un total de {resultado} palabras.")