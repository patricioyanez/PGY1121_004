# instalar e importar numpy ==> pip install numpy
import numpy as nu
casillero = nu.array([ ["", "", ""], 
                        ["", "", ""], 
                        ["", "", ""] ], dtype = object)

# definir funciones
def arrendar(casillero):
    pass
def mostrarUbicaciones(casillero):
    pass
def mostrarNombre(casillero):
    pass
def calcularGanancias(casillero):
    pass

# definir aplicacion
opcion= 0
listadoDeOpciones = ["1", "2", "3", "4", "5"]
while opcion != "5":
    print("===== Arriendo de casilleros =====")
    print("1.- Arrendar")
    print("2.- Mostrar ubicaciones disponibles")
    print("3.- Listar nombres de cliente")
    print("4.- Calcular ganancias")
    print("5.- Salir del programa")
    opcion = input("Seleccione opción:")

    if opcion not in listadoDeOpciones:
        print("=== Error: Opción no válida")
        input("Presione enter para continuar...")
        continue
    if opcion == "5":
        print("Adios!!!   :)")
    else:
        if opcion == "1":
            arrendar(casillero)
        elif opcion == "2":
            mostrarUbicaciones(casillero)
        elif opcion == "3":
            mostrarNombre(casillero)
        elif opcion == "4":
            calcularGanancias(casillero)
