Marcas = ["Mazda", "MiniCooper", "Mercedes Benz", "Porsche", "BMW", "Lamborghini", "Tesla"]
Modelo = [["CX-9", "Sedán", "3"], ["Convertible", "ClubMan", "CountryMan"], ["SUV", "HatchBack", "Tourer"], ["Cayenne", "Taycan", "911"],["i4", "iX3", "X6"], ["Huracán", "Urus", "Revuelto"], ["Model Y", "Model 3", "Model S"]]
codAutos = [["001", "002", "003"], ["004", "005", "006"], ["007", "008", "009"], ["010", "011", "012"], ["013", "014", "015"], ["016", "017", "018"], ["019", "020", "021"]]
PreciosAutos = [[53197.68, 21223.25, 83486.30], [41955.27, 31929.77, 31907.44], [47537.40, 32577.30, 85960], [98900, 80000, 256900],[58900, 75900, 95990.26], [269995, 230000, 650000], [64970, 46990, 50000]]
existencias = [[2,3,2], [5,1,2],[2,3,1],[1,2,0],[2,1,1],[1,1,1],[1,2,1]]

exit = 1
x = "-"


def Comprar():
    codAuto = str(input("Ingrese el código del Auto: "))
    for i in range(0, len(codAutos)):
        for j in range(0, 3):
            if(codAutos[i][j] == codAuto and existencias[i][j] > 0):
                print("{:<10} {:<15} {:<15} {:<15} {:<10}".format('Codigo', 'Marca', 'Modelo', 'Precio(USD)', 'Existencias'))
                print("{:<10} {:<15} {:<15} {:<15} {:<10}".format(codAuto, Marcas[i], Modelo[i][j], PreciosAutos[i][j], existencias[i][j]))
                confirmador = int(input("Ingrese 1 si desea continuar con la compra, de lo contrario ingrese 0"))
                if(confirmador == 1):
                    
                    TotalCompra = PreciosAutos[i][j]
                    
                    print(x*75, "\n", "Seleccione una de las opciones: \n", x*75)
                    print("1) Bancolombia",  "\n2) Nequi", "\n3) Davivienda", "\n4) VISA", "\n5) MasterCard")
                    metodoPago = int(input("Ingrese su método de pago: "))
                    if(metodoPago == 1):
                        TotalCompra = TotalCompra - (TotalCompra * 0.1) 
                        print("EL TOTAL DE LA COMPRA ES: ", TotalCompra)
                        confirmacionDeCompra = int(input("Ingrese 1 si ya realizó el pago: "))
                        if(confirmacionDeCompra == 1):
                            print("GRACIAS POR SU COMPRA, NOS ALEGRA QUE AHORA FORME PARTE DE LA FAMILIA ASU MARE, PUES")
                    elif(metodoPago == 3):
                        TotalCompra = TotalCompra - (TotalCompra * 0.15)
                        print("EL TOTAL DE LA COMPRA ES: ", TotalCompra)
                        confirmacionDeCompra = int(input("Ingrese 1 si ya realizó el pago: "))
                        if(confirmacionDeCompra == 1):
                            print("GRACIAS POR SU COMPRA, NOS ALEGRA QUE AHORA FORME PARTE DE LA FAMILIA ASU MARE, PUES")
                    else:
                        print("EL TOTAL DE LA COMPRA ES: ", TotalCompra)
                        confirmacionDeCompra = int(input("Ingrese 1 si ya realizó el pago: "))
                        if(confirmacionDeCompra == 1):
                            print("GRACIAS POR SU COMPRA, NOS ALEGRA QUE AHORA FORME PARTE DE LA FAMILIA ASU MARE, PUES")
   
                else:
                    break
                
    

while exit:
    print(x*75)
    print("B\tI\tE\tN\tV\tE\tN\tI\tD\tO")
    print(x*75, "\n", "Seleccione una de las opciones: ")
    print("1) Realizar una Compra",  "\n2) Consultar Precio", "\n3) Inventario", "\n4) Catálogo", "\n5) Salir")
    opcion = int(input("Ingrese la opción que quiere realizar: "))
    
    if(opcion == 1):
        
        print(x*75)
        Comprar()
        
            
        
                        
            
    elif(opcion == 2):
        print(x*75)
        codAuto = str(input("Ingrese el código del Auto: "))
        verificador = 0
        print(x*75)
        for i in range(0, len(codAutos)):
            for j in range(0, 3):
                if(codAutos[i][j] == codAuto):
                    print("{:<10} {:<15} {:<15} {:<15} {:<10}".format('Codigo', 'Marca', 'Modelo', 'Precio(USD)', 'Existencias'))
                    print("{:<10} {:<15} {:<15} {:<15} {:<10}".format(codAuto, Marcas[i], Modelo[i][j], PreciosAutos[i][j], existencias[i][j]))
                    
                    verificador = 1
        if(verificador == 0):
            print("EL CÓDIGO DEL AUTO INGRESADDO NO EXISTE")
                  
    elif(opcion == 4):
        print(x*75)
        print("{:<10} {:<15} {:<15} {:<15} {:<10}".format('Codigo', 'Marca', 'Modelo', 'Precio(USD)', 'Existencias'))
        print(x*75)
        
        for i in range(0, len(Marcas)):
            
            for j in range(0, 3):
                
                print("{:<10} {:<15} {:<15} {:<15} {:<10}".format(codAutos[i][j], Marcas[i], Modelo[i][j], PreciosAutos[i][j], existencias[i][j]))
                
    elif(opcion == 5):
        exit = 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        