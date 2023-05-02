#3.	Elaborar un programa en Python que permita crear una lista con los numeros enteros 
#   entre 1 y 20  (x) y de forma paralela otra lista con enteros aleatorios entre 1 y 6.

!pip install matplotlib

# Importar las librerías necesarias
import random
import numpy as np
import matplotlib.pyplot as plt

# Crear la lista x con los números enteros entre 1 y 20
x = list(range(1, 21))

# Crear la lista y con enteros aleatorios entre 1 y 6
y = [random.randint(1, 6) for i in range(20)]

#3.1 Mostrar las dos listas
print("Lista x:", x)
print("Lista y:", y)

#3.2 Crear el grafico de barras
plt.bar(x, y)
plt.title("Grafico de barras")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

#3.3 Mostrar las medidas estadísticas de la lista y
print("Media:", np.mean(y))
print("Mediana:", np.median(y))
print("Desviacion estandar:", np.std(y))