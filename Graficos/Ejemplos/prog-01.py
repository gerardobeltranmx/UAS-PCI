import matplotlib.pyplot as plt
lista1 = [9,4,3,14,7,11,20,31]
plt.plot(lista1)

plt.title("Título")
plt.xlabel("Abscisa")
plt.ylabel("Ordenada")

#Rótulos eje X
indice = [0,1,2,3,4,5,6,7];
plt.xticks(indice, ["A", "B", "C", "D", "E", "F", "G", "H"])
#Rótulos eje Y
plt.yticks
([0,100,200,300,400])

plt.show()


