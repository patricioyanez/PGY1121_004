Algoritmo EjemploParaSumatoria
	// EJERCICIO: solicitar un numero y Mostrar su factorial.
	Definir acumulador Como Entero
	Definir numero Como Entero
	
	Escribir "Ingrese un valor para el factorial"
	Leer numero
	acumulador = 1
	Para i = 1 Hasta numero Hacer
		acumulador = acumulador * i
	FinPara
	
	Escribir "El factorial del número ", numero, " es ", acumulador 
	
FinAlgoritmo