from joblib import load
import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Si no importo todas las class custom peta

# Clase para codificar el sexo
class SexEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.le = LabelEncoder()
        self.le.fit(X.to_numpy().ravel())  # Necesario array 1D
        return self

    def transform(self, X):
        return self.le.transform(X.values.ravel()).reshape(-1, 1)
    
    def get_feature_names_out(self, input_features=None):
        return np.array(['sex_encoded'])  # Devuelve nombre columna

# Clase para procesar la edad
class AgeEncoder(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.imputer = SimpleImputer(strategy='most_frequent')  # Rellenar valores faltantes con la moda
        self.imputer.fit(X)  # Ajustar el imputador
        return self

    def transform(self, X):
        X_imputed = self.imputer.transform(X)
        # Categorizamos las edades en grupos
        age_bins = [0, 16, 32, 48, 64, np.inf]  # Definir los límites de los grupos
        age_labels = [1, 2, 3, 4, 5]  # Etiquetas para los grupos
        return pd.cut(X_imputed.flatten(), bins=age_bins, labels=age_labels).to_numpy().reshape(-1, 1)
    
    def get_feature_names_out(self, input_features=None):
        return np.array(['age_encoded'])

# Clase para crear la columna 'family'
class FamilySizeTransformer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        self.imputer = SimpleImputer(strategy='most_frequent')  # Rellenar valores faltantes con la moda
        self.imputer.fit(X)  # Ajustar el imputador
        return self

    def transform(self, X):
        return (X['sibsp'] + X['parch']).to_numpy().reshape(-1, 1)

    def get_feature_names_out(self, input_features=None):
        return np.array(['family_transformed'])  # Nombre de la nueva columna

# Clase para procesar el puerto de embarque
class EmbarkedTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.imputer = SimpleImputer(strategy='most_frequent')  # Rellenar valores faltantes con la moda
        self.encoder = OneHotEncoder(sparse_output=False)  # Configuración para obtener un array denso

    def fit(self, X, y=None):
        # Ajustar el imputador a los datos
        self.imputer.fit(X)
        # Ajustar el codificador a los datos imputados
        X_imputed = self.imputer.transform(X)
        self.encoder.fit(X_imputed)
        return self

    def transform(self, X):
        # Rellenar valores faltantes primero
        X_imputed = self.imputer.transform(X)
        # Transformar los datos
        transformed_data = self.encoder.transform(X_imputed)
        # Obtener los nombres de las columnas codificadas
        column_names = self.encoder.get_feature_names_out(input_features=X.columns)
        return pd.DataFrame(transformed_data, columns=column_names, index=X.index)

    def get_feature_names_out(self, input_features=None):
        return self.encoder.get_feature_names_out()  # Obtener los nombres de las columnas codificadas
    

# Cargar el modelo de randomforest
modelo = load('SAPA/Ejercicios/modelo_random_forest.joblib')

# Cargar el csv
df = pd.read_csv("SAPA/Ejercicios/datos/titanic_test_data.csv")

# Hacer predicciones
predict = modelo.predict(df)

# Añadimos la prediccion
df["survived"] = predict

# Imprimimos
print(df)
