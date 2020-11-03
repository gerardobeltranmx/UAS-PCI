import statistics as stats

edades = [22, 23, 26, 26, 26, 34, 34, 38, 40, 41]

print("Media aritmetica: ", stats.mean(edades))
print("Mediana: ", stats.median(edades))
print("Moda: ", stats.mode(edades))
print("Varianza: ", stats.variance(edades))
print("Desviacion standard: ", stats.stdev(edades))

