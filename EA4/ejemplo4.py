import numpy as num

# operaciones de comparación y métodos estadísticos
a1 = num.array([1,2,3,4])
a2 = num.array([1,2,3,4])
a3 = num.array([1,7,3,6])

print("Resultado Igualdad   :", a1 == a2)
print("Resultado Igualdad   :", a1 == a3)
print("Resultado Mayor      :", a1 > a3)
print("Resultado Menor      :", a1 < a3)
print("Resultado Mayor=     :", a1 >=a3)
print("Resultado Menor=     :", a1 <=a3)

print("\n\n" , a1)
print("Suma     :", a1.sum())
print("Mayor    :", a1.max())
print("Menor    :", a1.min())
print("promedio :", a1.mean())


print("Suma     :", sum(a1))
print("Mayor    :", max(a1))
print("Menor    :", min(a1))
