import sys
#archivo = open("../../datos/municipios.txt","r")
archivo = open(sys.argv[1],"r")
suma=0
linea = archivo.readline()
while linea:
    datos = linea.split(",")
    suma = suma + int(datos[2])
    linea = archivo.readline()

print("La superficie es:", suma)

