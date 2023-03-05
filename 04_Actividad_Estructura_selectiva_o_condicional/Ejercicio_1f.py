#f.

num = int(input("Ingrese un numero de máximo 2 cifras: "))

if(num%2 == 0):
    print("El número es par")
if(num%7==0):
    print("El número es múltiplo de 7")
if(num%10==3):
    print("La última cifra del número es 3")
else:
    print("El número no es par, no es múltiplo de 7 y su última cifra es distinta de 3")