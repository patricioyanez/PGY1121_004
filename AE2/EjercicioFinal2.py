# 1.- Definir variables
# 2.- Solicitar la info
print("\n ******  Registro de datos ******")
nombre  = input("Ingrese el nombre                    : ")
edad    = input("Ingrese el edad                      : ")
telefono= input("Ingrese el teléfono                  : ")
genero  = input("Ingrese el género 1.- varón 2.- Mujer: ")

# 3.- Procesar la info obtenida
# 4.- Mostrar resultado

if genero == "1":
    print("Su nombre es {nombre} y su edad {edad}")
else:
    print("Su nombre es", nombre, " y su teléfono", telefono)
