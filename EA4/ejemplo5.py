import numpy as num

matriz = num.array([ [1,2,3], [4,5,6]  ]) # 2x3
print(matriz)

print("Suma     :", matriz.sum())
print("Mayor    :", matriz.max())
print("Menor    :", matriz.min())
print("promedio :", matriz.mean())

print("El valor de la coordenada 1,1 es:", matriz[1,1])
print("El valor de la coordenada 0,2 es:", matriz[0,2])
print("El valor de la coordenada 1,2 es:", matriz[-1,-1])

print("datos:", matriz[0][1:3])
print("datos:", matriz[0,1:3])