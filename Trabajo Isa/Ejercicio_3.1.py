
A = [[1,5,2,3],
    [4,1,9,8],
    [0,1,5,7],
    [6,5,7,9]]
B = [[9,6,5,4],
    [7,4,5,4],
    [0,0,4,0],
    [3,6,4,9]]
C = []
D = []
        
for i in range(0, 4):
    C.append([])
    D.append([])
    for j in range(0, 4):
        C[i].append(A[i][j] + B[i][j])
        D[i].append(A[i][j] - B[i][j])    
print("Matriz A: ", A)
print("Matriz B: ", B)
print("Matriz C = A + B: ", C)
print("Matriz D = A - B", D)
    