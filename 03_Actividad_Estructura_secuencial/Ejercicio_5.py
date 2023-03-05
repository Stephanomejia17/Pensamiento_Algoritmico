"""
Determinar el pago semanal de un obrero que recibe $22.200 por hora
laborada dado que ha trabajado cierta cantidad de horas y tiene una
deducción del 10% de lo devengado por concepto de parafiscales.
"""

horas = int(input("Ingrese el numero de horas laboradas: "))
sueldo = (horas * 22200) 
devengado = sueldo * 0.1

print("Su sueldo final será: ", sueldo + devengado)