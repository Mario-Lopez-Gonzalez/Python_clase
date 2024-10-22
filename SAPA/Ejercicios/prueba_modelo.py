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

# Crear el csv con datos reales y falsos y cargar

import pandas as pd
import seaborn as sns
import numpy as np

# definimos N
N = 100

# Cargar el conjunto de datos del Titanic
titanic = sns.load_dataset('titanic')

# Obtener 20 filas aleatorias
random_sample = titanic.sample(n=N)

# Renombrar la columna 'survived' a 'real_survived'
random_sample = random_sample.rename(columns={'survived': 'real_survived'})

# Crear un DataFrame con valores aleatorios
new_random_data = pd.DataFrame({
    'pclass': np.random.choice([1, 2, 3], size=N),  # Clase del pasajero
    'sex': np.random.choice(['male', 'female'], size=N),  # Sexo
    'age': np.random.randint(1, 80, size=N),  # Edad
    'sibsp': np.random.randint(0, 5, size=N),  # Hermanos/esposos a bordo
    'parch': np.random.randint(0, 5, size=N),  # Padres/hijos a bordo
    'fare': np.random.uniform(0, 500, size=N),  # Tarifa pagada
    'embarked': np.random.choice(['C', 'Q', 'S'], size=N),  # Puerto de embarque
})

# Establecer NaN en la columna 'real_survived'
new_random_data['real_survived'] = np.nan

# Combinar los dos DataFrames
df = pd.concat([random_sample, new_random_data], ignore_index=True)

# Guardar el DataFrame combinado en un archivo CSV
df.to_csv('SAPA/Ejercicios/datos/titanic_random_sample.csv', index=False)

# Cargamos csv y purgamos
df = pd.read_csv('SAPA/Ejercicios/datos/titanic_random_sample.csv')
df.drop(columns=["class","who","adult_male","deck","embark_town","alive","alone"], inplace=True)

# Hacer predicciones
predict = modelo.predict(df)

# Añadimos la prediccion
df["survived"] = predict

# Reordenar columnas
columns_order = [col for col in df.columns if col not in ['real_survived', 'survived']] + ['real_survived', 'survived']
df = df[columns_order]
# Filas aleatorias
df = df.sample(frac=1, random_state=1).reset_index(drop=True)

# Imprimimos
print(df)

# Calcular el número total de coincidencias
total_matches = (df['real_survived'] == df['survived']).sum()

# Calcular el número total de filas que no tienen NaN en 'real_survived'
total_valid = df['real_survived'].notna().sum()

# Calcular el porcentaje de acierto
if total_valid > 0:
    accuracy_percentage = (total_matches / total_valid) * 100
else:
    accuracy_percentage = 0

# Mostrar el porcentaje de acierto
print(f"El porcentaje de acierto entre 'real_survived' y 'survived' es: {accuracy_percentage:.2f}%")
