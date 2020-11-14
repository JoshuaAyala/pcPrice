import os

Procesador = "* Intel Core i3 9100F."
ProcesadorPrice = 1946.49

Disipador = "* Aerocool RGB 120mm"
DisipadorPrice = 399.00

Motherboard = "* GIGABYTE B365 DS3H."
MotherboardPrice = 1805.16

RAMmemory = "* Memoria RAM 16 GB DDR4 3000MHz Marca HyperX Fury."
RAMmemoryPrice = 1199.00

SSDisk = "* Unidad de estado sólido SSD Sata 120GB Marca ADATA."
SSDiskPrice = 499.00

HDDisk = "* Disco Duro interno 1TB WD."
HDDiskPrice = 954.38

TarjetaGrafica = "* NVIDIA GTX 1650 Super."
TarjetaGraficaPrice = 4299.00

Fuentedepoder = "* Fuente de poder 500w 80+ white."
FuentedepoderPrice = 999.00

envio = 119.00

os.system('clear')

print("#############")
print("   WELCOME	")
print("#############\n")
print("¿Qué quieres hacer?\n[1] Precio de todos los componentes.\n[2] Precio total de PC.\n[3] Asignar presupuesto.")
decision = int(input(">: "))
if(decision==1):
	print(Procesador)
	print("	Precio: $", ProcesadorPrice)
	print(Disipador)
	print("	Precio: $", DisipadorPrice)
	print(Motherboard)
	print("	Precio: $", MotherboardPrice)
	print(RAMmemory)
	print("	Precio: $", RAMmemoryPrice)
	print(SSDisk)
	print("	Precio: $", SSDiskPrice)
	print(HDDisk)
	print("	Precio: $", HDDiskPrice)
	print(TarjetaGrafica)
	print("	Precio: $", TarjetaGraficaPrice)
	print(Fuentedepoder)
	print("	Precio: $", FuentedepoderPrice)
elif(decision==2):
	envio = 0
	subtotal = ProcesadorPrice + DisipadorPrice + MotherboardPrice + RAMmemoryPrice + SSDiskPrice + HDDiskPrice + TarjetaGraficaPrice + FuentedepoderPrice
	print("Subtotal: $", subtotal)
	seguro = subtotal/100
	print("Seguro: $", seguro)
	total = subtotal + envio + seguro
	print("Envio: $", envio)
	print("#####################################")
	print("Total: $", total, " IVA INCLUIDO.")
	print("#####################################")
	print("\nCOMPRAS A MAYOR DE $4000 envío gratis.")
elif(decision==3):
	presupuesto = int(input("Presupuesto: "))
	if(presupuesto<=1500 and presupuesto>RAMmemoryPrice):
		print(RAMmemory)
		print("	Precio: $", RAMmemoryPrice)
		subtotal =  RAMmemoryPrice
		print("Subtotal: $", subtotal)
		seguro = subtotal/100
		print("Seguro: $", seguro)
		total = subtotal + envio + seguro
		print("Envio: $", envio)
		print("#####################################")
		print("Total: $", total, " IVA INCLUIDO.")
		print("Cambio: $", presupuesto - total)
		print("#####################################")
		print("\nCOMPRAS A MAYOR DE $4000 envío gratis.")
	elif(presupuesto<=2000 and presupuesto>1500):
		print(SSDisk)
		print("	Precio: $", SSDiskPrice)
		print(RAMmemory)
		print("	Precio: $", RAMmemoryPrice)
		# OPERACIONES Y RESULTADO
		subtotal = SSDiskPrice + RAMmemoryPrice
		print("Subtotal: $", subtotal)
		seguro = subtotal/100
		print("Seguro: $", seguro)
		total = subtotal + envio + seguro
		print("Envio: $", envio)
		print("#####################################")
		print("Total: $", total, " IVA INCLUIDO.")
		print("Cambio: $", presupuesto - total)
		print("#####################################")
		print("\nCOMPRAS A MAYOR DE $4000 envío gratis.")
	elif(presupuesto<=2500 and presupuesto>2000):
		print(RAMmemory)
		print("	Precio: $", RAMmemoryPrice)
		print(HDDisk)
		print("	Precio: $", HDDiskPrice)
		# OPERACIONES
		subtotal = HDDiskPrice + RAMmemoryPrice
		print("Subtotal: $", subtotal)
		seguro = subtotal/100
		print("Seguro: $", seguro)
		total = subtotal + envio + seguro
		print("Envio: $", envio)
		print("#####################################")
		print("Total: $", total, " IVA INCLUIDO.")
		print("Cambio: $", presupuesto - total)
		print("#####################################")
		print("\nCOMPRAS A MAYOR DE $4000 envío gratis.")
	elif(presupuesto<=3000 and presupuesto>2500):
		print(RAMmemory)
		print("	Precio: $", RAMmemoryPrice)
		print(HDDisk)
		print("	Precio: $", HDDiskPrice)
		print(SSDisk)
		print("	Precio: $", SSDiskPrice)
		subtotal = HDDiskPrice + RAMmemoryPrice + SSDiskPrice
		print("Subtotal: $", subtotal)
		seguro = subtotal/100
		print("Seguro: $", seguro)
		total = subtotal + envio + seguro
		print("Envio: $", envio)
		print("#####################################")
		print("Total: $", total, " IVA INCLUIDO.")
		print("Cambio: $", presupuesto - total)
		print("#####################################")
		print("\nCOMPRAS A MAYOR DE $4000 envío gratis.")
	elif(presupuesto<=3500 and presupuesto>3000):
		print(Procesador)
		print("	Precio: $", ProcesadorPrice)
		print(RAMmemory)
		print("	Precio: $", RAMmemoryPrice)
		subtotal =  RAMmemoryPrice + ProcesadorPrice
		print("Subtotal: $", subtotal)
		seguro = subtotal/100
		print("Seguro: $", seguro)
		total = subtotal + envio + seguro
		print("Envio: $", envio)
		print("#####################################")
		print("Total: $", total, " IVA INCLUIDO.")
		print("Cambio: $", presupuesto - total)
		print("#####################################")
		print("\nCOMPRAS A MAYOR DE $4000 envío gratis.")
	elif(presupuesto<=4000 and presupuesto>3500):
		envio = 0
		print(Procesador)
		print("	Precio: $", ProcesadorPrice)
		print(RAMmemory)
		print("	Precio: $", RAMmemoryPrice)
		print(SSDisk)
		print("	Precio: $", SSDiskPrice)
		subtotal =  RAMmemoryPrice + ProcesadorPrice + SSDiskPrice
		print("Subtotal: $", subtotal)
		seguro = subtotal/100
		print("Seguro: $", seguro)
		total = subtotal + envio + seguro
		print("Envio: $", envio)
		print("#####################################")
		print("Total: $", total, " IVA INCLUIDO.")
		print("Cambio: $", presupuesto - total)
		print("#####################################")
	elif(presupuesto<=4500 and presupuesto>4000):
		envio = 0
		gtxdisponible = int(input("¿GTX 1650 Super sigue disponible?\n[1] Sí.\n[2] No.\n>: "))
		if(gtxdisponible==1):
			print(TarjetaGrafica)
			print("	Precio: $", TarjetaGraficaPrice)
			subtotal =  TarjetaGraficaPrice
			print("Subtotal: $", subtotal)
			seguro = subtotal/100
			print("Seguro: $", seguro)
			total = subtotal + envio + seguro
			print("Envio: $", envio)
			print("#####################################")
			print("Total: $", total, " IVA INCLUIDO.")
			print("Cambio: $", presupuesto - total)
			print("#####################################")
		elif(gtxdisponible==2):
			print(Procesador)
			print("	Precio: $", ProcesadorPrice)
			print(RAMmemory)
			print("	Precio: $", RAMmemoryPrice)
			print(HDDisk)
			print("	Precio: $", HDDiskPrice)
			print(SSDisk)
			print("	Precio: $", SSDiskPrice)
			subtotal =  ProcesadorPrice + RAMmemoryPrice + HDDiskPrice + SSDiskPrice
			print("Subtotal: $", subtotal)
			seguro = subtotal/100
			print("Seguro: $", seguro)
			total = subtotal + envio + seguro
			print("Envio: $", envio)
			print("#####################################")
			print("Total: $", total, " IVA INCLUIDO.")
			print("Cambio: $", presupuesto - total)
			print("#####################################")
	elif(presupuesto<=5000 and presupuesto>4500):
		envio = 0
		gtxdisponible = int(input("¿GTX 1650 Super sigue disponible?\n[1] Sí.\n[2] No.\n>: "))
		if(gtxdisponible==1):
			print(TarjetaGrafica)
			print("	Precio: $", TarjetaGraficaPrice)
			print(SSDisk)
			print("	Precio: $", SSDiskPrice)
			subtotal =  TarjetaGraficaPrice + SSDiskPrice
			print("Subtotal: $", subtotal)
			seguro = subtotal/100
			print("Seguro: $", seguro)
			total = subtotal + envio + seguro
			print("Envio: $", envio)
			print("#####################################")
			print("Total: $", total, " IVA INCLUIDO.")
			print("Cambio: $", presupuesto - total)
			print("#####################################")
		elif(gtxdisponible==2):
			print(Procesador)
			print("	Precio: $", ProcesadorPrice)
			print(RAMmemory)
			print("	Precio: $", RAMmemoryPrice)
			print(Motherboard)
			print("	Precio: $", MotherboardPrice)
			subtotal =  ProcesadorPrice + RAMmemoryPrice + MotherboardPrice
			print("Subtotal: $", subtotal)
			seguro = subtotal/100
			print("Seguro: $", seguro)
			total = subtotal + envio + seguro
			print("Envio: $", envio)
			print("#####################################")
			print("Total: $", total, " IVA INCLUIDO.")
			print("Cambio: $", presupuesto - total)
			print("#####################################")
	else:
		print("Presupuesto insuficiente.")