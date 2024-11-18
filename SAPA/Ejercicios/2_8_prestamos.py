import joblib
import pandas as pd

def obtener_datos_usuario():
    # Pedir al usuario los datos de entrada
    int_rate = float(input("Introduce la tasa de interés (int_rate): "))
    installment = float(input("Introduce el monto de la cuota mensual (installment): "))
    fico = float(input("Introduce el puntaje de crédito FICO (fico): "))
    revol_bal = float(input("Introduce el saldo de crédito revolvente (revol_bal): "))
    revol_util = float(input("Introduce el porcentaje de utilización del crédito revolvente (revol_util): "))
    inq_last_6mths = float(input("Introduce el número de consultas crediticias en los últimos 6 meses (inq_last_6mths): "))
    pub_rec = int(input("Introduce el número de registros públicos (pub_rec): "))
    purpose = input("Introduce el propósito del préstamo ('debt_consolidation', 'credit_card', 'all_other', 'home_improvement', 'small_business', 'major_purchase', 'educational'): ")
    credit_policy = float(input("Introduce la cantidad de política de crédito (credit_policy): "))
    
    # Regresar los datos como un diccionario
    return {
        'int.rate': int_rate,
        'installment': installment,
        'fico': fico,
        'revol.bal': revol_bal,
        'revol.util': revol_util,
        'inq.last.6mths': inq_last_6mths,
        'pub.rec': pub_rec,
        'purpose': purpose,
        'credit.policy': credit_policy
    }

def cargar_modelo(modelo_path):
    # Cargar el modelo preentrenado desde un archivo .pkl
    return joblib.load(modelo_path)

def predecir(modelo, datos_usuario):
    # Convertir los datos a un DataFrame con las mismas columnas que el modelo espera
    columnas_esperadas = ['int.rate', 'installment', 'fico', 'revol.bal', 'revol.util', 'inq.last.6mths', 'pub.rec', 'purpose', 'credit.policy']
    input_data = pd.DataFrame([datos_usuario], columns=columnas_esperadas)
    
    # Realizar la predicción
    prediccion = modelo.predict(input_data)
    
    return prediccion

def main():
    # Ruta del modelo preentrenado (asegúrate de cambiar esta ruta a la ubicación de tu archivo .pkl)
    modelo_path = '/home/iabd/Documentos/Python_clase/SAPA/Ejercicios/modelo2_8Prestamos.pkl'  # Ruta al archivo del modelo
    
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
