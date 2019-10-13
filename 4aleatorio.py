from random import *

a = 0
print("ADIVINA EL NUMERO ALEATORIO")

while True:
	a = a+1
	
	x = int(input("Ingrese un numero entre 1 y 10: "))
	print("NUMERO ALEATORIO ",randint(1,10))
	
	n = int(input("Tu numero es mayor, menor o igual al numero aleatorio?\n\t1-Mayor  \t2-Menor  \t3-Igual   "))

	if n == 1:
		print("Sigue intentando")
	elif n == 2:
		print("Oh vaya! Sigue intentando")
	elif n == 3:
		print("Buen trabajo!")
		print("Lo lograste en ",a," intentos")
		j = int(input("QUIERES SEGUIR JUGANDO? 1-SI  2-NO  "))
		if j == 1:
			print(" ")
		elif j == 2:
			print("Muy bien. Luego mejoras tus ",a," intentos")
			break
	else:
		print("EL NUMERO INGRESADO NO ES UNA OPCION!!!")