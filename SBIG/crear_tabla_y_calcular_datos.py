# Importamos librerías
import pandas as pd
import numpy as np

# Preguntamos al usuario formato de datos
choice = "foo"
while choice not in ["1", "2"]:
    print(choice)
    choice = input("Elige 1 para meter los datos o 2 para meter la xi y ni de los datos: ")

if choice == "1": # Solo datos
    raw = input("Introduce los datos separados por comas: ")
    data = [int(x) for x in raw.split(',')]
elif choice == "2": # xi y ni
    raw_xi = input("Introduce xi separados por comas: ")
    xi = [int(x) for x in raw_xi.split(',')]
    x_i = np.array(xi)
    raw_ni = input("Introduce ni separados por comas: ")
    ni = [int(x) for x in raw_ni.split(',')]
    n_i = np.array(ni)
    data = np.repeat(x_i,n_i) # Creamos el array de datos a partir de xi y ni

# Creamos un DataFrame para Numpy
df = pd.DataFrame(data, columns=['Values'])

# Sacamos las frecuencias sacando las repeticiones del dataframe en values y guardandolo en un diccionario por clave xi y valor ni
frequency = df['Values'].value_counts().sort_index()

# Separamos el diccionario en listas xi y ni para manejo de datos
x_i = frequency.index.to_numpy()
n_i = frequency.values

# Sacamos el total de valores o la población (N)
total = n_i.sum()

# Sacamos Ni con la función cumsum que suma todos los valores hasta el actual
N_i = np.cumsum(n_i)

# Sacamos fi y Fi con los porcentajes
f_i_percent = (n_i / total) * 100
F_i_percent = np.cumsum(f_i_percent)

# Rellenamos el DataFrame con los datos
result_df = pd.DataFrame({
    'x_i': x_i,
    'n_i': n_i,
    'N_i': N_i,
    'f_i (%)': f_i_percent,
    'F_i (%)': F_i_percent
})

# Calculamos la media, varianza y desviación típica
average = np.average(x_i, weights=n_i)
variance = np.average((x_i - average) ** 2, weights=n_i)
std_dev = np.sqrt(variance)

# Sacamos la moda contando la cantidad de repeticiones por valor
values, counts = np.unique(data, return_counts=True)
max_count_index = np.argmax(counts)
mode = values[max_count_index]

# Sacamos los percentiles y la mediana que siempre es el percentil del 50%
Q1 = np.percentile(data, 25)
Q2 = np.percentile(data, 50)
Q3 = np.percentile(data, 75)
RIQ = Q3-Q1
median = Q2

# Calculamos los límites inferior y superior para sacar los outliers
inf_lim = Q1 - 1.5 * RIQ
sup_lim = Q3 + 1.5 * RIQ
outliers = [x for x in data if x < inf_lim or x > sup_lim]

# Imprimimos la tabla de frecuencias
print("Tabla de frecuencias:")
print(result_df)

# Imprimimos las estadísticas
print("\nEstadísticas:")
print(f"Moda: {mode}")
print(f"Mediana: {median}")
print(f"Media: {average:.2f}")
print(f"Varianza: {variance:.2f}")
print(f"Deviación estándar: {std_dev:.2f}")
print(f"Q1 (25%): {Q1}")
print(f"Q2 (50%): {Q2}")
print(f"Q3 (75%): {Q3}")
print(f"Rango intercuartílico: {RIQ}")
print(f"Límite inferior: {inf_lim}")
print(f"Límite superior: {sup_lim}")
if len(outliers) == 0:
    print("No hay outliers")
else:
    print(f"Los outliers son: {outliers}")