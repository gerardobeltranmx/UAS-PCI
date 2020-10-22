import sys

if (len(sys.argv) > 1):
    radio = float (sys.argv[1])
    area = 3.1416 * radio**2
    print ("El area es ", area)
else:
    print("Debe indicar el radio")
    print ("Ejemplo: $ python3 ", sys.argv[0], "10")
        
