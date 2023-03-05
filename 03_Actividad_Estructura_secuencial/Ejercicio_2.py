"""
Calcular el área y el perímetro de un rectángulo dado sus longitudes (largo y
ancho).
"""

largo = int(input("Ingrese el largo: "))
ancho = int(input("Ingrese el ancho: "))

area = largo * ancho
perimetro = largo*2 + ancho*2

print("El area es: ", area, "El perimetro es: ", perimetro)
