import numpy as num

# operaciones aritméticas con arreglos

a1 = num.array([1,2,3,4])
print(a1)

a1 = a1 + 1
print(a1)
a1 += 1
print(a1)

a1 **= 2
print(a1)

a2 = num.ones(10)
print(a2)
a2 += 4
print(a2)
a3 = num.ones(10)
print("suma de arreglos", a3 + a2)