import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros de la distribución normal
media = 1.90  # media de la distribución
desviacion_estandar = 0.10  # desviación estándar

# 1. ¿¿Cuál es la probabilidad de que un jugador seleccionado al azar mida más de 2 metros?
altura_1 = 2.00
probabilidad_1 = 1 - stats.norm.cdf(altura_1, media, desviacion_estandar) # Aplicamos 1 - x para sacar la inversa
print(f"Probabilidad de que la altura sea mayor a {altura_1} metros: {probabilidad_1*100:.4f}%")

# 2. ¿Cuál es la probabilidad de que un jugador seleccionado al azar mida menos de 1.85m?
altura_2 = 1.85
probabilidad_2 = stats.norm.cdf(altura_2, media, desviacion_estandar)
print(f"Probabilidad de que la altura sea mayor a {altura_2} metros: {probabilidad_2*100:.4f}%")

# 3. ¿Cuál es la probabilidad de que un jugador seleccionado al azar mida: 1.85 <=altura<= 2m?
altura_3_min = 1.85
altura_3_max = 2.00
probabilidad_3 = stats.norm.cdf(altura_3_max, media, desviacion_estandar) - stats.norm.cdf(altura_3_min, media, desviacion_estandar)
print(f"Probabilidad de que la altura sea entre {altura_3_min} metros y {altura_3_max} metros: {probabilidad_3*100:.4f}%")

# 4. Crear gráfico:

# Rango del eje X (media - 3 * desviación_estándar, media + 3 * desviación_estándar)
x = np.linspace(media - 3 * desviacion_estandar, media + 3 * desviacion_estandar, 1000)

# Función de densidad de probabilidad para la distribución normal
y = stats.norm.pdf(x, media, desviacion_estandar)

# Crear el gráfico
plt.plot(x, y, label=f'N({media}, {desviacion_estandar}^2)', color='b')

# Título y etiquetas
plt.title('Distribución Normal')
plt.xlabel('Altura (metros)')
plt.ylabel('Densidad de Probabilidad')

# Añadir la media al gráfico
plt.axvline(media, color='r', linestyle='--', label=f'Media = {media}')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()