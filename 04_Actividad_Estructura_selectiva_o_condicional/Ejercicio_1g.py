#g.

num_1 = int(input("Ingrese el primer numero: ")) 
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))

prom = (num_1 + num_2 + num_3)/3

m_1 = abs(prom - num_1)
m_2 = abs(prom - num_2)
m_3 = abs(prom - num_3)

print("El promedio es: ", prom)

if(m_1 < m_2 and m_1 < m_3):
    print("El numero mas cercano al promedio es: ", num_1)
elif(m_2 < m_1 and m_2 < m_3):
    print("El numero mas cercano al promedio es: ", num_2)
elif(m_3 < m_1 and m_3 < m_2):
    print("El numero mas cercano al promedio es: ", num_3)