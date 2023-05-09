import random
m = []
mayor = -999
for i in range(0, 5):
    m.append([])
    for j in range(0, 5):
        m[i].append(random.randrange(0,1000))
        
for i in range(0, 5): 
    for j in range(0, 5):
        if(mayor <= m[i][j]):
            mayor = m[i][j]
        
print(m)
print("Numero Mayor: ", mayor)