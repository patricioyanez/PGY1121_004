def resta(num1 = None, num2 = None):
    if num1 == None or num2 == None:
        print("Debe especificar ambos valores")
        return 0
    return num1 - num2

def resta2(num1, num2):
    return num1 - num2

resta()
resta(1)
print("El resultado es ",resta(10,6))

res = resta(15,3)
print("El resultado es ", res)
print("El resultado es ", resta2())