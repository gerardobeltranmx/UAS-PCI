import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("../../datos/dolar.csv")
meses = df['Mes']
precios =df['2011']
precios.index =np.arange(1,13)
#print (precios)
plt.plot(precios)
plt.title("Variación del precio del dólar durante el año " + precios.name)
plt.xlabel("Mes")
plt.ylabel("Precio")
plt.xticks(precios.index)
plt.yticks([12.2,12.4,12.6,12.8,13,13.2,13.4,13.6])
plt.show()