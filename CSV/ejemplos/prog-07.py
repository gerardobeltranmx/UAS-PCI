# Obtener lista ordenada descendente por el campo poblacion
# con la función itemgetter() del módulo operator.
import csv, operator

archivoCSV = open('../../datos/municipios.csv')

entrada = csv.DictReader(archivoCSV)

listadicc = list(entrada) # Obtener lista de diccionarios

listadiccord = sorted(listadicc, key=lambda x: int(x['superficie']), reverse=True)

for registro in listadiccord:
  print(registro['nombre'], "" , registro['poblacion'], registro['superficie'])

del entrada, listadicc, listadiccord

archivoCSV.close()

del archivoCSV