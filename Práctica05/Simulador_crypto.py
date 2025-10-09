print("Bienvenido a su cripto-mercado de confianza")
SaldoDisponible = int(input("Ingrese el monto que usará para invertir en criptomoneda: "))
Inversiones = 0
OpciónElegida = 1
while SaldoDisponible > 0 and OpciónElegida == 1 :
	print()
	print("Su saldo actual es de $",SaldoDisponible)
	monto = (int(input("¿Cuánto quiere invertir?")))

	if monto <= SaldoDisponible:
		SaldoDisponible = SaldoDisponible - monto
		Inversiones = Inversiones + 1
		
	else:
		print()
		print("Su dinero no es suficiente para esta inversión")
		print("Usted realizó un total de ",Inversiones," Inversiones exitosas")
		print()
		print("Su dinero sobrante: $",SaldoDisponible)
		OpciónElegida = int(input("""¿Desea seguir invirtiendo?
		1. Sí.
		2. No.					  """))

	


print("Usted realizó un total de ",Inversiones," inversiones exitosas.")
print("Su dinero sobrante: $",SaldoDisponible)







