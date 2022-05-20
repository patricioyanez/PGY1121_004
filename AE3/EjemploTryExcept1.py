a = 5
b = 0
try:
    c = a / b
    print("El resultado es:", c)
except ZeroDivisionError:
    print("Error al tratar de dividir por cero")
except:
    print("Ocurrio un error")
print("Fin del programa")