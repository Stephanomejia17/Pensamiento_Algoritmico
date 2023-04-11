Productos = ["Manzana", "Pera", "Guanabana", "Sandía", "Granadilla"]
codProductos = ["001", "002", "003", "004", "005"]
PreciosProductos = [2530, 1700, 25650, 16850, 1920]
existencias = [50,45,20,17,54]

exit = 1 #Verdadero
x = "-"

while exit:
    print(x*75)
    print("B\tI\tE\tN\tV\tE\tN\tI\tD\tO")
    print(x*75, "\n", "Seleccione una de las opciones: ")
    print("1) Realizar una Compra",  "\n2) Consultar Precio", "\n3) Inventario", "\n4) Salir")
    opcion = int(input("Ingrese la opción que quiere realizar: "))
    tamProductos = len(Productos)
    cesta = []
    preciosCesta = []
    total = 0
    
    if(opcion == 1):
        
        for i in range(0,tamProductos):
            print(x*75,"\nSi Terminó de agregar los productos ingrese 0\n", x*75)
            codigo = str(input("\nIngrese el codigo del Producto: "))
            if(codigo == "0"):
                break
            else:
                for j in range(0,tamProductos):
                    if(codigo == codProductos[j]):
                        cesta.append(Productos[j])
                        preciosCesta.append(PreciosProductos[j])
                        total = total + PreciosProductos[j]
                        break
            
        if(len(cesta) == 0):
            print("No se agregó ningún producto a la cesta")
        else:
            print("Productos Agregados: \n")
            print("\tProductos\tPrecio")
            for i in range(0,len(cesta)):
                
                print(i+1,". ", cesta[i], "\t\t", preciosCesta[i])
            print("total: \t\t\t", total)
    
    elif(opcion == 2):
        codigo = str(input("\nIngrese el codigo del Producto: "))
        for i in range(0,tamProductos):
            if(codigo == codProductos[i]):
                print("Precio: ", PreciosProductos[i])
                break
    
    elif(opcion == 3):
        print("Si desea conocer las existencias de todos los productos ingrese 0:")
        productoSelec = str(input("Ingrese el código del Producto: "))
        
        if(productoSelec == "0"):
            for i in range(0,len(Productos)):
                print("Producto: ", Productos[i], "\t Código: ", codProductos[i], "\t Existencias: ", existencias[i])
        else: 
            aux = -1
            for i in range(0,len(codProductos)):
                if(codProductos[i] == productoSelec):
                    aux = i
                
            if(aux == -1):
                print("El código seleccionado no Existe.")
            else:
                print("Producto: ", Productos[aux], "\t Código: ", codProductos[aux], "\t Existencias: ", existencias[aux])    
            
            
            
        
        
    else: 
        exit = 0
            
    
    