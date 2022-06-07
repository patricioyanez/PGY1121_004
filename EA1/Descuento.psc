Algoritmo Descuento
	Definir totalCompra Como Entero
	Definir totalAPagar Como Entero
	
	Escribir "Ingrese total de la compra"
	Leer totalCompra
	
	si totalCompra >= 500 Entonces
		totalAPagar = totalCompra * .7
		Escribir "El total a pagar es $",totalAPagar 
	SiNo
		si totalCompra >= 200 Entonces
			totalAPagar = totalCompra * .8
			Escribir "El total a pagar es $",totalAPagar 			
		SiNo
			si totalCompra >= 100 Entonces
				totalAPagar = totalCompra * .9
				Escribir "El total a pagar es $",totalAPagar 			
			SiNo
				Escribir "El total a pagar es $",totalCompra				
			FinSi				
		FinSi
	FinSi
	
	
FinAlgoritmo
