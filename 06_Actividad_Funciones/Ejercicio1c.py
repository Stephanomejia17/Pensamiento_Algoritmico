def factorial(num):
    res = 1
    for i in range(1, num+1):
        res = res * i
    return res


numero = int(input("Ingrese un valor: "))

print("EL factorial del numero ingresado es: ", factorial(numero))

