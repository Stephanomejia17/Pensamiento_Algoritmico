#b.ESTABLECER CUAL ES MAYOR DE DOS NUMEROS

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor valor: "))


if(a > b):
    print("El numero mayor es: ", a)
    
elif(a == b):
    print("Los numeros son iguales")
else:
    print("El numero mayor es: ", b)