#7.	Para el estudio de una zona del municipio, se cuenta con una matriz de n filas y m columnas.
#   Cada dato en posición fila, columna corresponde al número de habitantes en el área de la celda. 
#   De acuerdo a lo anterior, se necesita un programa en python que:
    
#•	Permita crear una matriz de n filas por m columnas con datos aletorios entre 0 y 1000.
#   N y m deben ser ingresados desde el teclado. Mostrar la matriz resultante

#•	Crear una nueva matriz de cadenas de caracteres (String) así:
    
#•	Si la celda en posición fila,columna de la primera matriz, contiene un número de habitantes entre 500 y 1000,
#   escribir en la matriz de cadenas en posición fila,columna, la letra “r” de “rojo”.

#•	Si la celda en posición fila,columna de la primera matriz, contiene un número de habitantes entre 250 y 499, 
#   escribir en la matriz de cadenas en posición fila,columna, la letra “a” de “amarillo”.

#•	Si la celda en posición fila,columna de la primera matriz, contiene un número de habitantes entre 0 y 249,
#   escribir en la matriz de cadenas en posición fila,columna, la letra “v” de “verde”.

#•	Mostrar la nueva matriz.


import numpy as np

# Ingresar n y m desde el teclado
n = int(input("Ingrese el número de filas: "))
m = int(input("Ingrese el número de columnas: "))

# Crear la matriz aleatoria
matriz_habitantes = np.random.randint(0, 1001, size=(n, m))
print("Matriz de habitantes:")
print(matriz_habitantes)

# Crear la matriz de cadenas de caracteres
matriz_colores = np.empty((n, m), dtype='U1')
for i in range(n):
    for j in range(m):
        habitantes = matriz_habitantes[i][j]
        if habitantes >= 500:
            matriz_colores[i][j] = "r"
        elif habitantes >= 250:
            matriz_colores[i][j] = "a"
        else:
            matriz_colores[i][j] = "v"

print("Matriz de colores:")
print(matriz_colores)
