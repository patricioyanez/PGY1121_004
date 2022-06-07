# definir variables
totalPesos = 0
# solitar datos al usuario
print("***** Super convertidor a Pesos Chilenos de Chile ******")
print("1.- Dolar Australiano")
print("2.- Pesos Argentinos")
print("3.- Yen")
opcion = input("Ingrese opción de moneda: ")
cantidad= input("Ingrese la cantidad a convertir: ")
# procesar datos
cantidad = float(cantidad)
if opcion == "1":
    totalPesos = 609.26 * cantidad
elif opcion == "2":
    totalPesos = 7.43 * cantidad
else:
    totalPesos = 6.66 * cantidad
# mostrar resultados
print("El total en pesos es: ", totalPesos)