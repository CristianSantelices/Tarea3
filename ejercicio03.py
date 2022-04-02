"""Crear una función que calcule la temperatura media de un día a 
partir de la temperatura máxima y mínima. Crear un programa principal, 
que utilizando la función anterior, vaya pidiendo la temperatura máxima y 
mínima de cada día y vaya mostrando la media.
 El programa pedirá el número de días que se van a introducir."""

def temperaturamedia(temax, temin):
    return (temax + temin)/2
dias = int(input("Ingrese el numero de dias: "))
temax = int(float(input("Ingresa temperatura maxima: ")))
temin = int(float(input("Ingresa temperatura minima: ")))
print(temperaturamedia(temax, temin))