print("Asistente de actividades diarias")
dia = input("¿Qué día de la semana es hoy? ") 
clima = input("¿Qué clima hace hoy? ")

match dia:
    case "lunes":
        if clima == "soleado":
            print("Hoy es un gran día para trabajar, ¡no olvides tu protector solar y feliz inicio de semana!")
        elif clima == "nublado":
            print("Hoy lleva paraguas al trabajo por si acaso, ¡feliz inicio de semana!")
        elif clima == "lluvioso":
            print("Hoy es un día triste :(, pero hay que trabajar, ¡no olvides tu paraguas y feliz inicio de semana!")


    case "martes":
        if clima == "soleado":
            print("Hoy es un gran día para trabajar, ¡no olvides tu protector solar!")
        elif clima == "nublado":
            print("Hoy lleva paraguas al trabajo por si acaso.")
        elif clima == "lluvioso":
            print("Hoy es un día triste :( pero hay que trabajar, ¡no olvides tu paraguas!")


    case "miercoles":
        if clima == "soleado":
            print("Hoy es un gran día para trabajar, ¡no olvides tu protector solar!")
        elif clima == "nublado":
            print("Hoy lleva paraguas al trabajo por si acaso.")
        elif clima == "lluvioso":
            print("Hoy es un día triste :( pero hay que trabajar, ¡no olvides tu paraguas!")


    case "jueves":
        if clima == "soleado":
            print("Hoy es un gran día para trabajar, ¡no olvides tu protector solar!")
        elif clima == "nublado":
            print("Hoy lleva paraguas al trabajo por si acaso.")
        elif clima == "lluvioso":
            print("Hoy es un día triste :( pero hay que trabajar, ¡no olvides tu paraguas!")


    case "viernes":
        if clima =="soleado":
            print("Hoy es un gran día para trabajar, ¡no olvides tu protector solar!, hoy es el último día de trabajo hay que ir a una fiesta plis :()")
        elif clima == "nublado":
             print("Hoy lleva paraguas al trabajo por si acaso, este clima esta para ver tu serie favorita :)")
        elif clima =="lluvioso":
            print("Hoy es un día triste :( pero hay que trabajar, ¡no olvides tu paraguas!, este clima esta para dormir toda la tarde, (-.-) zzz.")


    case "sabado":
        if clima =="soleado":
             print("Hoy es un gran día para ir a la playa, ¡no olvides tu protector solar!")
        elif clima == "nublado":
             print("Hoy el clima es perfecto para un paseo por el parque.")
        elif clima == "lluvioso":
             print("Hoy es un día triste :(, no te preocupes puedes seguir durmiendo, (-.-) zzz.")


    case "domingo":
        if clima == "soleado":
            print("Hoy es un gran día para ir a la playa, ¡no olvides tu protector solar!")
        elif clima == "nublado":
            print("Hoy el clima es perfecto para un paseo por el parque.")
        elif clima == "lluvioso":
            print("Hoy es un día triste :(, no te preocupes puedes seguir durmiendo, (-.-) zzz.")