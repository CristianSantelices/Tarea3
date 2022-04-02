"""Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos 
es múltiplo del otro. Crea una función EsMultiplo
 que reciba los dos números, y devuelve si el primero es múltiplo del segundo."""

def EsMultiplo():
    n1=int(input("Ingresa un numero: "))
    n2= int(input("Ingresa un numero: "))
    if n1 % n2 == 0:
        print(f"{n1} es multilpo de {n2}")
    else:
        print(f"{n1} no es multilpo de {n2}")
EsMultiplo()