#nombre = input("Escribe tu nombre: ")
#i=0
#while ( i <= 10):
#    print(i, " Hola: ", nombre)
#    i=i+1

num = int(input("Ingrese un número: "))
factorial=1
i=1
while (i <= num):
    factorial = factorial * i
    i=i+1

print("El factorial de %d es %d" % (num, factorial))

