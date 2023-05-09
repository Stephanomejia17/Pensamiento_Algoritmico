vector = [1,5,12,6,74,56,1,5,62,71]
primos = []

for i in range(0, len(vector)):
    contador = 0
    for j in range(1, vector[i]+1):
        if(vector[i] % j == 0):
            contador += 1
    if(vector[i] == 1):
        primos.append(vector[i])
    elif(contador == 2):
        primos.append(vector[i])
        
for i in range(0, len(primos)):
    print(primos[i])
