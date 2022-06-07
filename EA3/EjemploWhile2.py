# 1.- definir variables
contador = 1
acumulador = 1
# 2.- solicitar info
print("\n **** factorial *****")
numero = int(input("Ingrese un número:"))
# 3.- procesar info
while contador <= numero:
    acumulador *= contador
    contador += 1
# 4.- Mostrar resultado
print("El factorial de {} es {}".format(numero,acumulador))