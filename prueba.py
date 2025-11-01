Cursos = {}
Nombre_Curso = input("Introduzca el nombre del curso a agregar: ")
Cursos[Nombre_Curso] = ["Instructor"]
print(Cursos)
def Agregar_Curso():
    Nombre_Instructor = input("Introduzca el nommbre del instructor: ")
    Titulo_Instructor = input("Introduzca el título del instructor: ")
    Edad_Instructor = input("Introduzca la edad del instructor: ")
    Cursos[Nombre_Curso]["Instructor"] = {Nombre_Instructor,Titulo_Instructor,Edad_Instructor}

Agregar_Curso()
print(Cursos)