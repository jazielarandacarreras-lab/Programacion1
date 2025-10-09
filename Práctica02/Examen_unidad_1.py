aciertos = 0
print("Examen ")

print()

print("1. ¿Qué estructura de control es más adecuada para iterar sobre una secuencia de elementos de un número de veces conocido de antemano?")

opcion1 = int(input("""
1. Bucle "Para".
2. Sentencia condicional "Si".
3. Bucle "Repetir".
4. Bucle "Mientras".
"""))

match opcion1:
    case 1:
        print("Respuesta Correcta")
        aciertos = aciertos + 1
    case 2:
        print("Respuesta Incorrecta")
    case 3:
        print("Respuesta Incorrecta")
    case 4:
        print("Respuesta Incorrecta")
    case _:
        print("Respuesta Incorrecta")

print()

print("2. ¿Qué es un algoritmo?")

opcion2 = int(input("""
1. Conjunto de instrucciones escritas en código binario.
2. Un lenguaje de programación específico.
3. El código fuente de un programa de computadora.
4. Una secuencia de pasos finitos y bien definidos para resolver un problema.
"""))

match opcion2:
    case 1:
        print("Respuesta Incorrecta")
    case 2:
        print("Respuesta Incorrecta")
    case 3:
        print("Respuesta Incorrecta")
    case 4:
        print("Respuesta Correcta")
        aciertos = aciertos + 1
    case _:
        print("Respuesta Incorrecta")

print()

print("3. El lenguaje máquina está compuesto por:")

opcion3 = int(input("""
1. Símbolos lógicos y matemáticos.
2. Pseudocódigo.
3. Instrucciones en inglés abreviado.
4. Código binario.
"""))

match opcion3:
    case 1:
        print("Respuesta Inorrecta")
    case 2:
        print("Respuesta Incorrecta")
    case 3:
        print("Respuesta Incorrecta")
    case 4:
        print("Respuesta Correcta")
        aciertos = aciertos + 1
    case _:
        print("Respuesta Incorrecta")

print()
        
print("4. ¿Cuál de los siguientes componentes NO es parte fundamental de la arquitectura de Von Neumann?")

opcion4 = int(input("""
1. sistema de entrada/salida.
2. CPU.
3. Tarjeta gráfica.
4. Memoria principal.
"""))

match opcion4:
    case 1:
        print("Respuesta Inorrecta")
    case 2:
        print("Respuesta Incorrecta")
    case 3:
        print("Respuesta Correcta")
        aciertos = aciertos + 1
    case 4:
        print("Respuesta Incorrecta")
        
    case _:
        print("Respuesta Incorrecta")


print()

print("5. Un lenguaje de programación de alto nivel se caracteriza por: ")

opcion5 = int(input("""
1. Ser muy dificil de aprender y leer.
2. Ser el más rápido en tiempo de ejecución.
3. Tener un control directo y preciso sobre el hardware.
4. Ser independiente de la arquitectura de la computadora.
"""))

match opcion5:
    case 1:
        print("Respuesta Incorrecta")
    case 2:
        print("Respuesta Incorrecta")
    case 3:
        print("Respuesta Incorrecta")
    case 4:
        print("Respuesta Correcta")
        aciertos = aciertos + 1
    case _:
        print("Respuesta Incorrecta")


print()


print("6. El lenguaje Java es considerado un lenguaje de nivel... ")

opcion6 = int(input("""
1. Bajo.
2. Muy alto.
3. Medio.
4. Alto.
"""))

match opcion6:
    case 1:
        print("Respuesta Incorrecta")
    case 2:
        print("Respuesta Incorrecta")
    case 3:
        print("Respuesta Incorrecta")
    case 4:
        print("Respuesta Correcta")
        aciertos = aciertos + 1
    case _:
        print("Respuesta Incorrecta")


print()

print("7. Un programa de computadora es esencialmente: ")

opcion7 = int(input("""
1. Una colección de algoritmos.
2. El sistema operativo de una computadora.
3. Un dispositivo de hardware.
4. Una secuencia de instrucciones que la computadora ejecuta.
"""))

match opcion7:
    case 1:
        print("Respuesta Incorrecta")
    case 2:
        print("Respuesta Incorrecta")
    case 3:
        print("Respuesta Incorrecta")
    case 4:
        print("Respuesta Correcta")
        aciertos = aciertos + 1
    case _:
        print("Respuesta Incorrecta")

print()

print("8. En pseudocódigo, ¿Qué estructura de control se utiliza para ejecutar un bloque de código solo si se cumple una condición específica?")

opcion8 = int(input("""
1. Condicional o de selección.
2. Repetitiva "Para".
3. Secuencial.
4. Repetitiva "Mientras".
"""))

match opcion8:
    case 1:
        print("Respuesta Correcta")
        aciertos = aciertos + 1
        
    case 2:
        print("Respuesta Incorrecta")
    case 3:
        print("Respuesta Incorrecta")
    case 4:
        print("Respuesta Incorrecta")
    case _:
        print("Respuesta Incorrecta")


print()

print("9. El próposito principal del pseudocódigo es:")

opcion9 = int(input("""
1. Traducir automáticamente código de alto nivel a lenguaje máquina.
2. Ejecutar programas de forma más eficiente que un lenguaje compilado.
3. Planificar y describir la lógica de un algoritmo de forma legible para los humanos.
4. Proporcionar un control directo sobre los registros del procesador.
"""))

match opcion9:
    case 1:
        print("Respuesta Incorrecta")
    case 2:
        print("Respuesta Incorrecta")
    case 3:
         print("Respuesta Correcta")
         aciertos = aciertos + 1
    
    case 4:
        print("Respuesta Incorrecta")
    case _:
        print("Respuesta Incorrecta")



print()

print("10. ¿Cuál es la principal diferencia entre un bucle Mientras(while) y un bucle Repetir(do-while)?")

opcion10 = int(input("""
1. El bucle "Mientras" puede no ejecutarse, mientras que el "Repetir" se ejecuta al menos una vez.
2. No hay ninguna diferencia, son intercambiables.
3. El bucle "Mientras es más rápido que "Repetir".
4. El bucle "Repetir" solo usa números, mientras  que el "Mientras" puede usar cualquier condición.
"""))

match opcion10:
    case 1:
        print("Respuesta Correcta")
        aciertos = aciertos + 1
        
    case 2:
        print("Respuesta Incorrecta")
    case 3:
        print("Respuesta Incorrecta")
    case 4:
        print("Respuesta Incorrecta")
    case _:
        print("Respuesta Incorrecta")



print("Sus aciertos totales fueron: ")
print(aciertos)



