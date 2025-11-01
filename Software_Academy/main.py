from modelos.curso import Agregar_Curso
from modelos.curso import Modificar_Curso
from modelos.alumno import Modificar_Alumno
from modelos.alumno import Agregar_Alumno

Cursos = {}
while True:
    opcion = int(input("""Eliga la operación que desea utilizar:
1. Agregar Curso.
2. Modificar Curso.
3. Eliminar Curso.
4. Agregar Alumno.
5. Modificar Alumno.
6. Eliminar Alumno.
7. Mostrar Cursos.
8. Mostrar Alumnos.
9. Mostrar un Curso en específico. 
10. Salir.            
"""))
    if opcion == 1:
        Nombre_Curso_Agregar = input("Introduzca el nombre del curso a agregar: ").title()
        Curso_Nuevo = Agregar_Curso()
        Cursos[Nombre_Curso_Agregar] = Curso_Nuevo

    elif opcion == 2:
        Nombre_Curso_Modificar = input("Introduzca el nombre del curso a modificar:").title()
        Curso_Modificar = Modificar_Curso()
        Cursos[Nombre_Curso_Modificar] = Curso_Modificar

    elif opcion == 3:
        Nombre_Curso_Eliminar = input("Introduzca el nombre del curso a eliminar:").title()
        del Cursos[Nombre_Curso_Eliminar]
        

    elif opcion == 4:
        Nombre_Curso_Agregar_Alumno = input("Introduzca el nombre del curso en el que desea añadir al alumno: ").title()
        if Nombre_Curso_Agregar in Cursos:
            ID_Alumno = input("Introduzca el ID del Alumno: ").title()
            Alumno_Nuevo = Agregar_Alumno()
            Cursos[Nombre_Curso_Agregar_Alumno]["Alumnos"][ID_Alumno] = Alumno_Nuevo


    elif opcion == 5:
        Nombre_Curso_Modificar_Alumno = input("Introduzca el nombre del curso en el que desea modificar al alumno: ").title()
        if Nombre_Curso_Modificar_Alumno in Cursos:
            ID_Alumno_Modificar = input("Introduzca la ID del alumno a modificar: ")
            if ID_Alumno_Modificar in Cursos[Nombre_Curso_Modificar_Alumno]["Alumnos"]:
                Alumno_Modificado = Modificar_Alumno()
                del Cursos[Nombre_Curso_Modificar_Alumno]["Alumnos"][ID_Alumno_Modificar]
                Cursos[Nombre_Curso_Modificar_Alumno]["Alumnos"][ID_Alumno_Modificar]= Alumno_Modificado

    elif opcion == 6:
        Nombre_Curso_Eliminar_Alumno = input("Introduzca el nombre del curso en el que desea eliminar al alumno: ").title()
        if Nombre_Curso_Eliminar_Alumno in Cursos:
            ID_Alumno_Eliminar = input("Introduzca la ID del alumno a eliminar: ")
            if ID_Alumno_Eliminar in Cursos[Nombre_Curso_Eliminar_Alumno]["Alumnos"]:
                del Cursos[Nombre_Curso_Eliminar_Alumno]["Alumnos"][ID_Alumno_Eliminar]
   
        
    elif opcion == 7:
        print("Los cursos existentes son:")
        print("--------------------------")
        for e, i in Cursos.items():
            print(f"- {e}, {i}")
        print("--------------------------")

    elif opcion == 8:
        Opcion_Mostrar = input("Introduzca el nombre del curso en el cual desea ver la lista de alumnos: ").title()
        if Opcion_Mostrar in Cursos:
            print("Los Alumnos existentes en este curso son:")
            print("-----------------------------------------")
            for e, i in Cursos[Opcion_Mostrar]["Alumnos"].items():
                print(f"- {e}, {i}")
            print("-----------------------------------------")   

    elif opcion == 9:
        Opcion_Mostrar2 = input("Introduzca el curso que desea ver: ").title()
        if Opcion_Mostrar2 in Cursos:
            for a, e in Cursos[Opcion_Mostrar2].items():
                print(f"- {a}, {e}")

    elif opcion == 10:
        break
    
    else:
        print("Opción no válida.")





  