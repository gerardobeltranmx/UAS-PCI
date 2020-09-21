def sumatoria(*arg):
    s=0
    for valor in arg:
        s = s + valor
    return s

resultado1 = sumatoria(1,2,3,4)
print ("La suma es: ", resultado1)

resultado2 = sumatoria (1,2,3,4,5,6,7)
print ("La suma es: ", resultado2)

resultado2 = sumatoria (1,2,3,4,5,6,7,8,9,11)
print ("La suma es: ", resultado2)