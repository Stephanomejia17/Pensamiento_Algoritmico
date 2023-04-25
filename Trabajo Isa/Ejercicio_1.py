nombres = ["Juan","Ana","Miguel","Mariana","Luis","Julian","Beatriz","Laura","Juan David","Maria","Gabriela","Sara"]
generos = ["M","F","M","F","M","M","F","F","M","F","F","F"]
notas = [4.9,3.2,1.0,4.5,4.9,3.7,2.8,1.9,0.9,4.2,4.0,3.0]
suma = 0
contador = 0
suma_hombres = 0
conta_hombres = 0
suma_mujeres = 0
conta_mujeres = 0

n_M_Hombres = -999
n_b_Hombres = 999
n_M_Mujeres = -999
n_b_Mujeres = 999

nombre_M_Hombre = ""
nombre_M_Mujeres = ""
nombre_b_Hombres = ""
nombre_b_Mujeres = ""


for i in range(0, len(nombres)):
    suma += notas[i]
    contador += 1
    if(generos[i] == "M"):
        suma_hombres += notas[i]
        conta_hombres += 1
        if(n_M_Hombres < notas[i]):
            n_M_Hombres = notas[i]
            nombre_M_Hombre = nombres[i] 
        elif(n_b_Hombres > notas[i]):
            n_b_Hombres = notas[i]
            nombre_b_Hombres = nombres[i]
            
    else: 
        suma_mujeres += notas[i]
        conta_mujeres += 1
        if(n_M_Mujeres < notas[i]):
            n_M_Mujeres = notas[i]
            nombre_M_Mujeres = nombres[i] 
        elif(n_b_Mujeres > notas[i]):
            n_b_Mujeres = notas[i]
            nombre_b_Mujeres = nombres[i]
            
        
    
        
        



print("Promedio del curso: ", suma / contador)
print("Promedio de estudiantes hombres: ", round((suma_hombres / conta_hombres), 2))
print("Promedio de estudiantes mujeres: ", round((suma_mujeres / conta_mujeres), 2))
print("Nombre del estudiante con la nota más ALTA de los estudiantes HOMBRES: ", nombre_M_Hombre)
print("Nombre del estudiante con la nota más BAJA de los estudiantes HOMBRES: ", nombre_b_Hombres)
print("Nombre del estudiante con la nota más ALTA de las estudiantes MUJERES: ", nombre_M_Mujeres)
print("Nombre del estudiante con la nota más BAJA de las estudiantes MUJERES: ", nombre_b_Mujeres)



