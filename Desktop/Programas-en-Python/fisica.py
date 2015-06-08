print "Bienvenidx a la calculadora de electrostatica y electrodinamica."
print "La calculadora te va a hacer algunas preguntas para saber como resolver el problema que te plantearon."
print "Responde con S para 'si' y N para 'no' cuando te pregunte y con el valor cuando te lo pida."

#CONSTANTE
#-------------------------
k = 9*10**9
#-------------------------

#VARIABLES DADAS POR EL USUARIO
#-----------------------
fuerza = raw_input("Te da la FUERZA: ").upper()
carga = raw_input("Te da UNA CARGA: ").upper()
cargas = raw_input("Te da DOS CARGAS: ").upper()
distancia = raw_input("Te da la distancia: ").upper()
campo = raw_input("Te da el CAMPO ELECTRICO: ").upper()
trabajo = raw_input("Te da el TRABAJO: ").upper()
angulo = raw_input("Te da el angulo: ").upper() #intentar concebir como serian los comandos integrando los angulos.
#-----------------------

#FORMULAS
#-----------------------
if cargas == "S" and distancia == "S":
	q1 = input("Valor de Q1: ")
	q2 = input("Valor de Q2: ")
	d = input("Valor de D: ")
	print "Q1 = " + str(q1) + " C"
	print "Q2 = " + str(q2) + " C"
	print "D = " + str(d) + " m"
	resolucion = raw_input("Quiere calcular la 'F'UERZA o el 'T'RABAJO: ")
	if resolucion == "F":
		print "F =" + str((k * q1 * q2) / (d **2)) + " N"
	elif resolucion == "T":
		print "T = " + str((k * q1 * q2) / d) + " J"

if fuerza == "S" and carga == "S" and distancia == "S":
	f = input("Valor de F: ")
	q1 = input ("Valor de Q1: ")
	d = input("Valor de D: ")
	print "F = " + str(f) + " N"
	print "Q1 = " + str(q1) + " C"
	print "D = " + str(d) + " m"
	print "Q2 =" + str((f * (d **2)) / (k * q1)) + " C"
	
if fuerza == "S" and cargas == "S":
	f = input("Valor de F: ")
	q1 = input("Valor de Q1: ")
	q2 = input("Valor de Q2: ")
	print "F = " + str(f) + " N"
	print "Q1 = " + str(q1) + " C"
	print "Q2 = " + str(q2) + " C"
	print "D =" + str(((k * q1 * q2)/ f)**1/2) + " m"
	#por alguna razon, da mal la distancia.
	#es la unica que no funciona como debe.

if fuerza == "S" and carga == "S":
	f = input("Valor de F: ")
	q = input("Valor de Q: ")
	print "F = " + str(f) + " N"
	print "Q = " + str(q) + " C"
	print "E = " + str(f / q) + " N/C"
	
if carga == "S" and distancia == "S":
	q = input("Valor de Q: ")
	d = input("Valor de D: ")
	print "Q = " + str(q) + " C"
	print "D = " + str(d) + " m"
	print "E = " + str((k * q) / (d **2)) + " N/C"

if campo == "S" and distancia == "S":
	e = input("Valor de E: ")
	d = input("Valor de D: ")
	print "E = " + str(e) + " N/C"
	print "D = " + str(d) + " m"
	print "Q = " + str((e * (d **2)) / k) + " C"
	#algo raro sucede
	
if campo == "S" and carga == "S": #observad
	e = input("Valor de E: ")
	q = input("Valor de Q: ")
	resolucion = raw_input("Desea calcular la 'F'UERZA o la 'D'ISTANCIA: ").upper()
	if resolucion == "F":
		print "E = " + str(e) + " N/C"
		print "Q = " + str(q) + " C"
		print "F = " + str(e * q) + " N"
	elif resolucion == "D":
		print "Q = " + str(q) + " C"
		print "E = " + str(e) + " N/C"
		print "D = " + str(((k * q) / e) **1/2) + " m"
	#como ambas ecuaciones implican la falta de F y la presencia de E y Q,
	#la maquina no sabe cual de las dos operaciones tiene que hacer, porque
	#como la k no la anotamos nunca porque ya la indicamos como variable
	#la maquina no nota la diferencia entre el calculo de la F y el de la D
	#porque ambas ecuaciones estan compuestas por los mismos elementos.
	#para resolver el problema, decidi preguntarle al usuario que queria hacer
	#con esas variables, evitando el calculo consecutivo de ambas incognitas.

if fuerza == "S" and campo == "S":
	f = input("Valor de F: ")
	e = input("Valor de E: ")
	print "F = " + str(f) + " N"
	print "E = " + str(e) + " N/C"
	print "Q = " + str(f / e) + " C"
	
if fuerza == "S" and distancia == "S":
	f = input("Valor de F: ")
	d = input("Valor de D: ")
	print "F = " + str(f) + " N"
	print "D = " + str(d) + " m"
	print "W = " + str(f * d) + "J"

if trabajo == "S" and distancia == "S":
	t = input("Valor de t: ")
	d = input("Valor de D: ")
	print "T = " + str(t) + " J"
	print "D = " + str(d) + " m"
	print "F = " + str(t / d) + " N"
	
if trabajo == "S" and fuerza == "S":
	t = input("Valor de t: ")
	f = input("Valor de F: ")
	print "T = " + str(t) + " J"
	print "F = " + str(f) + " N"
	print "D = " + str(t / f) + " m"
	
if trabajo == "S" and distancia == "S" and carga == "S"
	t = input("Valor de t: ")
	d = input("Valor de D: ")
	q = input("Valor de Q: ")
	print "T = " + str(t) + " J"
	print "D = " + str(d) + " m"
	print "Q1 = " + str(q1) + " C"
	print "Q2 = " + str((t * d) / (q * k)) + " C"

if trabajo == "S" and cargas == "S":
	q1 = input("Valor de Q1: ")
	q2 = input("Valor de Q2: ")
	t = input("Valor de t: ")
	print "Q1 = " + str(q1) + " C"
	print "Q2 = " + str(q2) + " C"
	print "T = " + str(t) + " J"
	print "D = " + str((k * q1 * q2) / t) + " m"

#tentativa con angulos.

#if angulo == "S" #and <pregunta> existe un comodin para decirle a la compu: "Mira quiero que sea cualquier combinacion posible de variables == 's' mientras aparezca entre ellas angulo"</pregunta>:
	#poner acá el if de las otras condiciones
	#poner las variables, incluido el ANGULO.
	#poner prints de las variables
	#ahora el PRINT de la INCOGNITA va a estar dividido en dos
	#print "Xx = " + str(funcion*cos angulo) + " unidad correspondiente"
	#print "Xy = " + str(fucnio*sin angulo) + " unidad correspondiente"
	#print "Xr = " + str(pitagoras e/ Xx y Xy) + " unidad correspondiente"
	#existen funciones matemáticas que contemplan las trigonometricas:
	#siempre poner "from math import (y la funcion que queramos)"
	#y se procede a escribir la funcion como se hace comunmente.
	#funciones: acos(), asin(), atan(), cos(), sin(), tan()
