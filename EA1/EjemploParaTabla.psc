Algoritmo EjemploParaSumatoria
	// EJERCICIO: Mostrar la tabla del 1 al 10 del numero determinado por el usuario
	// crear las variables
	Definir total Como Entero
	Definir numero Como Entero
	// solicitar los datos
	Escribir "Ingrese el valor para multiplicar"
	Leer numero
	
	//Procesar la información Y MOSTRAR EL RESULTADO
	Para i = 1 Hasta 10 Hacer
		total = numero * i
		Escribir i, " x ", numero, " = ", total
	FinPara
	
FinAlgoritmo