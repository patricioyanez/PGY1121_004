# 1.- crear variables
from itertools import accumulate


contador = 0
acumlador= 0

# 2.- solicitar datos al usuario
print("**** Ejericicio contador y acumulador *****")
n1 = input("Ingrese número 1:")
n2 = input("Ingrese número 2:")
n3 = input("Ingrese número 3:")

# 3.- Procesar la información
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > 0 and n1 % 2 == 0:
    acumlador += n1  # acumulador = acumulador + n1
else:
    contador += 1

if n2 > 0 and n2 % 2 == 0:
    acumlador += n2
else:
    contador += 1


if n3 > 0 and n3 % 2 == 0:
    acumlador += n3  # acumulador = acumulador + n1
else:
    contador += 1

# 4.- Mostrar los resultados

print("Total de la suma     :", acumlador)
print("Total de la cuenta   :", contador)