"""
Intercambiar el valor de dos variables, es decir, el valor de la variable A
asignársela a la variable B, y el valor de B asignársela a la variable A.
"""

A = int(input("Ingrese el primer valor: "))
B = int(input("Ingrese el segundo valor: "))
c = A

A = B
B = c

print("El valor de A ahora es: ", A, "El valor de B ahora es: ", B)
