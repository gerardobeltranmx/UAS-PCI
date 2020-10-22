import sys
archivo = open ("datos.txt","a")
archivo.write(sys.argv[1]+ "\n")
archivo.write(sys.argv[2]+ "\n")
archivo.close()