"""
Determine la temperatura en grados Fahrenheit a partir del valor en grados
centígrados. Dado por la siguiente ecuación: f = 9/5*C + 32
"""

C = float(input("Ingrese los grados centigrados: "))

F = round(9/5*C +32, 2)

print("Los grados centigrados ", C, " en Farenheit son: ", F)


