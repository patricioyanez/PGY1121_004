try:
    numero = input("Ingrese un numero:")

    if not type(numero) is int:
        raise("El valor ingresado no es un INT")
except:
    print("Ocurrio un error de tipo de datos")
finally:
    print("Bloque terminado")
    
print("Aplicación cerrada")