from pathlib import Path
import joblib
import pandas as pd

def cargar_datos(path,sep=","):
    """
    Carga datos de un archivo csv desde la ruta proporcionada

    Atributos:
    path (str): ruta al archivo csv
    sep (str): separador del csv

    Devuelve:
    Dataframe: Dataframe con la información del csv separada por el separador designado
    """
    return pd.read_csv(path, sep=sep)

def cargar_modelo(path):
    """
    Cargar el modelo preentrenado desde un archivo .pkl
    Devuelve el modelo

    Atributos:
    path (str): ruta al archivo .pkl del modelo

    Devuelve:
    object: modelo cargado con joblib
    """
    return joblib.load(path)

def predecir(modelo, datos_usuario):
    """
    Realizar la predicción con los datos proporcionados

    Atributos:
    modelo (object): modelo cargado con joblib
    datos_usuario (Dataframe): Dataframe con los datos a predecir

    Devuelve:
    list: lista con las predicciones del modelo
    """
    return modelo.predict(datos_usuario)

def main():
    '''
    Función principal para asegurarse que no se ejecuta el archivo como parte de un módulo

    Excepciones:
    FileNotFoundError: error al buscar un archivo con el path designado, comprobar la ruta al archivo
    Exception: error no previsto, consultar información en pantalla
    '''
    try:
        # Definir rutas relativas
        modelo_path = Path("./recursos/modelos/creditcard.pkl")
        datos_path = Path("./datos/creditsample.csv")
        
        # Verificar existencia de los archivos
        if not modelo_path.exists():
            raise FileNotFoundError(f"Modelo no encontrado: {modelo_path}")
        if not datos_path.exists():
            raise FileNotFoundError(f"Datos no encontrados: {datos_path}")
        
        # Cargar el modelo preentrenado
        modelo = cargar_modelo(modelo_path)
        
        # Obtener los datos del usuario
        datos_usuario = cargar_datos(datos_path,";")
        
        # Realizar la predicción
        resultados = predecir(modelo, datos_usuario)
        
        # Mostrar el resultado de la predicción
        for i, resultado in enumerate(resultados):
            if resultado:
                print(f"La predicción para la línea {i} es: NO FRAUDE")
            else:
                print(f"La predicción para la línea {i} es: FRAUDE")
    
    except FileNotFoundError as fnf_error:
        print(f"Archivo no encontrado: {fnf_error}")
    except Exception as e:
        print(f"Se produjo un error: {type(e).__name__} - {e}")

if __name__ == '__main__':
    main()
