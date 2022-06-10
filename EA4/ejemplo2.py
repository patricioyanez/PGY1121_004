import numpy as num

# Métodos en numpy
arreglo = num.arange(10)
print(arreglo)
arreglo = num.arange(10.0)
print(arreglo)
arreglo = num.arange(4, 10)
print(arreglo)
arreglo = num.arange(2, 11, 2)
print(arreglo)
arreglo = num.arange(1, 11, 2)
print(arreglo)

a1 = arreglo
a1[0] = 1500
print(arreglo)

arreglo[0] = 1

print(arreglo)
print(a1)

a2 = a1.copy()
a2[0]= 2000
print("*****")
print(a1)
print(a2)