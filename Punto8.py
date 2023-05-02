#8.	Se tiene una matriz de f filas y c columnas, que representan las calles (filas) y las carreras (columnas) de un sector de la ciudad.
#   Las celdas representan cuadras. En cada celda, inicialmente de almacena de manera aleatoria un 0 ó 1.
#   Una vez se tiene la matriz de ceros y unos, cada valor de cero,
#   se deja en cero y cada valor de 1 se reemplaza por un valor aleatorio entre 100 y 999,
#   cada uno de los cuales representa la placa de un vehículo ubicado en esa cuadra. 
#   Se parte del supuesto que todas las calles y todas las carreras se circulan en ambos sentidos (Bidireccional)

#Elaborar un programa en Python que permita

#•	Mostrar la matriz resultante.
#•	Mostrar El número de vehículos que están circulando en ese momento por ese sector de la ciudad.
#•	Tomando como base al celda en posición 0,0 (fila,columna),
#   elaborar un gráfico x,y de la distancia en cuadras de cada vehículo a la celda (0,0) de la matriz.


import numpy as np
import matplotlib.pyplot as plt

# Ingresar f y c desde el teclado
f = int(input("Ingrese el numero de calles (filas): "))
c = int(input("Ingrese el numero de carreras (columnas): "))

# Crear la matriz aleatoria de 0's y 1's
matriz = np.random.randint(0, 2, size=(f, c))

# Reemplazar los 1's por placas aleatorias entre 100 y 999
matriz[matriz == 1] = np.random.randint(100, 1000, size=np.count_nonzero(matriz))

# Mostrar la matriz resultante
print("Matriz de vehiculos:")
print(matriz)

# Calcular el número de vehículos circulando
num_vehiculos = np.count_nonzero(matriz)
print(f"uúmero de vehículos circulando: {num_vehiculos}")

# Calcular las distancias de cada vehículo a la celda (0,0)
distancias = np.empty_like(matriz, dtype=float)
for i in range(f):
    for j in range(c):
        distancias[i][j] = np.sqrt(i**2 + j**2)

# Crear el gráfico de distancias
plt.figure()
plt.title("Distancia de los vehiculos a la celda (0,0)")
plt.xlabel("Carreras")
plt.ylabel("Calles")
plt.imshow(distancias, cmap="coolwarm")
plt.colorbar()
plt.show()