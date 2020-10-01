N = int (input())

# Entrada de datos
linea = input().split(" ")

# Conversión a Enteros de la lista
datos = [int(dato) for dato in linea]
# Ordenamiento de los datos
datos.sort()
# Salida de los datos
for dato in datos: 
    print(dato)

