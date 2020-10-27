# Leer un archivo y mostrarlo ordenado por primer
# campo con la función itemgetter() del módulo operator:
import csv, operator
archivoCSV = csv.reader(open('../../datos/municipios.csv'))
# salta el encabezado

next(archivoCSV, None)

listaordenada = sorted(archivoCSV, key=lambda x: int(x[2]),reverse=True)
for registro in listaordenada:
    print(registro)

