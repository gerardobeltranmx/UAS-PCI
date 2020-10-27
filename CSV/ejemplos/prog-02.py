import csv
# Abrir archivo csv
archivoCSV = open('../../datos/municipios.csv')
# Leer todos los registros
entrada = csv.reader(archivoCSV)
# Muestrar campos
for nombre, poblacion, superficie in entrada:
    print(nombre, poblacion, superficie)
    # Borrar objetos
del nombre, poblacion, superficie, entrada
# Cerrar archivo
archivoCSV.close()
# Borrar objeto
del archivoCSV