n_equipo = str(input("Ingrese el nombre del equipo: "))
resultados = []

puntos = 0
derrotas = 0
victorias = 0
empates = 0

g_favor = 0
g_contra = 0

cant_gol_anotados = 0
cant_gol_recibidos = 0

vallas_invictas = 0

for i in range(0, 19):
    p_favor = int(input("Ingrese la cantidad de puntos a favor: "))
    p_contra = int(input("Ingrese la cantidad de puntos en contra: "))
    cant_gol_anotados += p_favor
    cant_gol_recibidos += p_contra 
    
    if(p_contra == 0):
        vallas_invictas += 1
    
    if(p_favor > p_contra):
        puntos += 4
        victorias += 1
    elif(p_favor == p_contra):
        puntos += 1.5
        empates += 1
    else:
        derrotas += 1    
    resultados.append([p_favor, p_contra])
    
for i in range(0, 19):
    for j in range(0,2):
        if(j == 0):
            g_favor += resultados[i][j]
        else:
            g_contra += resultados[i][j]
            
            
if(g_favor > g_contra):
    Ma = g_favor
    m = g_contra
elif(g_favor < g_contra):
    Ma = g_contra
    m = g_favor
else:
    Ma = g_favor
    m = Ma


Mayor_Victoria = -999
Peor_Derrota = -999
for i in range(0, 19):
    for j in range(0,2):
        if(j == 0):
            if(resultados[i][j] >= Mayor_Victoria):
                Mayor_Victoria = resultados[i][j]
        else:
            if(resultados[i][j]>= Peor_Derrota):
                Peor_Derrota = resultados[i][j]
                
        
    

    
print("\nESTADÍSTICAS DE EQUIPO ", n_equipo, "\n")
print("Puntos Obtenidos: ", puntos)
print("Cantidad de Victorias", victorias)
print("Cantidad de empates: ", empates)
print("Cantidad de derrotas: ", derrotas)
print("Goles a Favor: ", g_favor)
print("Goles en Contra: ", g_contra)
print("Diferencia de goles: ", Ma - m)
print("Promedio de goles anotados: ", cant_gol_recibidos/19)
print("Promedio de goles recibidos: ", cant_gol_recibidos/19)
print("Vallas invictas: ", vallas_invictas)
print("Mayor Victoria: ", Mayor_Victoria)
print("Peor derrota: ", Peor_Derrota)
