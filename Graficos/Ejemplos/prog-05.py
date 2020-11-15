import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("../../datos/municipios.csv")
municipios = df['nombre']
poblacion =df['poblacion']/1000
plt.bar(poblacion.index, poblacion,color = "g")
plt.xticks(poblacion.index, municipios)
plt.ylabel('Población (miles)')
plt.xlabel('Municipios')
plt.title("Poblacion del Estado de Sinaloa")
plt.show()