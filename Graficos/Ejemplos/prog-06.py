import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("../../datos/dolar.csv")
datos = df['Mes']
datos0 = df['2010']
datos1 = df['2015']
datos2 = df['2017']
X = np.arange(12)
plt.bar(X + 0.00, datos0, color = "b", width = 0.25)
plt.bar(X + 0.25, datos1, color = "g", width = 0.25)
plt.bar(X + 0.50, datos2, color = "r", width = 0.25)
plt.xticks(X+0.4, datos)
plt.show()