clientes = []
rut = ""
nombre = ""
direccion = ""
comuna = ""
correo = ""
edad = -1
genero = ""
celular =""
tipo =""
suscrito = True

opcion = 0

while opcion != 4:
    print("**************  M E N Ú - JUAN MAESTRO  **************")
    print("1.- Registro")
    print("2.- Suscripción")
    print("3.- Consultar")
    print("4.- Salir")

    try:
        opcion = int(input("Ingrese la opción:"))
    except:
        print("Error en el ingreso de la opción")
        input("Presione enter para continuar......")
        continue

    if opcion == 1:
        print("Seleccionó la opción 1")

        try:
            rut = int(input("Ingrese rut:"))

            if rut < 4000000 or rut > 99999999:
                print("Rut fuera de rango")
                raise("Error de rango")
        except:
            print("Error: Rut no es válido")
            input("Presione enter para continuar....")
            continue

        nombre      = input("ingrese su nombre       : ")
        direccion   = input("ingrese su direccion    : ")
        comuna      = input("ingrese su comuna       : ")
        correo      = input("ingrese su correo       : ")

        if correo.count("@") != 0:
            print("Error: Correo no es válido")
            input("Presione enter para continuar....")
            continue
        
        try:
            edad = int(input("Ingrese rut:"))

            if edad < 0 or edad > 110:
                print("Edad fuera de rango")
                raise("Error de rango")
        except:
            print("Error: Edad no es válido")
            input("Presione enter para continuar....")
            continue

        genero = input("ingrese su genero(F o M): ")
        genero = genero.upper()
        if genero != 'F' or genero != "M":
            print("Error: Género no es válido")
            input("Presione enter para continuar....")
            continue

        celular     = input("ingrese su celular      : ")
        tipo        = input("ingrese su tipo: 1.-PREMIUM 2.-GOLD 3.-SILVER:")

        if tipo == "1":
            tipo = "PREMIUM"
        elif tipo == "2":
            tipo = "GOLD"
        elif tipo == "3":
            tipo = "SILVER"
        else:
            print("Error: Tipo no es válido")
            input("Presione enter para continuar....")
            continue

        cliente = [rut, nombre, direccion, comuna, correo, edad,genero,celular,tipo, suscrito]
        clientes.append(cliente)
    elif opcion == 2:
        print("Seleccionó la opción 1")
    elif opcion == 3:
        print("Seleccionó la opción 1")
    elif opcion == 4:
        print("Aplicación cerrada")

    
    input("Presione enter para continuar.....")
