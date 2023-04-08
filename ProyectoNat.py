def main ():
    import random

    nombres = ["Lina", "Ana", "Felipe", "Tola", "Carola", "Catalina", "Hector", "Luis", "Lorna", "Tere", "Juan", "Italo", "Herlinda", "Francy", "Alberto", "Ivan", "Brahian", "Marco", "Emilio", "Carmen", "Carlina", "Etore", "Luisa", "Leo", "Teresita", "Juana", "Eliana", "Hermelina", "Franco", "Alcides"]
    codigos = ["101710901", "101659391", "102716941", "101740605", "101510302", "101314941", "101780988", "101315971", "101799909", "101510505", "101730989", "101730080", "101736789", "100739989", "101730678", "101710901", "101770707", "101715978", "101718913", "101511505", "101731989", "101731080", "102736789", "100789989", "101730673", "101716901", "101760707", "101815978", "101718803", "101717703"]
    asignaturas = ["Innovaciones socio-educativas", "Investigacion en educacion", "Simposio", "Talentos y capacidades Excepcionales", "Seminario grado V", "Seminario grado VI", "Seminario grado VII"]
    creditos = [1, 2, 2, 3, 3, 2, 3]
    muestra = random.sample(range(len(nombres)), 30)
    calificaciones=[]
    Becado=-1
    for i in range(30): 
        calificaciones_est=[] 
        for j in range(len(asignaturas)): 
            calificacion = round(random.uniform(0.0, 5.0), 1)
            calificaciones_est.append(calificacion)
            calificaciones.append(calificaciones_est)
    promedios = []
    for i in range(30):
        suma_calif_cred = 0
        suma_creditos = 0
        for j in range(len(asignaturas)):
            if calificaciones[i][j] >= 3.5:
                suma_calif_cred += calificaciones[i][j] * creditos[j]
                suma_creditos += creditos[j] 
        if suma_creditos > 0:
            promedio = round(suma_calif_cred / suma_creditos, 2)
        else:
            promedio = 0
        promedios.append(promedio) 
    estudiantes_regulares = []
    estudiantes_prueba = [] 
    becado_index = -1
    Becado = 0 
    for i in range(30):  
        if promedios[i] >= 3.5:
            estudiantes_regulares.append(i) 
            if promedios[i] > Becado: 
                Becado = promedios[i] 
                becado_index = i
        else:
            estudiantes_prueba.append(i) 

    print("Estudiantes regulares:")
    for i in estudiantes_regulares:
        print("Nombre:", nombres[muestra[i]])
        print("Codigo:", codigos[muestra[i]])
        print("Asignaturas matriculadas:")
        print(asignaturas)
        suma_creditos = sum(creditos)
        print("Total creditos matriculados:", suma_creditos)
        print("Promedio credito:", round(promedios[muestra[i]], 2))
    
    print("El estudiante con la beca tiene un promedio de:", Becado)
    if becado_index != -1:
        print("Datos del estudiante con la beca:")
        print("Nombre:", nombres[muestra[becado_index]])
        print("Codigo:", codigos[muestra[becado_index]])
        print("Asignaturas matriculadas:")
        print(asignaturas)
        suma_creditos = sum(creditos)
        print("Total creditos matriculados:", suma_creditos)
        print("Promedio credito:", round(promedios[muestra[becado_index]], 2))
        
main()