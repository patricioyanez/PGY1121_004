try:
    numero = int(input("Ingrese un numero:"))
except ValueError:
    print("Valor ingresado no es válido")
finally:
    print("Bloque terminado")
    
print("Aplicación cerrada")