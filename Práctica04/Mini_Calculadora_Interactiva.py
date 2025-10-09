while True:
    print()
    print("°Mini Calculadora Interactiva°")
    print()
    print("""Elige una operación:
    1. Sumar dos números.
    2. Restar dos números.
    3. Multiplicar dos números.
    4. Dividir dos números.
    5. Salir.      """)
    opcion = int(input("Elige una opción e introdúzcala aquí: "))
    if opcion == 1:
        print("Ha seleccionado Suma.")
        Numero1 = int(input("¿Cuál es el primer número que desea utilizar? "))
        Numero2 = int(input("¿Cuál es el segundo número que desea utilizar? "))
        Resultado = Numero1+Numero2
        print("El resultado de la operacion es: ",Resultado)
    elif opcion == 2:
        print("Ha seleccionado Resta.")
        Numero1 = int(input("¿Cuál es el primer número que desea utilizar? "))
        Numero2 = int(input("¿Cuál es el segundo número que desea utilizar? "))
        Resultado = Numero1-Numero2
        print("El resultado de la operacion es: ",Resultado)
    elif opcion == 3:
        print("Ha seleccionado Multiplicación.") 
        Numero1 = int(input("¿Cuál es el primer número que desea utilizar? "))
        Numero2 = int(input("¿Cuál es el segundo número que desea utilizar? "))   
        Resultado = Numero1*Numero2
        print("El resultado de la operacion es: ",Resultado)
    elif opcion == 4:
        print("Ha seleccionado División.") 
        Numero1 = int(input("¿Cuál es el primer número que desea utilizar? "))
        Numero2 = int(input("¿Cuál es el segundo número que desea utilizar? ")) 
        Resultado = Numero1/Numero2
        print("El resultado de la operacion es: ",Resultado)
    elif opcion == 5:
        print("Ha decidido salir.") 
        break
    else:
        print("Ha ocurrido un error fatal")
print()