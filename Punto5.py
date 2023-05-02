#5. Crear una matriz (nxn) con números enteros aleatorios entre 10 y 99 usando la librería numpy.
#   n debe ser ingresado desde el teclado.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Se pide el numero para el tamaño de la matriz
n = int(input("Ingrese el valor de n: "))

#5.1 Se crea y se imprime la matriz
matriz = np.random.randint(10, 100, size=(n, n))
print(matriz)

#Se defiene las matrices diagonales
diag_principal = np.diag(matriz)
diag_secundaria = np.diag(np.fliplr(matriz))[::-1]

#5.2 Se crea el grafico de puntos con las diagoaneles
plt.plot(diag_principal, diag_secundaria, 'o')
plt.xlabel('Diagonal principal')
plt.ylabel('Diagonal secundaria')
plt.show()

#5.3 Se crean y se imprimen las medidas estadisticas
df = pd.DataFrame(matriz)
print(df.describe())
