Algoritmo Ejercicio1
	// crear variables
	Definir sueldo1 Como Entero
	Definir sueldo2 Como Entero
	Definir sueldo3 Como Entero
	
	// solicitar datos al usuario
	Escribir "Ingrese el primer sueldo:"
	Leer sueldo1
	Escribir "Ingrese el segndo sueldo:"
	Leer sueldo2	
	Escribir "Ingrese el tercer sueldo:"
	Leer sueldo3	
	
	//procesar la información
	si sueldo1 > sueldo2 Entonces // y sueldo1 > sueldo3  Entonces
		si sueldo1 > sueldo3 Entonces
			Escribir "Sueldo 1 es el mayor"
		sino 
			Escribir "Sueldo 3 es el mayor"
		FinSi
	SiNo
		si sueldo2 > sueldo3 Entonces
			Escribir "Sueldo 2 es el mayor"	
		SiNo
			Escribir "Sueldo 3 es el mayor"
		FinSi
	FinSi

	
	
	
FinAlgoritmo
