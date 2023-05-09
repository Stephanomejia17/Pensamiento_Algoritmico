m = [[340,345,567,458,145,265,897], [540,457,125,104,100,745,895], [830,910,860,450,782,566,489], [120, 457, 411, 555, 888, 568, 471], [130,140,150,160,125,128,489]]
sumaDeDias = []
diaDeVentaMayor = -999
prom = 0
sucursal = 0

for j in range(0, 7):
    suma = 0
    for i in range(0, 5):
        suma += m[i][j]
    sumaDeDias.append(suma)

for i in range(0, 7):
    if (diaDeVentaMayor <= sumaDeDias[i]):
        diaDeVentaMayor = sumaDeDias[i]
        sucursal = i+1
        
sucurcalesTotales = []
for i in range(0, 5):
    suma = 0
    for j in range(0, 7):
        suma += m[i][j]
    sucurcalesTotales.append(suma)
mayorSucurs = -99
sucurRentable = 0
for i in range(0, 5):
    if (mayorSucurs <= sucurcalesTotales[i]):
        mayorSucurs = sucurcalesTotales[i]
        sucurRentable = i+1
        
promedios = []
for j in range(0, 7):
    prom = 0
    for i in range(0, 5):
        prom += m[i][j]
    promedios.append(prom/5)
    
print("Dia de mayor venta: ",sucursal)
print("Sucursal más rentable: ", sucurRentable)
print("Promedios: ")
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format('Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'))
print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(promedios[0], promedios[1], promedios[2], promedios[3], promedios[4], promedios[5], promedios[6]))

