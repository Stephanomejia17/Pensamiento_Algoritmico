#Imprimir el promedio de una lista de 100 números.
sum = 0
cont = 0
for i in range(0, 100):
    sum = sum + i
    cont = cont + 1
print("La suma de los valores son: ", sum)
print("La cantidad de numeros sumados son: ", cont)
print("El promedio es: ", sum/cont)