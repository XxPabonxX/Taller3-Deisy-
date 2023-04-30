#2.	Elaborar un programa en Python que permita crear una lista con los números enteros 
#   entre -100 y 100  (x) y de forma paralela otra lista con el cubo de x (x**3).

!pip install matplotlib

import matplotlib.pyplot as plt

# Crear una lista con los números enteros entre -100 y 100
x = list(range(-100, 101))

# Crear otra lista con el cubo de x (x**3)
y = [num**3 for num in x]

#2.1 Mostrar las dos listas
print("Lista x: ", x)
print("Lista y: ", y)

#2.2 Mostrar el gráfico de barras
plt.bar(x, y)
plt.title("Gráfico de barras")
plt.xlabel("X")
plt.ylabel("X**3")
plt.show()

#2.3 Mostrar el gráfico de líneas
plt.plot(x, y)
plt.title("Gráfico de líneas")
plt.xlabel("X")
plt.ylabel("X**3")
plt.show()

#2.4 Mostrar el gráfico de puntos
plt.scatter(x, y)
plt.title("Gráfico de puntos")
plt.xlabel("X")
plt.ylabel("X**3")
plt.show()
