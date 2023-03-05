#e. DETERMINAR SI UN NUMERO ES DIVISOR DE OTRO,
#AMBOS NUMEROS SON INGRESADOS POR EL USUARIO

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))



if(a > b): 
    M = a
    m = b
else:
    M = b
    m = a


if (M % m) == 0 :
    print("El numero ", m, " es divisor de ", M)
else:
    print("El numero ", m, " no es divisor de ", M)