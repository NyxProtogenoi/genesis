#Triangulo

#CONSIGNA
#--------
#Definir dos funciones que reciban un parametro (ancho) que dibujen cada
#una una mitad del triangulo. Ejemplo: ancho = 4, caracter = c, se deberia
#ver asi:
#c
#cc
#ccc
#cccc
#ccc
#cc
#c

#CONCENPCIONES
#-------------
#podriamos pedir ancho, y construir arriba y abajo.
#o podriamos pedir alto, y construir para el costado.

ancho = int(input("Ancho del triangulo: "))
caracter = raw_input("Con que caracter quiere usted dibujar el triangulo: ")

def hacela_religiosamente():
	
	def parte_superior():
		global ancho
		bla = ancho
		while ancho > 0:
			ancho -= 1
			dor = bla - ancho
			original = caracter*dor
			print original
	parte_superior()
	def parte_inferior():
		global ancho
		while ancho > 0:
			ancho -= 1
			original = caracter*(ancho)
			print original
	parte_inferior()
	return

hacela_religiosamente()

#PROBLEMA:
#No me quiere ejecutar los dos juntos. Si comentas el llamado de una de
#las dos funciones, efectivamente ejecuta la otra. De lo contrario,
#como ahora que no esta comentada ninguna, solo se ejecuta la primera.
