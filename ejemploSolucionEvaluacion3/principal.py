# solución casi al 100%
from os import system
import funciones  # importa el contenido de las funciones del archivo
clientes = [] # debe ser un arreglo
opcion = 0
while opcion != 4:
    system("cls")
    print("#### BIENVENIDO ####")
    print("####     A      ####")
    print("##  AUTO SEGURO   ##")

    print("1) GRABAR  ")
    print("2) BUSCAR  ")
    print("3) IMPRIMIR CERTIFICADOS")
    print("4) SALIR  ")

    try:
        opcion = int(input("Ingrese opción : "))
    except:
        print("La opción no es correcta.")
        input("Presione enter para continuar....")
        continue
    
    if opcion < 1 or opcion > 4:
        print("La opción no es valida.")
        input("Presione enter para continuar....")
        continue
    else:
        if opcion == 1:
            funciones.opcion1(clientes) ## llama a la funcion definida en el archivo funciones.py. Se debe importar primero
        elif opcion == 2:
            funciones.opcion2(clientes)
        elif opcion == 3:
            funciones.opcion3(clientes)
        elif opcion == 4:        
            funciones.opcion4("nombre","apellido")