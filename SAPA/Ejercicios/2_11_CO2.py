import joblib
import pandas as pd

def obtener_datos_usuario():
    # Pedir al usuario los datos de entrada
    ok = False
    while ok == False:
        try:
            car = input("Introduce tu marca de coche: ").strip()
            if not car:
                raise ValueError("La marca del coche no puede estar vacía.")
            
            model = input("Introduce tu modelo de coche: ").strip()
            if not model:
                raise ValueError("El modelo del coche no puede estar vacío.")
            
            volume = input("Introduce el volumen de tu coche (en litros): ").strip()
            volume = int(volume)  # Convertir a número, lanza ValueError si no es válido
            if volume <= 0:
                raise ValueError("El volumen debe ser un número entero positivo.")
            
            weight = input("Introduce el peso de tu coche (en kilogramos): ").strip()
            weight = int(weight)  # Convertir a número, lanza ValueError si no es válido
            if weight <= 0:
                raise ValueError("El peso debe ser un número entero positivo.")
            
            # Si todo es válido, salir del bucle
            ok = True
        
        except ValueError as e:
            print(f"Error: {e}. Por favor, inténtalo de nuevo.")
    
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
    # Ruta del modelo preentrenado
    modelo_path = '/home/iabd/Documentos/Python_clase/SAPA/Ejercicios/modelo2_11CO2.pkl'  #NOTE Ruta al archivo del modelo
    
    # Cargar el modelo preentrenado
    modelo = cargar_modelo(modelo_path)
    
    # Obtener los datos del usuario
    datos_usuario = obtener_datos_usuario()
    
    # Realizar la predicción
    resultado = predecir(modelo, datos_usuario)
    
    # Mostrar el resultado de la predicción
    print(f"La predicción para los datos proporcionados es: {resultado[0]}")
    
if __name__ == '__main__':
    main()