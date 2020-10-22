import sys

if len(sys.argv)>1 :
    linea = sys.argv[1]
    datos = linea.split(";")
    archivo=open("sinaloa.txt", "a")
    archivo.write(datos[0]+","+ datos[1]+","+datos[2]+","+datos[3]+","+ datos[4]+"\n")
    archivo.close()
else:
    print("Debe indicar datos para guardar")

