numero = 10
numero = numero + 1
print(numero)
nombre = "Juan"
print(nombre)

print("Ingrese su personaje favorito de SNK")
nombre = input() # lee el teclado, devuelve siempre un string
apellido = input("¿Cúal es el apellido?:")

print("Su personaje es: ", nombre, apellido)
edad = int(input("¿Cúal es su edad?")) #convierte a numero el str
edad = edad + 2
print("Su edad es:", edad)

nombre = nombre + str(edad)
print(nombre)