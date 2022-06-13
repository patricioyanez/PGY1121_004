def calculo(precio , descuento):
    return precio - (precio * descuento / 100)

datos = [10000, 15]
print("Total a pagar es:", calculo(*datos))

datos = [25000, 10]
print("Total a pagar es:", calculo(*datos))