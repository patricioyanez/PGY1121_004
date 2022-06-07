# 1.- Definir variables
total = 0
descuento = 0
# 2.- Solicitar la info
print("\n ******  Ventas de insumos ******")
print("=== Ingrese cantidades")
mascarillas = input("Mascarillas:")
guante = input("Guante     :") # guanteClinico
delantal = input("Delantal   :")
amonio = input("Amonio     :")
tieneCodigo = input("Tiene código de descuento 1.-Si 2.-No: ")

# 3.- Procesar la info obtenida
total = total + int(mascarillas) * 1000
total += int(guante) * 1000
total += int(delantal) * 2000
total += int(amonio) * 3000

if tieneCodigo == "1":
    descuento = int(input("Ingrese el % de descuento:"))
    total -= total * descuento / 100
# 4.- Mostrar resultado
print("El total a pagar es:", int(total))