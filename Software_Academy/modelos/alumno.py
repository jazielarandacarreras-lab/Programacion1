
def Agregar_Alumno():
    
    Nombre_Alumno = input("Introduzca el nombre del alumno: ").title()
    Edad_Alumno = input("Introduzca la edad del alumno: ").title()
    Semestre_Alumno = input("Introduzca el semestre del alumno: ").title()
    Carrera_Alumno = input("Introduzca la carrera del alumno: ").title()
    Alumno_Nuevo = {"Nombre": Nombre_Alumno, "Edad": Edad_Alumno, "Semestre": Semestre_Alumno, "Carrera": Carrera_Alumno}
    return Alumno_Nuevo

def Modificar_Alumno():
    print("Ha elegido modificar un alumno.")
    Nombre_Alumno = input("Introduzca el nombre del alumno: ").title()
    Edad_Alumno = input("Introduzca la edad del alumno: ").title()
    Semestre_Alumno = input("Introduzca el semestre del alumno: ").title()
    Carrera_Alumno = input("Introduzca la carrera del alumno: ").title()
    Alumno_Modificado = {"Nombre": Nombre_Alumno, "Edad": Edad_Alumno, "Semestre": Semestre_Alumno, "Carrera": Carrera_Alumno}
    return Alumno_Modificado