v = [78,26,9,7,11,24,9,6]
dato = int(input("Ingrese el dato: "))
cont = 0
i = 0
while ((i <= len(v)-1) and (dato != v[i])):
    if(dato == v[i]):
        cont += 1
    i += 1
    
        
if(cont <= len(v)):
    print("El dato se encontró en la posición ", i+1)
else:
    print("EL dato no se encontró")