# Obtener lista ordenada descendente por el campo nombre
# con la función itemgetter() del módulo operator.
import csv, operator
archivoCSV = open('../../datos/municipios.csv')
entrada = csv.DictReader(archivoCSV)

listadicc = list(entrada) # Obtener lista de diccionarios

listadiccord = sorted(listadicc,key=operator.itemgetter('nombre'),reverse=False)

for registro in listadiccord:
  print(registro)

del entrada, listadicc, listadiccord

archivoCSV.close()
del archivoCSV