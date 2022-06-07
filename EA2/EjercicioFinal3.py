# 1.- Definir variables
# 2.- Solicitar la info
print("\n ******  Muestra de tabla de multiplicar ******")
nro = int(input("Ingrese el número para la tabla: "))

# 3.- Procesar la info obtenida
# 4.- Mostrar resultado

if nro < 1:
    print("El número no es válido")
else:
    print(f"01 x {nro} =", (nro * 1))
    print("02 x", nro, "=", (nro*2))
    print(f"03 x {nro} =", (nro * 3))
    print(f"04 x {nro} =", (nro * 4))
    print(f"05 x {nro} =", (nro * 5))
    print(f"06 x {nro} =", (nro * 6))
    print(f"07 x {nro} =", (nro * 7))
    print(f"08 x {nro} =", (nro * 8))
    print(f"09 x {nro} =", (nro * 9))
    print(f"10 x {nro} =", (nro * 10))

