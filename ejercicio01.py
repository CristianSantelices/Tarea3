"""
Crea un función EscribirCentrado,
que reciba como parámetro un texto y
lo escriba centrado en pantalla 
(suponiendo una anchura de 80 columnas;
pista: deberás escribir 40 - longitud/2 espacios antes del texto). 
Además subraya el mensaje utilizando el carácter =
"""

def centrar(cad):
	print(" " * int(40 - (len(cad)/2)),cad)
	print(" " * int(40 - (len(cad)/2)),"=" * len(cad))

mensaje1 = "Un mensaje centrado"
centrar(mensaje1)
mensaje2 = "Otro mensaje"
centrar(mensaje2)

	



