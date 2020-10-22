import sys
if(len(sys.argv) > 2):
   num1  = int (sys.argv[1])
   num2  = int (sys.argv[2])
   suma = num1 +  num2 
   print ("La suma es: ", suma)
else:
   print ("Debes indicar 2 numeros para sumar")