print("Promocion de 3 Peliculas")
print("Ingrese el precio de las tres peliculas")
p1 = int(input("Pelicula #1 "))
p2 = int(input("Pelicula #2 "))
p3 = int(input("Pelicula #3 "))

if p1 < p2:
	if p2 < p3:
		print("El precio a pagar es ",p1+p2,)
	else:
		print("El precio a pagar es ",p1+p3)
elif p1 > p2 and p1 > p3:
	print("El precio a pagar es ",p2+p3,)

