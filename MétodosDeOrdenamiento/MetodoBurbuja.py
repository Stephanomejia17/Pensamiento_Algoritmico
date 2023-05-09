vect = []
tamanio = int(input("Ingrese el tamaño del vector: "))

for i in range(0, tamanio):
    valor = int(input("Ingrese un valor: "))
    vect.append(valor)


for i in range(0, tamanio):
    for j in range(0, i+1):
        aux = 0
        if(vect[i] < vect[j]):
            aux = vect[j]
            vect[j] = vect[i]
            vect[i] = aux
        
        

print(vect)
    