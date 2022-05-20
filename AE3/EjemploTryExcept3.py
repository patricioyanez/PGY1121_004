a = 5
b = 0 
try:
    c = a / b
    print("El resultado es:", c)
except:
    print("Error al tratar de dividir por cero")
finally: 
    print("El bloque TRY EXCEPT ha finalizado con éxito")
print("Fin del programa")