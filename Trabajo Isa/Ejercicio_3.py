FxC= int(input("Ingrese la cantidad de filas y Columnas: "))
A = []
B = []
C = []
D = []
for i in range(0, FxC):
    A.append([])
    for j in range(0, FxC):
        A[i].append(0)
        
for i in range(0, FxC):
    B.append([])
    for j in range(0, FxC):
        B[i].append(0)
for i in range(0, FxC):
    C.append([])
    for j in range(0, FxC):
        C[i].append(0)
for i in range(0, FxC):
    D.append([])
    for j in range(0, FxC):
        D[i].append(0)
        
for i in range(0, FxC):
    for j in range(0, FxC):
        valor = int(input("Ingrese valor de la PRIMERA matriz: "))
        A[i][j] = valor       
for i in range(0, FxC):
    for j in range(0, FxC):
        valor = int(input("Ingrese valor de la SEGUNDA matriz: "))
        B[i][j] = valor
        
for i in range(0, FxC):
    for j in range(0, FxC):
        C[i][j] = A[i][j] + B[i][j]
        D[i][j] = A[i][j] - B[i][j]    
print("Matriz A: ", A)
print("Matriz B: ", B)
print("Matriz C = A + B: ", C)
print("Matriz D = A - B", D)
    