Algoritmo EjemploSuma
	Definir numero Como Entero
	Definir indice Como Entero
	Definir total Como Entero
	// inicializar variables
	total  = 0 
	indice = 1	
	Mientras indice <= 5 Hacer
		Escribir "Ingrese n�mero ", indice, ":"
		Leer numero
		
		si numero > 0 Entonces
			total  = total + numero
			indice = indice + 1
		SiNo
			Escribir "El nro ingresado no es v�lido"			
		FinSi		
	FinMientras		
	Escribir "La suma de los nros es:" total
FinAlgoritmo

