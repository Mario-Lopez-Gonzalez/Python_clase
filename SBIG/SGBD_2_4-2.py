import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# Definir los parámetros de la distribución normal
media = 3.2  # media de la distribución
desviacion_estandar = 0.5  # desviación estándar

# 1.- Queremos saber la probabilidad de que un bebé recién nacido pese exactamente 3.5
peso_1 = 3.5
prob_1 = stats.norm.pdf(peso_1, media, desviacion_estandar) # Usamos la pdf para puntos concretos
print(f"La probabilidad de que un bebé pese {peso_1}Kg es de {prob_1*100:.4f}%")

# 2.- ¿Cuál es el peso mínimo que debe tener un recién nacido para que el 80% de los bebés pesen menos que él?
percentil_80 = stats.norm.ppf(0.80, media, desviacion_estandar)
print(f"El valor de altura en el percentil 80 (top 20%) es: {percentil_80:.4f}Kg")