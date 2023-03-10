"""
Diseñe un algoritmo para determinar la suma de los números cuya última cifra es
siete y están comprendidos entre dos números M y N ingresados por el usuario.
"""
M = int(input("Ingrese un valor: "))
N = int(input("Ingrese el segundo valor: "))

if(M > N):
    May = M
    men = N
else:
    May = N
    men = M
sum = 0
for i in range(men,May):
    if(i % 10 == 7):
        sum = sum + i
print("La suma es: ", sum)

