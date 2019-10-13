
print("Convertor de °F a °C, °C a °F, Kelvin a °C, °C a Kelvin, Kelvin a °F y °F a Kelvin")



def FC():
	f = float(input("Ingrese los grados Fahrenheit que desea convertir: "))
	c = ((f-32)/1.8)
	print("Equivale a ",c,"°C")

def CF():
	c = float(input("Ingrese los grados Celsius que desea convertir: "))
	f = ((c*1.8)+32)
	print("Equivale a ",f,"°F")

def KC():
	k = float(input("Ingrese los Kelvin que desea convertir: "))
	c = k-273.15
	print("Equivale a ",c,"°C")

def CK():
	c = float(input("Ingrese los grados Celsius que desea convertir: "))
	k = c+273.15
	print("Equivale a ",k,"Kelvin")

def KF():
	k = float(input("Ingrese los Kelvin que desea convertir: "))
	a = k-273.15
	f = (1.8*a)+32
	print("Equivale a ",f,"°F")

def FK():
	f = float(input("Ingrese los grados Fahrenheit que desea convertir: "))
	k = ((f-32)/1.8)+273.15
	print("Equivale a ",k,"Kelvin")

while True:
	print("ELIJA LA CONVERCION QUE DESEA HACER")
	opcion = int(input("\t1 - Fahrenheit a Celsius\n\t2 - Celsius a Fahrenheit\n\t3 - Kelvin a Celsius\n\t4 - Celsius a Kelvin\n\t5 - Kelvin a Fahrenheit\n"
"\t6 - Fahrenheit a Kelvin\n\t7 - Salir\n Opcion: "))

	if opcion == 1:
		FC()
	elif opcion == 2:
		CF()
	elif opcion == 3:
		KC()
	elif opcion == 4:
		CK()
	elif opcion == 5:
		KF()
	elif opcion == 6:
		FK()
	elif opcion == 7:
		print("Hasta luego!")
		break
else:
	print("Opcion no disponible!")



	