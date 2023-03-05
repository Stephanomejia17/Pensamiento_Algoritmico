#c. DETERMINAR EL VALOR DE C, DADA LA EXPRESION

x = int(input("Ingrese un valor: "))
y = int(input("Ingrese es segundo valor: "))

if (x <= 4/3) and (y != 0):
    c = ((4 - 3*x)**1/2) / ((5-6*y)**1/3)
else:
    print("Los valores ingresados no pueden ser usados para resolver la ecuacion")