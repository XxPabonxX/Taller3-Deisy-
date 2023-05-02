#En el municipio de se está haciendo un estudio sobre pluviosidad medida en milímetros por hora:
#mm/h. y se clasifica así:  

# Débiles: cuando su intensidad es <= 2 mm/h

# Moderadas: > 2 mm/h y <= 15 mm/h

# Fuertes: > 15 mm/h y <= 30 mm/h

# Muy fuertes: >30 mm/h y <= 60 mm/h

# Torrenciales: >60 mm/h 

#Para esto se tomó un área central en el municipio representada por una matriz cuadrada (orden N). 

#Elabore un programa en python que permita calcular y mostrar en pantalla lo siguiente:

#-Crear una matriz de números aleatorios entre 0 y 100, 
#de orden N (Matriz cuadrada. NxN) (N debe ser ingresado desde el teclado). 

#-Mostrar la matriz resultante.

#-Calcular y mostrar el promedio, la desviación estándar,
# la mediana y la moda de pluviosidad para la zona de estudio (matriz).

#-Mostrar un gráfico x,y, en el que x son las categorías D, M, F , MF, T.
# y corresponde a la frecuencia de cada categoría.


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Pedimos al usuario que ingrese el orden N de la matriz cuadrada
N = int(input("Ingrese el orden N de la matriz cuadrada: "))

# Creamos la matriz aleatoria de orden N
matriz = np.random.randint(0, 100, size=(N, N))

# Mostramos la matriz resultante
print("Matriz resultante:\n", matriz)

# Convertimos la matriz en un vector unidimensional
pluviosidad = matriz.flatten()

# Definimos las categorías y sus límites
categorias = ['D', 'M', 'F', 'MF', 'T']
limites = [0, 2, 15, 30, 60, np.inf]

# Calculamos la frecuencia de cada categoría
frecuencia, _ = np.histogram(pluviosidad, bins=limites)

# Mostramos el promedio, la desviación estándar, la mediana y la moda de pluviosidad
promedio = np.mean(pluviosidad)
desviacion_estandar = np.std(pluviosidad)
mediana = np.median(pluviosidad)
moda = stats.mode(pluviosidad).mode[0]

print("Promedio de pluviosidad: {:.2f}".format(promedio))
print("Desviacion estandar de pluviosidad: {:.2f}".format(desviacion_estandar))
print("Mediana de pluviosidad: {:.2f}".format(mediana))
print("Moda de pluviosidad: {:.2f}".format(moda))

# Graficamos la frecuencia de cada categoría
plt.bar(categorias, frecuencia)
plt.xlabel("Categorías de pluviosidad")
plt.ylabel("Frecuencia")
plt.title("Frecuencia de cada categoría de pluviosidad")
plt.show()
