def Agregar_Curso():
    Aula = input("Introduzca el aula para el curso: ").title()
    Nombre_Instructor = input("Introduzca el nommbre del instructor: ").title()
    Titulo_Instructor = input("Introduzca el título del instructor: ").title()
    Edad_Instructor = input("Introduzca la edad del instructor: ").title()
    curso = {Aula:{"Instructor":{"Nombre":Nombre_Instructor, "Titulo":Titulo_Instructor, "Edad":Edad_Instructor}}, "Alumnos":{}}
    return curso

def Modificar_Curso():
    print("Ha elegido modificar el curso.")
    Aula2 = input("Introduzca el aula para el curso: ") .title()
    Nombre_Instructor2 = input("Introduzca el nombre del instructor: ").title()
    Titulo_Instructor2 = input("Introduzca el título del instructor: ").title()
    Edad_Instructor2 = input("Introduzca la edad del instructor: ").title()
    Curso_Modificado = {Aula2:{"Instructor":{"Nombre":Nombre_Instructor2, "Titulo":Titulo_Instructor2, "Edad":Edad_Instructor2 }}, "Alumnos":{}}
    return Curso_Modificado
