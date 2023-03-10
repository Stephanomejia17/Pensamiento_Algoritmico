#Mostrar todos los números impares desde 1 hasta el 300.
suma = 0

for i in range(1,300): 
    if(i % 2 != 0):
        suma = suma + i
print("La suma de los numeros impares hasta 300 es: ", suma)