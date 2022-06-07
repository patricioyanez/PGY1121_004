# 1.- declarar variables si es necesario
subtotal = 0
valor = 0
descuento = 0
totalPorCobrar = 0

# 2.- Solicitar la información al usuario
print("****** CINE DUOC ********")
print("Ud pertenece a DuocUc Plaza Oeste")
esDeDuoc = input("Presione\n1.-Si\n2.-No\npara ingresar info:")

print("==== Tipo de entrada ====")
print("1.-Estreno")
print("2.-Normal")
tipoEntrada = input("Selecccione opción:")
unidadesTipoEntrada = input("Ingrese cantidad de boletos:")


print("==== Palomitas de maíz ====")
print("1.- Pequeño")
print("2.- Mediano")
print("3.- Grande")
palomitas = input("Selecccione opción:")
unidadesPalomitas = input("Ingrese cantidad de palomitas:")

print("==== Bebidas ====")
print("1.- Pequeño")
print("2.- Mediano")
print("3.- Grande")
bebidas = input("Selecccione opción:")
unidadesBebidas = input("Ingrese cantidad de bebidas:")


# 3.- Procesar información
if tipoEntrada == "1": # int(tipoEntrada) == 1:
    valor = 4800
else:
    valor = 2900

subtotal =  valor * int(unidadesTipoEntrada)

if palomitas == "1": 
    valor = 2500
elif palomitas == "2": 
    valor = 4500
else:
    valor = 7800

subtotal = subtotal + valor * int(unidadesPalomitas)

if bebidas == "1": 
    valor = 1000
elif palomitas == "2": 
    valor = 1250
else:
    valor = 2000

subtotal = subtotal + valor * int(unidadesBebidas)

if esDeDuoc == "1":
    descuento = subtotal * .3

print("El total de compra es:")
print("SubTotal      : " , subtotal)
print("Descuento     : " , descuento)
print("Total a pagar : " , (subtotal- descuento))
