# definicion de funcion (no se ejecuta a menos que se llame)
def sumar(numero1, numero2):
    total = numero1 + numero2
    print(f"Total: {total}")

def sumar2(numero1, numero2):
    total = numero1 + numero2
    return total

num1 = int(input("Ingrese nro 1:"))
num2 = int(input("Ingrese nro 2:"))

## llama a la función
sumar(num1,num2)
print("El total es:", sumar2(num1,num2))
print("**** Fin del programa ****")