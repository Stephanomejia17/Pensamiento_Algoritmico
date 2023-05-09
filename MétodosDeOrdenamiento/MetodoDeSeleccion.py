vect = []
tamanio = int(input("Ingrese el tamaño del vector: "))

for i in range(0, tamanio):
    valor = int(input("Ingrese un valor: "))
    vect.append(valor)


for i in range(0, tamanio-1):
    for j in range(i+1, tamanio):
        aux = 0
        if(vect[j] < vect[i]):
            aux = vect[i]
            vect[i] = vect[j]
            vect[j] = aux
            
        
for i in range(0, tamanio):
    print(vect[i])
                
