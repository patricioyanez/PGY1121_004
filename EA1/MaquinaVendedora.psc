Algoritmo MaquinaVendedora
	// EJERCICIO:
	// Realizar la venta de 3 productos: Coca cola, Fanta y Sprite.
	// Los valores de estos son: 600, 500 y 350.
	// solicitar al usuario que producto quiere y la cantidad.
	// mostrar el total a pagar.
	
	Definir numeroOpcion Como Entero
	Definir cantidad Como Entero
	Definir totalPagar Como Entero
	
	Escribir "*****  Super Maquina Vendedora ******"
	Escribir "1.- Coca cola"
	Escribir "2.- Fanta"
	Escribir "3.- Sprite"
	Escribir "Ingrese el codigo del producto"
	Leer numeroOpcion
	Escribir "Ingrese cantidad a comprar"
	Leer cantidad
	
	si numeroOpcion = 1 Entonces
		totalPagar = cantidad * 600
	SiNo
		si numeroOpcion = 2 Entonces
			totalPagar = cantidad * 500
		SiNo
			totalPagar = cantidad * 350
		FinSi
	FinSi
	
	Escribir "El total a pagar es: $", totalPagar
		
FinAlgoritmo
