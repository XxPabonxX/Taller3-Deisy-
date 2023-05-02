import numpy as np
import matplotlib.pyplot as plt

# Matriz con información de las subregiones
subregiones = np.array([
    ['VALLE DE ABURRÁ', '01', 10],
    ['BAJO CAUCA', '02', 6],
    ['MAGDALENA MEDIO', '03', 6],
    ['NORDESTE', '04', 10],
    ['NORTE', '05', 17],
    ['OCCIDENTE', '06', 19],
    ['ORIENTE', '07', 23],
    ['SUROESTE', '08', 23],
    ['URABÁ', '09', 11]
])

# Matriz de temperaturas aleatorias
temperaturas = np.random.randint(15, 31, size=(9, 12))

# Mostrar las dos matrices en forma paralela
print("Matriz de subregiones:")
print(subregiones)
print("\nMatriz de temperaturas:")
print(temperaturas)

# Promedio de temperatura por subregión
prom_subregion = np.mean(temperaturas, axis=1)
print("\nPromedio de temperatura por subregión:")
for i in range(len(prom_subregion)):
    print(f"{subregiones[i][0]} ({subregiones[i][1]}): {prom_subregion[i]:.2f}")

# Promedio de temperatura por mes
prom_mes = np.mean(temperaturas, axis=0)
print("\nPromedio de temperatura por mes:")
for i in range(len(prom_mes)):
    print(f"Mes {i+1}: {prom_mes[i]:.2f}")

# Promedio de temperatura para todo el departamento
prom_dept = np.mean(temperaturas)
print("\nPromedio de temperatura para todo el departamento:", prom_dept)

# Gráfico subregión vs promedio de temperatura
plt.bar(subregiones[:, 0], prom_subregion)
plt.title("Promedio de temperatura por subregión")
plt.xlabel("Subregión")
plt.ylabel("Promedio de temperatura")
plt.xticks(rotation=90)
plt.show()

# Gráfico mes vs promedio de temperatura
plt.plot(prom_mes)
plt.title("Promedio de temperatura por mes")
plt.xlabel("Mes")
plt.ylabel("Promedio de temperatura")
plt.show()