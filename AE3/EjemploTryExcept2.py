a = 5
b = 10 ### cambiar el cero por otro numero
try:
    c = a / b
    print("El resultado es:", c)
except:
    print("Error al tratar de dividir por cero")
else: # si no existe excepciones else se ejecuta.
    print("No ocurrio ningún error")
print("Fin del programa")