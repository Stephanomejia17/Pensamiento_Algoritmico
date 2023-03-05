#h.

A = int(input("Ingrese el primer valor: "))
B = int(input("Ingrese el segundo valor: "))
C = int(input("Ingrese el tercer valor: "))    
Y = int(input("Ingrese el cuarto valor: "))

if(Y < A and A < B and B < C):
    X = 0
    print("X es igual a: ", X)
elif((A <= Y) and A < B):
    X = 1
    print("X es igual a: ", X)
elif((B <= Y) and B < C):
    X = 2
    print("X es igual a: ", X)
elif(C <= Y):
    X = 3
    print("X es igual a: ", X)
else:
    X = 4
    print("X es igual a: ", X)

A = float(input("Ingrese el primer peso: "))
B = float(input("Ingrese el segundo peso: "))
C = float(input("Ingrese el tercer peso: "))
D = float(input("Ingrese el cuarto peso: "))

if(A != B):
    if(A > B):
        print(A, " es de mayor peso")
    else:
        print(A, " es de menor peso")
elif(B != A):
    if(B > A):
        print(B, " es de mayor peso")
    else:
        print(B, " es de menor peso")
elif(C != A):
    if(C > A):
        print(C, " es de mayor peso")
    else:
        print(C, " es de menor peso")
elif(D != A):
    if(D > A):
        print(D, " es de mayor peso")
    else:
        print(D, " es de menor peso")