print "Vamos a calcular BASKARA."
print "Te voy a pedir una serie de numeros, y en base a ellos voy a calcular el valor de X1 y de X2."

a = input("Valor de 'a': ")
b = input("Valor de 'b': ")
c = input("Valor de 'c': ")

if (b **2) - 4 * a * c >= 0:
	x1 = (-b + (b **2 - 4 * a * c) **1/2) / 2 * a
	x2 = (-b - (b **2 - 4 * a * c) **1/2) / 2 * a
	print "X1 = " + str(x1)
	print "X2 = " + str(x2)
else:
	print "X1 y X2 no se pueden calcular porque el determinante es negativo."
