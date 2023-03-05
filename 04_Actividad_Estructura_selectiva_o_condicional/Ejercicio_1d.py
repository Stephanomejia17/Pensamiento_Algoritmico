#D.

se_1 = float(input("Ingrese la primera nota de Seguimientos: "))
se_2 = float(input("Ingrese la segunda nota de Seguimientos: "))
ex_1 = float(input("Ingrese la nota de Parcial: "))
ex_2 = float(input("Ingrese la nota de final: "))

prom = se_1*0.2 + se_2*0.2 + ex_1*0.3 + ex_2*0.3

if(prom >= 3):
    print("Ganaste la materia")
elif (prom >= 2 and prom <= 2.9):
    print("\nDERECHO A RECUPERACION\n")
    rec = float(input("Ingrese la nota de Recuperacion: "))
    if (rec >= 3):
        print("Ganaste la materia")
    else:
        print("Reprobaste")
else:
    print("Reprobaste")