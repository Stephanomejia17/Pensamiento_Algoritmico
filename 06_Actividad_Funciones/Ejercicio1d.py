def suma(num1, num2):
    sum = num1 + num2
    return sum
def resta(num1, num2):
    res = num1 - num2
    return res
def multiplicacion(num1, num2):
    multi = num1 * num2
    return multi
def division(num1, num2):
    div = num1/num2
    return div


numero1 = int(input("Ingrese el primer valor: "))
numero2 = int(input("Ingrese el segundo valor: "))

print("La suma es: ", suma(numero1,numero2))
print("La resta es: ", resta(numero1, numero2))
print("La multiplicacion: ", multiplicacion(numero1, numero2))
print("La division es: ", division(numero1, numero2))