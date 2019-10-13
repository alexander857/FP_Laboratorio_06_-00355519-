numero = int(input("Ingresa un numero: "))

while numero > 0:
    resto = numero % 10
    numero = int(numero / 10)
    print("%d" % (resto), end = "")