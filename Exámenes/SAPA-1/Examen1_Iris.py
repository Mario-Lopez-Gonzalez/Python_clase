import joblib
import pandas as pd

def obtener_datos_usuario():
    """Solicitar datos del usuario y devolverlos en un diccionario."""

    def pedir_decimal_positivo(mensaje):
        """Solicitar un número entero positivo."""
        while True:
            try:
                valor = input(mensaje).strip()
                valor = float(valor)
                if valor <= 0:
                    raise ValueError("El número debe ser mayor a 0")
                return valor
            except ValueError as e:
                print(f"Introduce un número por favor")

    # Solicitar datos al usuario
    spl = pedir_decimal_positivo("Introduce el largo del sépalo en cm: ")
    spw = pedir_decimal_positivo("Introduce el ancho del sépalo en cm: ")
    ptl = pedir_decimal_positivo("Introduce el largo del pétalo en cm: ")
    ptw = pedir_decimal_positivo("Introduce el ancho del pétalo en cm: ")

    # Regresar los datos como un diccionario
    return {
        'sepal length (cm)': spl,
        'sepal width (cm)': spw,
        'petal length (cm)': ptl,
        'petal width (cm)': ptw,
    }


def cargar_modelo(modelo_path):
    """Cargar el modelo preentrenado desde un archivo .pkl"""
    return joblib.load(modelo_path)

def predecir(modelo, datos_usuario):
    """Realizar la predicción con los datos proporcionados."""
    columnas_esperadas = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    input_data = pd.DataFrame([datos_usuario], columns=columnas_esperadas)
    result = ""
    if modelo.predict(input_data) == 0:
        result = "Clase 1"
    elif modelo.predict(input_data) == 1:
        result = "Clase 2"
    elif modelo.predict(input_data) == 2:
        result = "Clase 3"
    else:
        result = "ERROR"
    return result

def main():
    try:
        # Ruta del modelo preentrenado
        modelo_path = './Examen1_Iris.pkl'  # Ruta al archivo del modelo
        
        # Cargar el modelo preentrenado
        modelo = cargar_modelo(modelo_path)
        
        # Obtener los datos del usuario
        datos_usuario = obtener_datos_usuario()
        
        # Realizar la predicción
        resultado = predecir(modelo, datos_usuario)
        
        # Mostrar el resultado de la predicción
        print(f"La predicción para los datos proporcionados es: {resultado}")
    
    except FileNotFoundError:
        print("Error: No se encontró el archivo del modelo. Verifica la ruta proporcionada.")
    except Exception as e:
        print("Algo salió mal. Por favor, intente nuevamente.")
        # Para depuración, puedes imprimir detalles del error:
        # print(f"Detalle del error: {e}")

if __name__ == '__main__':
    main()

