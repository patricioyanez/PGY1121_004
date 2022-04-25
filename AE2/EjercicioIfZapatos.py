print("******* Super Zapatería *******")
nro = input("Ingrese número de zapato: ")
cantidad = input("Ingrese cantidad de pares: ")
cantidad = int(cantidad)
total = 0

if cantidad < 2:
    total = 23000
else:
    total = 20000 * cantidad

print("==== Total a pagar ====")
print("total a pagar: ", total)
