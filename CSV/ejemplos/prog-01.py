# Leer el archivo con reader() y
# muestrar todos los registros, uno a uno:
import csv
# Abrir archivo csv
archivoCSV=open('../../datos/municipios.csv')
# Leer todos los registros
entrada = csv.reader(archivoCSV)
# Cada línea se muestra como una lista de campos
for registro in entrada:
    print(registro)