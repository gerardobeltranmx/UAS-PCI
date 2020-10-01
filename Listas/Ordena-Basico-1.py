N = int (input())

linea = input().split(" ")
print (linea)

datos = [int(dato) for dato in linea]
print (datos)

datos.sort()

for dato in datos: 
    print(dato)

