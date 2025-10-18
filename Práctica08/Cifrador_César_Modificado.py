def cifrar_mensaje(mensaje, clave):
    resultado = ""
    for letra in mensaje:
        if letra.isalpha():
            if letra.isupper():
                base = ord('A')
            else:
                base = ord('a')
            nuevaletra = chr((ord(letra) - base + clave) % 26 + base)
            resultado = resultado + nuevaletra

        elif letra.isdigit():
            resultado = resultado + letra

        elif letra == " ":
            resultado = resultado + "_"

        else:
            if clave % 2 == 0:
                resultado = resultado + "@"
            else:
                resultado = resultado + "!"
    return resultado


def main():
    while True:
        print("°CIFRADOR CÉSAR MODIFICADO°")
        print("""1. Cifrar mensaje.
2. Descifrar mensaje.
3. Salir.""")

        opcion = input("Seleccione una opción (1-3): ")
        match opcion:
            case "1" | "cifrar"|"cifrar mensaje":
                mensaje = input("Escribe el mensaje: ")
                clave = int(input("Escribe la clave (número): "))
                resultado = cifrar_mensaje(mensaje, clave)
                print("Mensaje cifrado:", resultado)

            case "2" | "descifrar" | "descifrar mensaje":
                mensaje = input("Escribe el mensaje cifrado: ")
                clave = int(input("Escribe la clave usada: "))
                resultado = cifrar_mensaje(mensaje, -clave)
                print("Mensaje descifrado:", resultado)

            case "3" | "salir":
                print("Adiós. o/ ")
                break
            case _:
                print("Has puesto una operación inválida.")


main()