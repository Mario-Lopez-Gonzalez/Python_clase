import numpy as np
import pandas as pd
import joblib
import os
from sklearn.impute import SimpleImputer

# Funciones custom

# Funcion para los feature_names_out de age
def age_name(function_transformer, feature_names_in):
    return ["age"]  # feature names out

# Funcion para los feature_names_out de age
def family_name(function_transformer, feature_names_in):
    return ["family"]  # feature names out

# Función para categorizar edades
def categorize_age(X):
    imputer = SimpleImputer(strategy='most_frequent',)
    X_imputed = imputer.fit_transform(X)
    return pd.cut(X_imputed.flatten(), bins=[-1, 16, 32, 48, 64, np.inf], labels=[1, 2, 3, 4, 5]).to_numpy().reshape(-1, 1)

# Función para transformar tamaño de familia
def transform_family(X):
    return (X['sibsp'] + X['parch']).values.reshape(-1, 1)

# Función para cargar el CSV
def load_csv():
    while True:
        file_path = input("Por favor, introduce la ruta del archivo CSV: ")
        if os.path.isfile(file_path):
            try:
                df = pd.read_csv(file_path)
                # Controlar que no contenga la columna 'Survived'
                if 'survived' in df.columns:
                    print("Error: El archivo no debe contener la columna 'survived'.")
                else:
                    return df
            except Exception as e:
                print(f"Error al cargar el archivo: {e}")
        else:
            print("Error: El archivo no existe. Inténtalo de nuevo.")

# Función para cargar el modelo
def load_model(model_path):
    if os.path.isfile(model_path):
        try:
            model = joblib.load(model_path)
            return model
        except Exception as e:
            print(f"Error al cargar el modelo: {e}")
            return None
    else:
        print("Error: El modelo no existe. Asegúrate de que la ruta sea correcta.")
        return None

# Función para realizar la predicción
def make_prediction(model, df):
    try:
        predictions = model.predict(df)
        return predictions
    except Exception as e:
        print(f"Error al realizar la predicción: {e}")
        return None

def main():
    # Cargar el DataFrame desde el CSV
    df = load_csv()

    # Cargar el modelo
    model_path = input("Por favor, introduce la ruta del archivo del modelo (.pkl): ")
    model = load_model(model_path)

    # Si el modelo se carga correctamente, realizar la predicción
    if model is not None:
        predictions = make_prediction(model, df)
        
        if predictions is not None:
            # Mostrar las predicciones
            df['Predictions'] = predictions
            print("Predicciones realizadas:")
            print(df[['Predictions']])
        else:
            print("No se pudieron realizar predicciones.")
    else:
        print("No se pudo cargar el modelo.")

if __name__ == "__main__":
    main()
