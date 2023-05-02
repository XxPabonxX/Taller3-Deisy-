#1. Elaborar un programa en Python de google colab,
#   que permita ingresar desde el teclado una lista con nombres de personas
#   y de forma paralela una lista con sus correspondientes edades.

!pip install matplotlib

import matplotlib.pyplot as plt

# ingresar la lista de nombres
names = input("Ingrese una lista de nombres separados por comas: ").split(',')

# ingresar la lista de edades
while True:
  ages = input("Ingrese una lista de edades separadas por comas: ").split(',')
  if all(age.isdigit() for age in ages):
    ages = [int(age) for age in ages]
    if len(names) == len(ages):
      break
    else:
      print("La cantidad de nombres y edades debe ser la misma.")
  else:
    print("Ingrese solo números enteros para las edades.")

#1.1 mostrar las dos listas
print("Nombres:", names)
print("Edades:", ages)

#1.2 crear el gráfico de barras
plt.bar(names, ages)
plt.title("Edades de personas")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()

#1.3 crear el gráfico de líneas
plt.plot(names, ages, 'o-')
plt.title("Edades de personas")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()

#1.4 crear el gráfico de puntos
plt.scatter(names, ages)
plt.title("Edades de personas")
plt.xlabel("Nombre")
plt.ylabel("Edad")
plt.show()