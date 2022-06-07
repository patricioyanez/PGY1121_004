print("Ingrese numero para analizar:")
n1 = int(input("Ingrese el numero: "))

if n1 > 999:
    print("Nro supera la cantidad de digitos esperados")
elif n1 > 99:
    print("el NUMERO TIENE 3 DIGITOS")
elif n1 > 9:
        print("el NUMERO TIENE 2 DIGITOS")
else:
        print("el NUMERO TIENE 1 DIGITOS")