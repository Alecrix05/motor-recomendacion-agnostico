import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', 1000)

def load_data(filepath, text_columns):
    try:
        df = pd.read_csv(filepath)

        for col in text_columns:
            if col not in df.columns:
                print(f"Error: La columna '{col}' no se encuentra en el dataset.")
                return None
            
        df[text_columns] = df[text_columns].fillna('')

        df['texto_combinado'] = df[text_columns].agg(' '.join, axis=1)

        return df
    except FileNotFoundError:
        print(f"El archivo en la ruta '{filepath}' no existe.")
        return None
    
if __name__ == "__main__":
    archivo_test = "juegos_prueba.csv"
    
    columnas_a_procesar = ["descripcion", "tags"]

    df_limpio = load_data(archivo_test, columnas_a_procesar)

    if df_limpio is not None:
        print("--- Dataset procesado con éxito ---")
        print(df_limpio[['titulo', 'texto_combinado']].head(2))