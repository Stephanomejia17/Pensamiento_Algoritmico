edades = []

for i in range(0, 10):
    edad = int(input("Ingrese una edad: "))
    edades.append(edad)

suma = 0
for i in range(0, len(edades)):
    suma = suma + edades[i]

promedio = suma/10

menor = 999
mayor = -999
for i in range(0, len(edades)):
    if(mayor < edades[i]):
        mayor = edades[i]
for i in range(0, len(edades)):
    if(menor > edades[i]):
        menor = edades[i]
        
        
print("Suma de edades: ", suma, "\nEdad Promedio: ", promedio, "\nMayor: ", mayor, "\nMenor: ", menor)
