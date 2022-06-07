flag = True
nro = 0
print("\n===== Invertir números =====")

while flag:
    nro = int(input("Ingrese número:"))

    if nro >= 103  and nro <= 981:
        flag = False
'''
nro = 0
while nro < 103  or nro > 981:    
    nro = int(input("Ingrese número n2:"))
print(nro)
'''
unidad = int(nro / 100)
decena = int(nro / 10) - (unidad * 10)
centena= nro - (unidad * 100 + decena * 10)

print(unidad, decena, centena)
print(centena * 100 + decena * 10 + unidad)