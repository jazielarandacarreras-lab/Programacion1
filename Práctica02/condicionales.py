#if else elif

edad = 25#input("Dime tu edad: ")
edad = int(edad)
if edad >= 10 and edad < 18:
    print("Eres un adolescente.")
elif edad >= 18:
    print("Eres un adulto.")
else:
    print("Todavía eres un niño.")
print("Fin del programa.")


#Match

opcion = int(input("""
1. Agregar
2. Editar
3. Eliminar
4. Leer
5. Finalizar
"""))

match opcion:
    case 1:
        print("Se ha agregado correctamente.")
    case 2:
        print("Se ha modificado.")
    case 3:
        print("Se ha eliminado correctamente")
    case 4:
        print("El usuario registrado se llama Jaziel.")
    case 5:
        print("Se finalizá el programa.")