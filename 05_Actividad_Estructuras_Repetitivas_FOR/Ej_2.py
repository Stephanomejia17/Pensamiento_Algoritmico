"""
Una tienda de música vende LP de distintos géneros y artistas. La tienda ofrece descuentos en sus compras según el género y el año de lanzamiento del LP

- Género Rock y lanzamiento menor o igual a 1969: 10% de descuento
- Género Metal y lanzamiento menor o igual a 1980: 15% de descuento
- Género Heavy Metal y lanzamiento menor o igual a 1989: 15% de descuento
- Género Pop y lanzamiento mayor o igual a 2000: 10% de descuento
- Género Punk y lanzamiento mayor o igual a 2000: 15% de descuento
- Género Salsa y lanzamiento mayor o igual a 2005: 15% de descuento
- Género Disco y lanzamiento menor o igual a 1960: 25% de descuento

Elabore un programa que lea la cantidad de discos que un cliente va a comprar. Luego por cada disco, lea el género año de lanzamiento y precio del disco
Al final, Calcule:
    Total a Pagar
    Total Descontado
    
"""


#VERSION 1
"""
discos = int(input("Cantidad de Discos que comprará: "))

total_pagar = 0
total_desc = 0

for i in range (1,discos+1):
    print("Elija entre: Rock -- Metal -- Heavy Metal -- Pop -- Punk -- Salsa -- Disco")
    genero = str(input("Ingrese el género del disco: "))
    anio = int(input("Ingrese el año de lanzamiento del disco: "))
    p_discos = float(input("Ingrese el Valor del Disco: "))
    if((genero == "Rock") and (anio <= 1969)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.1))
        total_desc = total_desc + (p_discos-(p_discos * 0.1))
        
    elif((genero == "Metal") and (anio <= 1980)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.15))
        total_desc = total_desc + (p_discos-(p_discos * 0.15))
        
    elif((genero == "Heavy Metal") and (anio <= 1989)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.15))
        total_desc = total_desc + (p_discos-(p_discos * 0.15))
        
    elif((genero == "Pop") and (anio >= 2000)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.1))
        total_desc = total_desc + (p_discos-(p_discos * 0.1))
        
    elif((genero == "Punk") and (anio >= 2000)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.15))
        total_desc = total_desc + (p_discos-(p_discos * 0.15))
        
    elif((genero == "Salsa") and (anio <= 2005)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.15))
        total_desc = total_desc + (p_discos-(p_discos * 0.15))
        
    elif((genero == "Disco") and (anio <= 1960)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.25))
        total_desc = total_desc + (p_discos-(p_discos * 0.25))
        
    else:
        total_pagar = total_pagar + p_discos

print("Valor Total a Pagar: ", total_pagar, "\nValor Total de Descuento: ", total_desc)
"""

#VERSION 2

discos = int(input("Cantidad de Discos que comprará: "))

total_pagar = 0
total_desc = 0

for i in range (1,discos+1):
    print("Elija entre:\n 1.Rock \n 2.Metal \n 3.Heavy Metal \n 4.Pop \n 5.Punk \n 6.Salsa \n 7.Disco")
    genero = int(input("Ingrese el género del disco: "))
    anio = int(input("Ingrese el año de lanzamiento del disco: "))
    p_discos = float(input("Ingrese el Valor del Disco: "))
    if((genero == 1) and (anio <= 1969)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.1))
        total_desc = total_desc + (p_discos-(p_discos * 0.1))
        
    elif((genero == 2) and (anio <= 1980)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.15))
        total_desc = total_desc + (p_discos-(p_discos * 0.15))
        
    elif((genero == 3) and (anio <= 1989)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.15))
        total_desc = total_desc + (p_discos-(p_discos * 0.15))
        
    elif((genero == 4) and (anio >= 2000)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.1))
        total_desc = total_desc + (p_discos-(p_discos * 0.1))
        
    elif((genero == 5) and (anio >= 2000)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.15))
        total_desc = total_desc + (p_discos-(p_discos * 0.15))
        
    elif((genero == 6) and (anio <= 2005)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.15))
        total_desc = total_desc + (p_discos-(p_discos * 0.15))
        
    elif((genero == 7) and (anio <= 1960)):
        total_pagar = total_pagar + (p_discos-(p_discos * 0.25))
        total_desc = total_desc + (p_discos-(p_discos * 0.25))
        
    else:
        total_pagar = total_pagar + p_discos

print("Valor Total a Pagar: ", total_pagar, "\nValor Total de Descuento: ", total_desc)


