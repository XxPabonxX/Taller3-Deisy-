#!pip install matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Definir los datos de producción
produccion = {"maquina1": [6261,205,6801,4314,9262,6165,9277,4593,1764,1021,1988,6044],
              "maquina2": [7221,7173,5094,3046,9015,1014,9332,2368,2904,5397,3178,8315],
              "maquina3": [5709,6517,7133,1593,3361,4380,2928,916,6232,4138,7420,1848],
              "maquina4": [4486,5993,4439,1242,8915,5556,3573,7995,1130,2718,2767,5761],
              "maquina5": [1647,604,1902,5101,9209,814,5167,6224,261,6273,8390,3492],
              "maquina6": [5989,870,2198,9754,8396,6389,6451,5137,2051,7871,7708,7600],
              "maquina7": [2850,1904,2362,846,8823,5989,108,9192,2417,6382,2469,9150],}

# Crear un DataFrame a partir de los datos de producción
df = pd.DataFrame(produccion)

# Calcular las medidas estadísticas básicas para cada máquina
medidas = df.describe()
print(medidas)

# Generar el gráfico de barras para la máquina3
ax = df['maquina3'].plot.bar(x=df.index, y='maquina3', rot=0)
ax.set_xlabel("Mes")
ax.set_ylabel("Unidades producidas")
ax.set_title("Producción de la máquina3 por mes")
plt.show()