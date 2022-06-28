from os import system

def opcion1(arreglo):
    system("cls")
    patente = ""
    tipo = ""
    marca = ""
    precio = ""
    multa = ""
    aprobacion  = ""
    fecha =""
    nombre = ""
    apellido = ""
    print("LA OPCION SELECCIONADA ES 1")

    try:
        patente = input("INGRESE LA PATENTE: ")

        if patente == "" or len(patente) != 6 :
            raise("Patente no encontrada")
            
    except:
        print("Patente no valida")
        input("Presione enter para continuar....")
        return

    print("##################TIPOS DE AUTOS#################")
    print("1)SUV 2)SedÃ¡n 3)Hatchback 4)Pick-Up 5)Todoterreno")
    print("6)VAN    7)Descapotable      8)CUV     9)City Car")

    tipo = input("SELECCIONE EL TIPO DE AUTO: ")
    
    if tipo == "1":
        tipo = "SUV"
    elif tipo == "2":
        tipo = "SedÃ¡n" 
    elif tipo == "3":
        tipo = "Hatchback"
    elif tipo == "4":
        tipo = "Pick-Up"
    elif tipo == "5":
        tipo = "Todoterreno"
    elif tipo == "6":
        tipo = "VAN"
    elif tipo == "7":
        tipo = "Descapotable"
    elif tipo == "8":
        tipo = "CUV"
    elif tipo == "9":
        tipo = "City Car"

    else:
        print("Tipo no valido")
        input("Presione enter para continuar....")
        return

    try:
        system("cls")
        print("LA PATENTE DEL AUTO INGRESADO ES: ", patente)
        print("EL  TIPO  DE  AUTO  INGRESADO ES: ", tipo)
        print("'''''''''''''''''''''''''''''''''''''''''''''''''")
        marca = str(input("INGRESE LA MARCA DEL AUTO   : "))

        if len(marca) <=2  or len(marca) >=15:
            raise("Marca Invalida")    
    except:
        print("Marca no valida")
        input("Presione enter para continuar....")
        return
    try:
        precio      = int(input("INGRESE EL PRECIO DEL AUTO  : "))
        if precio < 5000000 or precio > 99999999:
            raise("Precio fuera de rango")    
    except:
        print("Precio no valido")
        input("Presione enter para continuar....")
        return  
    try:        
        multa = int(input("INGRESE EL VALOR DE LA MULTA: "))
        if multa < 0 or multa > 999999999:
            raise("Multa fuera de rango")    
    except:
        print("Multa no valida")
        input("Presione enter para continuar....")
        return

    print("EMISION DE CONTAMINANTES")
    print("  1)SI ESTÃ APROBADO")
    print("  2)NO ESTÃ APROBADO")
    
    aprobacion = input("INGRESE UNA OPCIÃ“N:")

    if aprobacion == "1":
        aprobacion = "Aprobado"
    elif aprobacion == "2":
        aprobacion = "No aprobado" 
    else:
        print("AprobaciÃ³n no valida")
        input("Presione enter para continuar....")
        return

    fecha = input("INGRESE LA FECHA DE REGISTRO: ")
    if fecha.find("/") == -2:
        print("fecha no valida")
        input("Presione enter para continuar....")
        return

    nombre = input("INGRESE SU PRIMER NOMBRE  : ")
    apellido = input("INGRESE SU PRIMER APELLIDO: ")


    cliente = [patente, tipo, marca, precio, multa, aprobacion, fecha, nombre, apellido]

    arreglo.append(cliente)

def opcion2(arreglo):
    print("La opción seleccionada es 2")
    try:
        patente = input("Ingrese la patente: ")
        if patente == "" or len(patente) != 6 :
            raise("Patente no encontrada")    
    except:
        print("Patente no valida")
        input("Presione enter para continuar....")
        return
    
    clienteEncontrado = []
    for cliente in arreglo:
        if cliente[0] == patente:
            clienteEncontrado = cliente
            break
    
    if len(clienteEncontrado) == 0:
        print("Patente no encontrada")
    else:
        print("\n==== Datos de la patente encontrado ====")
        print("Patente        : ", clienteEncontrado[0])
        print("Tipo           : ", clienteEncontrado[1])
        print("Marca          : ", clienteEncontrado[2])
        print("Precio         : ", clienteEncontrado[3])
        print("Multa          : ", clienteEncontrado[4])
        print("Aprobacion     : ", clienteEncontrado[5])
        print("Fecha          : ", clienteEncontrado[6])
        print("Nombre         : ", clienteEncontrado[7])
        print("Apellido       : ", clienteEncontrado[8])

def opcion3(arreglo):
    import random
    valor= random.randint(1500,3500)
    print("Usted imprimirÃ¡ el certificado del vehí­culo")
    print("\n==== Certificado ====")
    print("Patente        : ", arreglo[0])
    print("Tipo           : ", arreglo[1])
    print("Marca          : ", arreglo[2])
    print("Precio         : ", arreglo[3])
    print("Multa          : ", arreglo[4])
    print("Aprobacion     : ", arreglo[5])
    print("Fecha          : ", arreglo[6])
    print("Nombre         : ", arreglo[7])
    print("Apellido       : ", arreglo[8])
    print(f"El valor es de : {valor}")
    print("Los datos registrados son: ")

def opcion4(nombre,apellido):
    print("Hasta pronto") 
    print(f"{nombre} {apellido}") 
    print("V 3.2 ") 