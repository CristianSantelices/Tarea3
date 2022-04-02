"""Crear una función que calcule el MCD de dos 
número por el método de Euclides. El método de Euclides es el siguiente:
Se divide el número mayor entre el menor.
Si la división es exacta, el divisor es el MCD.
Si la división no es exacta, dividimos el divisor entre 
el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
Crea un programa principal que lea dos números enteros y muestre el MCD."""


def intercambiar(mayor, menor):
	aux = int()
	if mayor<menor:
		aux = mayor
		mayor = menor
		menor = aux

def calcularmcd(num1, num2):
	mcd = int()
	resto = int()
	intercambiar(num1,num2)
	resto = num1%num2
	if resto==0:
		mcd = num2
	else:
		mcd = calcularmcd(num2,resto)
	return mcd

if __name__ == '__main__':
	numero1 = int()
	numero2 = int()
	print("Numero 1: ", end="")
	numero1 = int(input())
	print("Numero 2: ", end="")
	numero2 = int(input())
	print("MCD: ",calcularmcd(numero1,numero2))


