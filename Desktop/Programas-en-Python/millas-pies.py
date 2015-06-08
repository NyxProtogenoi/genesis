#miles to feet

def a_pies(millas):
	pies = millas * 5280
	print "Pies: " + str(pies)
	
a_pies(millas=int(input("Cuantas millas: ")))

#horas a segundos

def a_segundos(horas):
	segundos = horas * 3600
	print "Segundos: " + str(segundos)
	
a_segundos(horas=int(input("Cuantas horas: ")))

#perimetro rectangulo

def peri_rectangulo(lado_mayor, lado_menor):
	perimetro = lado_mayor * 2 + lado_menor * 2
	print "El perimetro del ractangulo es: " + str(perimetro)

peri_rectangulo(lado_mayor=int(input("Longitud del lado mayor: ")), lado_menor=int(input("Longitud del lado menor: ")))

#area rectangulo

def area_rect(base, altura):
	area = base * altura
	print "El area del rectangulo es: " + str(area)

area_rect(base=int(input("Longitud de la base: ")),altura=int(input("Longitud de la altura: ")))

#circunferencia: perimetro del circulo

#def circunferencia(radio):
#	circunferencia = 2 * math(pi) * radio
#	print "La longitud de la circunferencia es de: " + str(circunferencia)
	
#circunferencia(radio=int(input("Radio del circulo: ")))
