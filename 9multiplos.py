n = int(input("Ingrese un numero para saber sus multiplos entre 1 y 100 "))
print("Los multiplos de ",n," son: ")
for i in range(1,101):
	if i % n == 0:
		print(i)