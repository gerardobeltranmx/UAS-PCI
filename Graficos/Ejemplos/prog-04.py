import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("../../datos/municipios.csv")
municipios = df['nombre']
poblacion =df['poblacion']/1000
plt.barh(poblacion.index, poblacion)
plt.yticks(municipios.index, municipios)
plt.xlabel('Población (miles)')
plt.ylabel('Municipios')
plt.title("Poblacion del Estado de Sinaloa")
plt.show()

