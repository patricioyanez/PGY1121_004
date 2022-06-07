# 1.- Definir variables
# 2.- Solicitar la info
print("\n ******  Buscar el mayor ******")
n1 = input("Ingrese el 1er número: ")
n2 = input("Ingrese el 2do número: ")
n3 = input("Ingrese el 3er número: ")

# 3.- Procesar la info obtenida
# 4.- Mostrar resultado
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print("El 1er nro es mayor")
elif n2 > n3:
    print("El 2do nro es mayor")
else:
    print("El 3er nro es mayor")

