Algoritmo EjemploMiestrasMenu
	Definir opcion Como Entero
	
	opcion = 0
	
	Mientras opcion <> 4 Hacer
		Limpiar Pantalla
		Escribir "*******  Ejemplo de un menú  ********"
		Escribir "1.- Saludar"
		Escribir "2.- Despedirse"
		Escribir "3.- Otro"
		Escribir "4.- Salir"
		Escribir "Ingrese la opcion:"
		Leer opcion
		si opcion = 1 Entonces
			Escribir "Hola Mamá hermosa :) Te quero mx"
			Escribir "Presione cualquier tecla para continuar"
			Esperar Tecla
			
		FinSi
		si opcion = 2 Entonces
			Escribir "Chaoooo Mamá hermosa :) , nos vimos!!!"
			Escribir "Presione cualquier tecla para continuar"
			Esperar Tecla
			
		FinSi
	FinMientras
	Escribir "Se ha cerrado el sistema"
FinAlgoritmo
