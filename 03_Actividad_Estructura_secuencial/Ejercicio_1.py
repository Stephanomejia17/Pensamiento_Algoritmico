"""
A la mama de Juan le preguntan su edad y contesta: tengo 3 hijos, pregúntele
a Juan su edad. Alberto tiene 2/3 de la edad de Juan, Ana tiene 4/3 de la
edad de Juan y mi edad es la suma de las tres. Hacer un algoritmo que
muestre la edad de los cuatro.
"""

e_juan = int(input("Ingrese la edad: "))
e_Alberto = int(e_juan * 2/3)
e_Ana = int(e_juan * 4/3)

e_mama = e_juan + e_Alberto + e_Ana

print("La edad de Juan es: ", e_juan, " La edad de Alberto es: ", e_Alberto, " La edad de Ana es: ", e_Ana, " La edad de la mama es: ", e_mama)

