# Leer un archivo csv como lista de diccionarios con
# DictReader() y mostrar sólo datos de algunas columnas:
import csv

archivoCSV=open('../../datos/municipios.csv')

entrada = csv.DictReader(archivoCSV)

for reg in entrada:
    print(reg['nombre'], reg['poblacion'], reg['superficie'])