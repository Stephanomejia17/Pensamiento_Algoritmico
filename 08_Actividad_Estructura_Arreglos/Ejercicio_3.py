temp = []
suma = 0
M = -999
for i in range(0, 5):
    diario = float(input("Ingrese la temperatura: "))
    temp.append(diario)
    suma = suma + diario
    if(M<temp[i]):
        M = temp[i]
    
promedio = suma/5
cont = 0
for i in range(0, len(temp)):
    if(temp[i] < promedio):
        cont += 1

print("Temperatura más alta: ", M, "\nDías donde la temperatura fue menor que el promedio" , promedio, ": ", cont)



    