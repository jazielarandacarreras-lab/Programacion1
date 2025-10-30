while True:
    info_tienda = "Star Games ",2025
    print(f"{info_tienda}, La estrella eres tú.")
    Inventario = {
        "Minecraft":{"Precio": 440, "Stock": 20},
        "God of war":{"Precio": 560, "Stock": 25},
        "Cuphead":{"Precio": 230, "Stock": 15},
    }
    print("El precio del segundo juego es de", Inventario["God of war"]["Precio"])
    Inventario["God of war"]["Stock"] =Inventario["God of war"]["Stock"] - 1
    print("ESte es el inventario.")
    print(Inventario.items())