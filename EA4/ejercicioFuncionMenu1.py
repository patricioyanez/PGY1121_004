opcion= 0
listadoDeOpciones = ["1", "2", "3", "4", "5"]
while opcion != "5":
    print("===== Super Calculadora =====")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Multiplicar")
    print("4.- Dividir")
    print("5.- Salir del programa")
    opcion = input("Seleccione opción:")

    if opcion not in listadoDeOpciones:
        print("=== Error: Opción no válida")
        input("Presione enter para continuar...")
        continue
    if opcion == 5:
        print("Adios!!! :) ")
    else:
        try:
            num1 = int(input("Ingrese 1er nro:"))
            num2 = int(input("Ingrese 2do nro:"))
        except:
            print("=== Error: Número no válido.")
            input("Presione enter para continuar...")
            continue

        resultado = ""

        if opcion == "1":
            resultado = sumar(num1, num2)
        elif opcion == "2":
            resultado = restar(num1, num2)
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
        elif opcion == "4":
            resultado = dividir(num1, num2)

        print("El resultado es:", resultado)
        input("Presione enter para continuar...")