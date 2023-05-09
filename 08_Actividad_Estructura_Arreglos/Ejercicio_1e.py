pares = []
impares = []

for i in range(1, 11):
    if(i % 2 == 0):
        pares.append(i)
    else:
        impares.append(i)
        
for i in range(0, len(pares)):
    print(pares[i])
for i in range(0, len(impares)):
    print(impares[i])
    