"""Queremos crear un programa que trabaje con fracciones a/b.
Para representar una fracción vamos a utilizar dos enteros: numerador y denominador.
Vamos a crear las siguientes funciones para trabajar con funciones:
Leer_fracción: La tarea de esta función es leer por teclado el numerador y el denominador.
Cuando leas una fracción debes simplificarla.
Escribir_fracción: Esta función escribe en pantalla la fracción.
Si el dominador es 1, se muestra sólo el numerador.
Calcular_mcd: Esta función recibe dos número y devuelve el máximo común divisor.
Simplificar_fracción: Esta función simplifica la fracción, para ello hay que dividir numerador y
dominador por el MCD del numerador y denominador.
Sumar_fracciones: Función que recibe dos funciones n1/d1 y n2/d2,
y calcula la suma de las dos fracciones.
La suma de dos fracciones es otra fracción cuyo numerador=n1*d2+d1*n2 y denominador=d1*d2.
Se debe simplificar la fracción resultado.
Restar_fracciones: Función que resta dos fracciones: numerador=n1*d2-d1*n2 y denominador=d1*d2.
Se debe simplificar la fracción resultado.
Multiplicar_fracciones: Función que recibe dos fracciones
y calcula el producto, para ello numerador=n1*n2 y denominador=d1*d2.
Se debe simplificar la fracción resultado.
Dividir_fracciones: Función que recibe dos fracciones y calcula el cociente,
para ello numerador=n1*d2 y denominador=d1*n2. Se debe simplificar la fracción resultado."""

def Intercambiar(mayor,menor):
	if mayor<menor:
		return menor,mayor
	else:
		return mayor,menor

def CalcularMCD(num1,num2):
	num1, num2 = Intercambiar(num1,num2)
	resto = num1 % num2
	if resto == 0:
		return num2
	else:
		return CalcularMCD(num2,resto)
def LeerFraccion():
	num = int(input("Numerador:"))
	den = int(input("Denominador:"))
	num,den = SimplificarFraccion(num,den)
	return num,den
def SimplificarFraccion(num,den):
	mcd = CalcularMCD(num,den)
	num = num / mcd
	den = den / mcd
	return num,den
def EscribirFraccion(num,den):
	if den!= 1:
		print(num)
		print("---")
		print(den)
	else:
		print("")
		print(num)
		print("")
def SumarFracciones(n1,d1,n2,d2):
	nr = n1*d2 + d1*n2
	dr = d1 * d2
	nr,dr = SimplificarFraccion(nr,dr)
	return nr,dr
def RestarFracciones(n1,d1,n2,d2):
	nr = n1*d2 - d1*n2
	dr = d1 * d2
	nr,dr = SimplificarFraccion(nr,dr)
	return nr,dr
def MultiplicarFracciones(n1,d1,n2,d2):
	nr = n1 * n2
	dr = d1 * d2
	nr,dr = SimplificarFraccion(nr,dr)
	return nr,dr
def DividirFracciones(n1,d1,n2,d2):
	nr = n1 * d2
	dr = d1 * n2
	nr,dr = SimplificarFraccion(nr,dr)
	return nr,dr

while True:
	print("1.- Sumar dos fracciones")
	print("2.- Restar dos fracciones")
	print("3.- Multiplicar dos fracciones")
	print("4.- Dividir dos fracciones")
	print("5.- Salir")
	opcion = int(input())
	if opcion>=1 and opcion <=4:
		print("Fracción 1:")
		num1,den1= LeerFraccion()
		print("Fracción 2:")
		num2,den2= LeerFraccion()
	if opcion == 1:
		print("Sumar fracciones")
		numr,denr = SumarFracciones(num1,den1,num2,den2)
		EscribirFraccion(numr,denr)
	elif opcion == 2:
		print("Restar fracciones")
		numr,denr = RestarFracciones(num1,den1,num2,den2)
		EscribirFraccion(numr,denr)
	elif opcion == 3:
		print("Multiplicar fracciones")
		numr,denr = MultiplicarFracciones(num1,den1,num2,den2)
		EscribirFraccion(numr,denr)
	elif opcion == 4:
		print("Dicidir fracciones")
		numr,denr = DividirFracciones(num1,den1,num2,den2)
		EscribirFraccion(numr,denr)
	elif opcion == 5:
		break
	else:
		print("Opción incorrecta")
	

