import random
Palabras = ("abajo","abeja","abeto","abono","abril",
            "abrir","abuso","acaso","acato","acebo",
            "acera","acero","actor","adobe", "acoso")
while True:
    Palabra = Palabras[random.randint(0,len(Palabras)-1)]
    Wordle = list(Palabra)
    print("""\033[1;36m
===============================[Wordle]=========================================
Bienvenido ya he elegido la palabra secreta. Tienes 5 intentos para addivinarla.
================================================================================ \033[0;30m]       """)
    for i in range(5):
        intento = input("Ingrese una palabra de 5 letras sin acentos.").lower()[:5]
        indice = 0
        resultado = ""
        correctas = 0
        for letra in intento:
            if letra == Wordle[indice]:
                correctas += 1
                resultado += "\033[1;32m" + letra + "\033[0;30m"      
            elif letra in Wordle:
                resultado += "\033[1;33m" + letra + "\033[0;30m"  
            else:
                resultado += "\033[1;31m" + letra + "\033[0;30m"  
            indice += 1
        print(resultado)
        if correctas == 5:
            break
    if correctas == 5:
        print(f"Felicidades la palabra era \033[1;32m{Palabra}\033[0;30m has acertado.")
    else:
        print(f"Lo siento has fallado la palabra era \033[1;31m{Palabra}\033[0;30m")
        
    opcion = input("¿Desea jugar otra ronda? (Si/No)").lower()
    if opcion == "no":
        break
    
    