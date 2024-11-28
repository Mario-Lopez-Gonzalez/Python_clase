import joblib
import pandas as pd

def obtener_datos_usuario():
    """Solicitar datos del usuario y devolverlos en un diccionario."""

    def pedir_cadena(mensaje):
        """Solicitar una cadena no vacía."""
        while True:
            try:
                valor = input(mensaje).strip()
                if not valor:
                    raise ValueError("El campo no puede estar vacío")
                return valor
            except ValueError as e:
                print(f"Error: {e}. Por favor, inténtalo de nuevo.")

    def pedir_entero_positivo(mensaje):
        """Solicitar un número entero positivo."""
        while True:
            try:
                valor = input(mensaje).strip()
                if not valor.isdigit():  # Validar si el input es numérico
                    raise ValueError("El valor debe ser un número entero positivo")
                valor = int(valor)
                if valor <= 0:
                    raise ValueError("El número debe ser mayor a 0")
                return valor
            except ValueError as e:
                print(f"Error: {e}. Por favor, inténtalo de nuevo.")

    # Solicitar datos al usuario
    car = pedir_cadena("Introduce tu marca de coche: ")
    model = pedir_cadena("Introduce tu modelo de coche: ")
    volume = pedir_entero_positivo("Introduce el volumen de tu coche (en litros): ")
    weight = pedir_entero_positivo("Introduce el peso de tu coche (en kilogramos): ")

    # Regresar los datos como un diccionario
    return {
        'Car': car,
        'Model': model,
        'Volume': volume,
        'Weight': weight,
    }


def cargar_modelo(modelo_path):
    """Cargar el modelo preentrenado desde un archivo .pkl"""
    return joblib.load(modelo_path)

def predecir(modelo, datos_usuario):
    """Realizar la predicción con los datos proporcionados."""
    columnas_esperadas = ['Car', 'Model', 'Volume', 'Weight']
    input_data = pd.DataFrame([datos_usuario], columns=columnas_esperadas)
    return modelo.predict(input_data)

def main():
    try:
        # Ruta del modelo preentrenado
        modelo_path = './modelo2_11CO2.pkl'  # Ruta al archivo del modelo
        
        # Cargar el modelo preentrenado
        modelo = cargar_modelo(modelo_path)
        
        # Obtener los datos del usuario
        datos_usuario = obtener_datos_usuario()
        
        # Realizar la predicción
        resultado = predecir(modelo, datos_usuario)
        
        # Mostrar el resultado de la predicción
        print(f"La predicción para los datos proporcionados es: {resultado[0]}")
    
    except FileNotFoundError:
        print("Error: No se encontró el archivo del modelo. Verifica la ruta proporcionada.")
    except Exception as e:
        print("Algo salió mal. Por favor, intente nuevamente.")
        # Para depuración, puedes imprimir detalles del error:
        # print(f"Detalle del error: {e}")

if __name__ == '__main__':
    main()

