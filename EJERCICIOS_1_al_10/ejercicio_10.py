'''
Ejercicio 10:
Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres
Ejemplo:
nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
nota = [6,8,10,8,5]

'''
lista_nombres = []
lista_sexo = []
lista_nota = []
contador_alumnos = 0
nota_baja = None
nombre_ = ''
acumulador_femenino = 0
contador_femenino = 0

while contador_alumnos < 5:
    contador_alumnos += 1
    nombre = input("Ingrese el nombre del alumno: ")

    lista_nombres.append(nombre)

    sexo = input("Ingrese un sexo: M o F: ")
    while sexo != "M" and sexo != "F":
        sexo = input("Error, introducir un sexo valido: ")

    lista_sexo.append(sexo)

    nota = input("Ingrese una nota numerica: ")
    while nota.isalpha():
        nota = input("ERROR. INGRESE UNA NOTA NUMERICA: ")

    nota = int(nota)    
    lista_nota.append(nota)


    for i in range(len(lista_nombres)):
        nombre = lista_nombres[i]
        sexo = lista_sexo[i]
        nota = lista_nota[i]
        
        if sexo == "M":
            if  nota_baja == None or nota < nota_baja :
                nota_baja = nota
                nombre_ = lista_nombres[i]

    for i in range(len(lista_nombres)):
        nombre = lista_nombres[i]
        sexo = lista_sexo[i]
        nota = lista_nota[i]

        if sexo == "F":
            acumulador_femenino += nota 
            contador_femenino += 1
            
        if contador_femenino != 0 and contador_femenino != 0:
            promedio = acumulador_femenino / contador_femenino

print(f"PROMEDIO NOTA FEMENINA : {promedio:.0f}")
print(f"HOMBRE CON NOTA MAS BAJA: {nombre_} -- {nota_baja}")