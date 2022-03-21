Algoritmo EjercicioTriangulo
	// crear las variables
	Definir angulo1 Como Entero
	Definir angulo2 Como Entero
	Definir angulo3 Como Entero
	Definir total Como Entero
	// solicitar los datos al usuario
	Escribir "Ingrese el primer angulo:"
	Leer angulo1
	Escribir "Ingrese el segundo angulo:"
	Leer angulo2	
	Escribir "Ingrese el tercero angulo:"
	Leer angulo3	
	
	total = angulo1 + angulo2 + angulo3
	si total <> 180 Entonces //< >
		Escribir "Los angulos no corresponden"
	SiNo
		si angulo1 = angulo2 y angulo1 = angulo3 Entonces
			Escribir "Es un triangulo equilatero"
		sino
			si angulo1 = angulo2 o angulo1 = angulo3 o angulo2 = angulo3 Entonces
				Escribir "Es un triangulo isoceles"
			FinSi
		FinSi
	FinSi
	// tarea realizar el escaleno y rectangulo
	
	
FinAlgoritmo
