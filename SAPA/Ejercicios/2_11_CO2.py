import joblib
import pandas as pd

def obtener_datos_usuario():
    # Pedir al usuario los datos de entrada
    car = input("Introduce tu marca de coche: ")
    model = input("Introduce tu modelo de coche: ")
    volume = input("Introduce el volumen de tu coche: ")
    weight = input("Introduce el peso de tu coche: ")
    
    # Regresar los datos como un diccionario
    return {
        'Car': car,
        'Model': model,
        'Volume': volume,
        'Weight': weight,
    }

def cargar_modelo(modelo_path):
    # Cargar el modelo preentrenado desde un archivo .pkl
    return joblib.load(modelo_path)

def predecir(modelo, datos_usuario):
    # Convertir los datos a un DataFrame con las mismas columnas que el modelo espera
    columnas_esperadas = ['Car','Model','Volume','Weight']
    input_data = pd.DataFrame([datos_usuario], columns=columnas_esperadas)
    
    # Realizar la predicción
    prediccion = modelo.predict(input_data)
    
    return prediccion

def main():
    try:
        # Ruta del modelo preentrenado
        modelo_path = '.\SAPA\Ejercicios\modelo2_11CO2.pkl'  #NOTE Ruta al archivo del modelo
        
        # Cargar el modelo preentrenado
        modelo = cargar_modelo(modelo_path)
        
        # Obtener los datos del usuario
        datos_usuario = obtener_datos_usuario()
        
        # Realizar la predicción
        resultado = predecir(modelo, datos_usuario)
        
        # Mostrar el resultado de la predicción
        print(f"La predicción para los datos proporcionados es: {resultado[0]}")
    
    except Exception as e:
        print("Algo salió mal. Por favor, intente nuevamente.")

if __name__ == '__main__':
    main()
