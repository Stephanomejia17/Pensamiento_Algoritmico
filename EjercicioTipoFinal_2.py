def llenarMatriz(accionistas, dias, resultado):
    tamanio = len(accionistas)
    
    for i in range(0, tamanio):
        resultado.append([])
        for j in range(0, dias):
            print("Ingrese la accion del Accionista ", accionistas[i], " en el día: ", j+1)
            valor = int(input())
            resultado[i].append(valor)
    return resultado
            
            
def Promedio(resultado, dias, promedio):
    for i in range(0,10):
        suma = 0
        for j in range(0, dias):
            suma += resultado[i][j]
        promedio.append(suma/dias)
    return promedio   

def Busqueda(matriz, valorABuscar, dias, accionistas):
    
    menor = 999
    for i in range(0, len(matriz)):
        for j in range(0, dias):
            if(accionistas[i] == valorABuscar and matriz[i][j] < menor):
                menor = matriz[i][j]
    return menor            
        

    
    


def main():
    accionistas = ["Ecopetrol", "Isagen", "Bancolombia", "Fabricato", "Avianca", "Exito", "Suramericana", "Argos", "Nutresa", "Varela"]
    dias = int(input("Ingrese la cantidad de días: "))
    resultado = []
    promedio = []
    
    llenarMatriz(accionistas, dias, resultado)
    Promedio(resultado, dias, promedio)
    print("Promedios: ")
    for i in range(0, len(accionistas)):
        print(i+1,".", accionistas[i], ": ", promedio[i])
    valorABuscar = str(input("Ingrese el accionista con menor accion que desea buscar: "))
    
    
    menor = Busqueda(resultado, valorABuscar, dias, accionistas)
    print("La menor Accion de ", valorABuscar, " es: ", menor)
    
    
main()