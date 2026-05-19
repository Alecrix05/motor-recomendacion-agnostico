def analizar_texto(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            todas_las_palabras = contenido.lower().split()
            palabras_limpias = [p for p in todas_las_palabras if len(p) > 2]
            frecuencia_palabras = {}

            for p in palabras_limpias:
                if p in frecuencia_palabras:
                    frecuencia_palabras[p] += 1
                else:
                    frecuencia_palabras[p] = 1
            
            return frecuencia_palabras
    except FileNotFoundError:
        print(f"El archivo no existe.")
        return {}

if __name__ == "__main__":
    resultado = analizar_texto("texto.txt")
    print("Frecuencia de palabras limpias: ")
    print(resultado)