total = 0
opcion= 0

while opcion != 6:
    print("===== Super Panadería =====")
    print("1.- Amasado")
    print("2.- Molde")
    print("3.- Baguette")
    print("4.- Integral")
    print("5.- Total a pagar")
    print("6.- Salir del programa")
    try:
        opcion = int(input("Seleccione opción:"))
    except ValueError:
        input("Valor ingresado no es válido. Presione enter para continuar")
        continue

    if opcion < 1 or opcion > 6:
        print("=== Error: Opción no válida")
        input("Presione enter para continuar")
    elif opcion == 6:
        print("Adios!!! :) ")
    elif opcion == 5:
        if total < 5000:
            total *= 1.1
        else:
            print("El envio es gratis")
        print("El total de la compra es:", int(total))
        total = 0
    else: ## opcion dentro del rango
        try:
            cantidad = int(input("Ingrese cantidad a llevar: "))
        except ValueError:
            input("Valor ingresado no es válido. Presione enter para continuar")
            continue
        if opcion == 1:
            total  += cantidad * 1500
        elif opcion == 2:
            total  += cantidad * 1000
        elif opcion == 3:
            total  += cantidad * 2000
        elif opcion == 4:
            total  += cantidad * 3000

