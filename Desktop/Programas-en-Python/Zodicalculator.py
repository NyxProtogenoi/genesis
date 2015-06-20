#Intento de calculadora de zodiaco toma 2.

mes = raw_input("Escriba en letras el mes de su nacimiento: ").lower()
dia = input("Escriba el numero del dia de su nacimiento: ")


if mes == "enero":
	if dia>1 and dia<=21:
		signo = "Sos de capricornio."

	elif dia>21 and dia<31:
		signo = "Sos de acuario."
	print signo

if mes == "febrero":
	if dia>1 and dia<=21:
		signo = "acuario"

	elif dia>21 and dia<29:
		signo = "piscis"
	print signo

if mes == "marzo":
	if dia>1 and dia<=21:
		signo = "piscis"

	elif dia>21 and dia<31:
		signo = "aries"
	print signo

if mes == "abril":
	if dia>1 and dia<=21:
		signo = "aries"

	elif dia>21 and dia<31:
		signo = "tauro"
	print signo

if mes == "mayo":
	if dia>1 and dia<=21:
		signo = "tauro"

	elif dia>21 and dia<31:
		signo = "geminis"
	print signo

if mes == "junio":
	if dia>1 and dia<=21:
		signo = "geminis"

	elif dia>21 and dia<31:
		signo = "cancer"
	print signo

if mes == "julio":
	if dia>1 and dia<=21:
		signo = "cancer"

	elif dia>21 and dia<31:
		signo = "leo"
	print signo

if mes == "agosto":
	if dia>1 and dia<=21:
		signo = "leo"

	elif dia>21 and dia<31:
		signo = "virgo"
	print signo

if mes == "septiembre":
	if dia>1 and dia<=21:
		signo = "virgo"

	elif dia>21 and dia<31:
		signo = "libra"
	print signo

if mes == "octubre":
	if dia>1 and dia<=21:
		signo = "libra"

	elif dia>21 and dia<31:
		signo = "escorpio"
	print signo

if mes == "noviembre":
	if dia>1 and dia<=21:
		signo = "escorpio"

	elif dia>21 and dia<31:
		signo = "sagitario"
	print signo

if mes == "diciembre":
	if dia>1 and dia<=21:
		signo = "sagitario"

	elif dia>21 and dia<31:
		signo = "capricornio"
	print signo
