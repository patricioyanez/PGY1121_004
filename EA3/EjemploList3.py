lista1 = [1,2,3,4]
print(lista1)
lista1.remove(2) # si el valor no existe, lanza una excepción
print(lista1)

# elimina el ultimo elemento, opcional: rescata el valor
nro = lista1.pop()
print(lista1)
print("Valor Eliminado:", nro)

lista1.insert(1, 2)
lista1.append(4)
print(lista1)
nro = lista1.pop(2)
print(lista1)
print("Valor Eliminado:", nro)
