print("°Analizador de textos°")
Texto = input("Ingrese el texto que desea analizar: ")
Letra1 = input("Ingrese la primera letra que desea buscar en el texto: ")
Letra2 = input("Ingrese la segunda letra que desea buscar en el texto: ")
Letra3 = input("Ingrese la tercera letra que desea buscar en el texto: ")
Texto = Texto.lower()
Letra1 = Letra1.lower() 
Letra2 = Letra2.lower()
Letra3 = Letra3.lower()
CantidadLetras = 0

print()

for l in Texto:
    if l == Letra1 or l == Letra2 or l == Letra3:
        CantidadLetras = CantidadLetras + 1
print(f"La cantidad de veces que aparecen las letras {Letra1}, {Letra2} y {Letra3} en el texto es: {CantidadLetras}")


TextoSplit= Texto.split()
CantidadPalabras = len(TextoSplit)
print(f"La cantidad de palabras que tiene el texto es: {CantidadPalabras}")

CantidadCaracteres = len(Texto)
print(f"La cantidad de caracteres que tiene el texto es: {CantidadCaracteres}"
      )
TextoInvertido = ' '.join(TextoSplit[::-1])
print(f"El texto con el orden de palabras invertido es: {TextoInvertido}")


if (palabra.lower() == "python" for palabra in TextoSplit):
    print("La palabra 'python' sí se encuentra en el texto.")
else:
    print("La palabra 'python' no se encuentra en el texto.")