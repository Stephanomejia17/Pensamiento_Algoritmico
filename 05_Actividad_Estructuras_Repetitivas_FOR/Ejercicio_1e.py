#Calcule la suma de los números pares que están entre el 10 y 2, empezando por
#el 10 y sumando sucesivamente 8,6,…, 2.
sum = 0
for i in range(10,0,-2):
    sum = sum +i
    
print("Suma: ", sum)