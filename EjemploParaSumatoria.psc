Algoritmo EjemploParaSumatoria
	// EJERCICIOS solicitar un numero y Mostrar la sumatoria de este.
	Definir acumulador Como Entero
	Definir numero Como Entero
	
	Escribir "Ingrese un valor para la sumatoria"
	Leer numero
	
	Para i = 1 Hasta numero Hacer
		acumulador = acumulador + i
	FinPara
	
	Escribir "La sumatoria del número ", numero, " es ", acumulador 
	
FinAlgoritmo
