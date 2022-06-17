# instalar e importar numpy ==> pip install numpy
import numpy as nu
casillero = nu.array([ ["", "", ""], 
                        ["", "", ""], 
                        ["", "", ""] ], dtype = object)

# definir funciones
def arrendar(casillero):
    print("=== Arrendar casillero ===")
    print("1.- nivel 1 $ 10.000")
    print("2.- nivel 2 $  5.000")
    print("3.- nivel 3 $  2.000")

    try:
        opcion = int(input("Ingrese nivel del casillero: ")) # fila
        fila = opcion - 1
        casillerosDisponibles(casillero, fila)
        nroCasillero = int(input("Ingrese nivel del casillero: ")) # columna
        columna = nroCasillero - 1
        nombre = input("Ingrese el nombre          : ")
        casillero[fila, columna] = nombre
#        print(casillero)
    except:
        print("=== Error: Opción no válida")
        input("Presione enter para continuar...")        


def casillerosDisponibles(casillero, fila):
    print("Casilleros disponibles de la fila ", fila+1)
    nroCasillero = 1
    for columna in casillero[fila]:
        if columna == "":
            print("Casillero ", nroCasillero)
        nroCasillero += 1


def mostrarUbicaciones(casillero):
    print("*** Disponibilidad de casilleros ***")
    filas = ""
    nroCasillero = 1
    valor = ""
    for fila in casillero:
        for columna in fila:
            if columna == "":
                valor = str(nroCasillero)
            else:
                valor = "X"
            filas += valor + " " 
            nroCasillero += 1
        filas += "\n"
    print(filas)
    input("Presione enter para continuar...") 


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
