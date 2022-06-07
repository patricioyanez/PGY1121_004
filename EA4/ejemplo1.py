import numpy
arreglo = numpy.array([10,12,35,4,55,0,4,2,1,11])
print(arreglo)
print("Cantidad de dimensión:", arreglo.ndim, "dimensión")
print("Cantidad de elementos:", arreglo.shape)

# extraer porciones del arreglo
#  indice de busqueda aumenta en 1
print("Elementos seleccionados: ", arreglo[1:5]) 
#  indice de busqueda aumenta en 2 (ultimo parametro)
print("Elementos seleccionados: ", arreglo[1:9:2])
# toma todo el indice y aumenta 3 el indice de busqueda
print("Elementos seleccionados: ", arreglo[::3]) 
# se señala el indice de inicio y aumenta 4 el indice de busqueda
print("Elementos seleccionados: ", arreglo[2::4]) 
print("Elementos seleccionados: ", arreglo[:6:2]) 
print("último elemento: ", arreglo[-1]) 
print("prenúltimo elemento: ", arreglo[-2]) 
print("ante penúltimo elemento: ", arreglo[-3]) 
print("5to elemento: ", arreglo[4]) 
print("6to elemento: ", arreglo[5]) 
