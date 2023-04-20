Marcas = ["Mazda", "MiniCooper", "Mercedes Benz", "Porsche", "BMW", "Lamborghini", "Tesla"]
Modelo = [["CX-9", "Sedán", "3"], ["Convertible", "ClubMan", "CountryMan"], ["SUV", "HatchBack", "Tourer"], ["Cayenne", "Taycan", "911"],["i4", "iX3", "X6"], ["Huracán", "Urus", "Revuelto"], ["Model Y", "Model 3", "Model S"]]
codAutos = ["001", "002", "003", "004", "005", "006", "007"]
PreciosAutos = []
existencias = [50,45,20,17,54]

exit = 1
x = "-"

while exit:
    print(x*75)
    print("B\tI\tE\tN\tV\tE\tN\tI\tD\tO")
    print(x*75, "\n", "Seleccione una de las opciones: ")
    print("1) Realizar una Compra",  "\n2) Consultar Precio", "\n3) Inventario", "\n4) Catálogo", "\n5) Salir")
    opcion = int(input("Ingrese la opción que quiere realizar: "))
    
    if(opcion == 4):
        print(x*75)
        print("M-A-R-C-A\t\t\t", "M-O-D-E-L-O" )
        print(x*75)
        
        for i in range(0, len(Marcas)):
            
            for j in range(0, 3):
                print(Marcas[i],"\t\t", Modelo[i][j])
                
                
                
        
        
    
    
    elif(opcion == 5):
        exit = 0