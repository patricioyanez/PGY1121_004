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
            rut = int(input("Ingrese su rut: "))
        
            if rut < 4000000 or rut > 99999999:
                raise("El rut está fuera del rango")
        except:
            print("El rut no es válido")
            input("Presione enter para continuar......")
            continue
        
        nombre      = input("ingrese su nombre       : ")
        direccion   = input("ingrese su direccion    : ")
        comuna      = input("ingrese su comuna       : ")

        correo      = input("ingrese su correo       : ")

        if correo.count("@") != 1: # cuenta las apariciones del @
            print("El correo no es válido")
            input("Presione enter para continuar......")
            continue

        try:
            edad = int(input("Ingrese su edad: "))
        
            if edad < 0 or edad > 110:
                raise("La edad está fuera del rango")
        except:
            print("El edad no es válido")
            input("Presione enter para continuar......")
            continue

    elif opcion == 2:
        print("Seleccionó la opción 2")
    elif opcion == 3:
        print("Seleccionó la opción 3")
    elif opcion == 4:
        print("Aplicación cerrada")

    
    input("Presione enter para continuar.....")
