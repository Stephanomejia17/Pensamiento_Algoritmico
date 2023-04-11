#Escriba un pseudocodigo que posea: Una funcion que calcule la media de tres numeros y un conunto de subprogramas (funciones) que determinen: El cuadrado de un número, el cubo de un numero, los divisores de un numero, si el numero es primo o no

def media(valor1, valor2, valor3):
    suma = valor1 + valor2 + valor3
    resultado = suma/3
    
    return resultado

def cuadrado(num):
    res = num**2
    return res

def cubo(num):
    res = num**3
    return res

def divisores(num):
    list = []
    i = 1
    cont = 0
    while (i <= num):
        
        if(num%i == 0):
            cont += 1
            list.append(i)
        i = i + 1
    list.append(cont)
    return list

def primo(num):
    cont = 0
    for i in range(1,num):
        if(num%i==0):
            cont += 1
    return cont


"""
n1 = int(input("Ingrese el primer valor: "))
n2 = int(input("Ingrese el segundo valor: "))
n3 = int(input("Ingrese el tercer valor: "))

res = round(media(n1, n2, n3), 2)

print("La media de los numeros ", n1, ", ", n2, " y ", n3, " es: ", res)
"""

numero = int(input("Ingrese un valor: "))
listDiv = divisores(numero)
if(primo(numero) <= 2):
    print("El numero es primo.")
else:
    print("El numero no es primo.")




cont = listDiv[-1]
print("Divisores: ")

for i in range(0,cont):
    print(listDiv[i])

