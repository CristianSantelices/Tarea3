"""Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza dicha función en un programa principal
 que lea el radio de una circunferencia y muestre su área y perímetro."""

import math
def CalcularAreaPerimetro(radio):
	area = math.pi * radio ** 2;
	perimetro = 2 * math.pi * radio;
	return area,perimetro
radio = float(input("Introduce el radio:"))
area,perimetro = CalcularAreaPerimetro(radio)
print("Área:",area)
print("Perímetro:",perimetro)
