v = [78,26,9,7,11,24,9,6]
dato = int(input("Ingrese el dato: "))
cont = 0
for i in range(0, len(v)):
    if(dato == v[i]):
        cont += 1
         
    
        
if(cont > 0):
    print("El dato se encontró", cont, "veces")
else:
    print("EL dato no se encontró")