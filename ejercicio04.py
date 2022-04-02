"""Crea un función “ConvertirEspaciado”, 
que reciba como parámetro un texto y devuelve una cadena con un espacio 
 adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
Crea un programa principal donde se use dicha función."""

def ConvertirEspaciado(cad):
	cad_con_espacio = cad.replace(""," ")
	cad_con_espacio.strip()
	return cad_con_espacio

mensaje = input("Introduce una cadena:")
print("La cadena con espacio:",ConvertirEspaciado(mensaje))
