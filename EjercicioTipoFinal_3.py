def llenarMatriz(m, cantidadPuntosV, cervezas):
    for i in range(0, cantidadPuntosV):
        m.append([])
        id = int(input("Ingrese el ID del punto de venta: "))
        print("Ingrese los gastos para el punto de venta ", id)
        gastos = int(input())
        m[i].append(id)
        m[i].append(gastos)
        for j in range(0, 5):
            print("Ingrese el total de ventas para la cerveza ", cervezas[j])
            valor = int(input())
            m[i].append(valor)
            
def IngresoPV(cantidadPuntosV, m):
    valor = 0
    vector = []
    for i in range(0, cantidadPuntosV):
        valor = 0
        for j in range(2, 7):
            valor += m[i][j]
        vector.append(valor-m[i][1])
        
    return vector

def TCVendeMas(cantidadPuntosV, m):
    ventasPC = []
    Resultado = []
    
    for j in range(2, 7):
        valor = 0
        for i in range(0, cantidadPuntosV):
            valor += m[i][j]
        ventasPC.append(valor)
    Mayor = -999    
    index = 0
    for i in range(0, len(ventasPC)):
        if(ventasPC[i] > Mayor):
            Mayor = ventasPC[i]
            index = i
            
    Resultado.append(Mayor)
    Resultado.append(index)
    
    return Resultado   


def PromGastos(cantidadPuntosV, m):
    Resultado = []
    suma = 0
    for j in range(1, 2):
        for i in range(0, cantidadPuntosV):
            suma += m[i][j]
    promedio = suma / cantidadPuntosV
    
    
    for j in range(1, 2):
        for i in range(0, cantidadPuntosV):
            if(m[i][j] >= promedio):
                Resultado.append(m[i][0])
                
    return Resultado
            
             

            

def main():
    cervezas = ["Rubia", "Negra", "Roja", "Verde", "Azul"]
    cantidadPuntosV = int(input("Ingrese la cantidad de puntos de venta: "))
    matriz = []
    llenarMatriz(matriz, cantidadPuntosV, cervezas)
    print(matriz)
    
    #Ingreso por ventas
    TotalDeVentas = IngresoPV(cantidadPuntosV, matriz)
    for i in range(0, cantidadPuntosV):
        print("El total de ventas para ", matriz[i][0], " es ", TotalDeVentas[i])
        
        
    #Tipo de cerveza que se vende mas
    TCQSVM = TCVendeMas(cantidadPuntosV, matriz)
    print("La cerveza con mayor ventas es ", cervezas[TCQSVM[1]], " con un total de ", TCQSVM[0])
    
    
    #Promedio
    
    Prom = PromGastos(cantidadPuntosV, matriz)
    for i in range(0, len(Prom)):
        print("El establecimiento con id ", Prom[i], " se encuentra por encima del promedio de gastos.")
        
    
    
    
    
    
    
    
    
main()