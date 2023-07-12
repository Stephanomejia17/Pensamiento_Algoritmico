def llenarMatriz(m,partidos, regiones):
    for i in range(0, partidos):
        m.append([])
        for j in range(0, regiones):
            print("Ingrese los resultados para la region ", i+1, " y el partido ", j+1)
            valor = int(input())
            m[i].append(valor)
            
            
    return m
    
def totalVotosPartido(m, partidos, regiones):
    suma = []
    
    for j in range(0, regiones):
        valor = 0
        for i in range(0, partidos):
            valor += m[i][j]
        suma.append(valor)
    return suma    

def totalVotosRegion(m, partidos, regiones):
    suma = []
    
    for i in range(0, partidos):
        valor = 0
        for j in range(0, regiones):
            valor += m[i][j]
        suma.append(valor)
    return suma    


def PartidoObtuvoMayor(m, partidos, regiones):
    Mayor = -999
    indice = 0
    Valores = []
    for i in range(0, partidos):
        valor = 0
        for j in range(0, regiones):
            valor += m[i][j]
    
            if(valor > Mayor):
                Mayor = valor
                indice = i
                
    Valores.append(Mayor)
    Valores.append(indice)
    
    return Valores
            
def Promedio(m, partidos, regiones):
    Promedio = []
    for i in range(0, partidos):
        Suma = 0
        for j in range(0, regiones):
            Suma += m[i][j]
        Promedio.append(Suma/partidos)
        
    return Promedio
            


def main():
    NumPartidos = int(input("Ingrese la cantidad de Partidos: "))
    NumRegiones = int(input("Ingrese la cantidad de REgiones: "))
    matriz = []
    llenarMatriz(matriz, NumPartidos, NumRegiones)
    TotalDeVotosPP = totalVotosPartido(matriz, NumPartidos, NumRegiones)
    TotalDeVotosPR = totalVotosRegion(matriz, NumPartidos, NumRegiones)
    PartidoObtuvoMayorRegion = PartidoObtuvoMayor(matriz, NumPartidos, NumRegiones)
    Promedios = Promedio(matriz, NumPartidos, NumRegiones)
    x = "-"
    
    print(x*40)
    print("Votos por Partido: ")
    for i in range(0, NumPartidos):
        print(i+1,".",TotalDeVotosPP[i])
        
    print("Votos por Region: ")
    for i in range(0, NumPartidos):
        print(i+1,".",TotalDeVotosPR[i])
        
    print("El partido que Obtuvo más votos es ", PartidoObtuvoMayorRegion[1], " con un total de ", PartidoObtuvoMayorRegion[0], " votos")
    
    print("Promedios: ")
    for i in range(0, NumPartidos):
        print(i+1,".",Promedios[i])    
        
main()