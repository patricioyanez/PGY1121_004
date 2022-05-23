listaCliente = []
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
    elif opcion == 2:
        print("Seleccionó la opción 1")
    elif opcion == 3:
        print("Seleccionó la opción 1")
    elif opcion == 4:
        print("Aplicación cerrada")

    
    input("Presione enter para continuar.....")
