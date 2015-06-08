#CONSIGNA:
#Escribir programa que me pida un ancho y alto para hacer un rectangulo
#y un caracter con el que dibujar el rectangulo. Tengo que hacer una
#FUNCION que me permita hacer eso.
#Ejemplo: ancho = 5, alto = 6, caracter = x.
#lo que me tiene que retornar la funcion:
# x x x x x
# x x x x x
# x x x x x
# x x x x x
# x x x x x
# x x x x x

#MI INTERPRETACION:
#Basicamente lo que quiero es que la funcion tome el ANCHO y en base al
#numero al que equivale me repita el CARACTER la misma cantidad de veces
#que ANCHO indica. Con eso, quiero que tome el ALTO y me repita la linea
#creada con ANCHO.

ancho = int(input("Que ancho quiere que tenga su rectangulo: "))
alto = int(input("Que alto quiere que tenga su rectangulo: "))
caracter = raw_input("Con que caracter quiere que se dibuje el rectangulo: ")

def new_beginings():
	fila = caracter*ancho
	for bla in range(0,alto):
		print fila+" "*ancho
	
new_beginings()
