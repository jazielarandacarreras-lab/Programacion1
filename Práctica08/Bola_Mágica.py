import random
while True:
    print("°------------------------------------------------------------------------°")
    print("Hola, soy la bola mágica. Hazme una pregunta (Escribe salir para terminar)")
    respuesta = input() 
    if respuesta.lower() == "salir":
        print("¡Adiós! o/")
        break
    
    numero = random.randint(1,20)
    if numero == 1:
        print("Sí, definitivamente.")   
    elif numero == 2:
        print("Sin duda.")  
    elif numero == 3:       
        print("Definitivamente sí.")
    elif numero == 4:
        print("No lo dudes.")   
    elif numero == 5:
        print("Probablemente.")
    elif numero == 6:   
        print("Es posible.")
    elif numero == 7:       
        print("Sí.")
    elif numero == 8:           
        print("No.")
    elif numero == 9:   
        print("Probablemente no.")
    elif numero == 10:
        print("No es posible.")
    elif numero == 11:       
        print("Definitivamente no.")        
    elif numero == 12:
        print("No lo creo.")    
    elif numero == 13:     
        print("Pregunta de nuevo más tarde.")
    elif numero == 14:       
        print("No puedo predecirlo ahora.")
    elif numero == 15:     
        print("Concéntrate y pregunta de nuevo.")
    elif numero == 16:       
        print("No cuentes con ello.")
    elif numero == 17:       
        print("Mi respuesta es no.")
    elif numero == 18:       
        print("Mis fuentes dicen que no.")
    elif numero == 19:       
        print("Es cierto.")
    elif numero == 20:       
        print("Es decididamente así.")