print("Cajero Auntomatico")
print("Su Saldo es $1000.00")


print("\t1 - Hacer un Retiro")
print("\t2 - Hacer un Deposito")

x = float(input("Ingrese una opcion "))

if x == 1:
	c = float(input("Ingrese la cantidad a retirar "))
	if c > 1000:
		print("Cuenta sin fondos!")
	else:
		d = 1000-c
		print("Retiro exitoso!")
		print("Usted a retirado ",c)
		print("Su saldo actual es ",d)

elif x == 2:
	c = float(input("Ingrese la cantidad a depositar "))
	d = 1000+c
	print("Deposito exitoso!")
	print("Usted a depositado ",c)
	print("Su saldo actual es ",d)




	