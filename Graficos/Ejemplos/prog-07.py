import matplotlib.pyplot as plt
partidos = ["PRI", "PAN", "MORENA", "OTROS"]
porcentaje = [19, 26, 52, 3]
expl =(0, 0, 0, .2)
plt.pie(porcentaje, explode=expl,
labels=partidos, shadow=True)
plt.title("Encuesta")
plt.legend()
plt.show()