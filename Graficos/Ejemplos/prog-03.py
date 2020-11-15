import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("../../datos/dolar.csv")
meses = df['Mes']
precios1 =df['2010']
precios2 =df['2020']
precios1.index =np.arange(1,13)
precios2.index =np.arange(1,13)
plt.plot(precios1, label = precios1.name, marker='x', linestyle=':', color='b')
plt.plot(precios2, label = precios2.name, marker='o', linestyle='--', color='r')
plt.legend(loc="upper left")
plt.title("Variación del precio del dolar durante el "+ precios1.name + " y " + precios2.name)
plt.xlabel("Mes")
plt.ylabel("Precio")
plt.xticks(precios1.index)
plt.yticks([12,14,16,18,20,22,24,26])
plt.savefig("comparativ.pdf")
plt.show()
