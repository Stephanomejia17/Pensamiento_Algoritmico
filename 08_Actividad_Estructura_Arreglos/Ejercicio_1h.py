vector = []
pares =[]
impares = []

for i in range(0,20):
    valor = int(input("Ingrese un valor: "))
    vector.append(valor)


for i in range(0, len(vector)):
    if(vector[i] % 2 == 0):
        pares.append(vector[i])
        
    else:
        impares.append(vector[i])
        


for i in range(0, len(pares)):
    print(pares[i])
for i in range(0, len(impares)):
    print(impares[i])
    