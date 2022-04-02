"""Escribir dos funciones que permitan calcular:
La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
Escribe un programa principal con un menú 
donde se pueda elegir la opción de convertir a segundos,
convertir a horas,minutos y segundos o salir del programa."""

def convertir_a_segundos(h, m, s):
	seg = int()
	segmento = h*3600+m*60+s
	return seg

def convertir_a_hms(seg, h, m, s):
	h = int(seg/3600)
	segmento = segmento-h*3600
	m = int(seg/60)
	segmento = segmento-m*60
	s = seg

if __name__ == '__main__':
	hor = int()
	min = int()
	seg = int()
	segundo = int()
	opcion = int()
	while True:# no hay 'repetir' en python
		print("1.- Convertir a segundos")
		print("2.- Convertir a horas, minutos y segundos")
		print("3.- Salir")
		opcion = int(input())
		if opcion==1:
			print("Horas:", end="")
			hor = int(input())
			print("Minutos:", end="")
			min = int(input())
			print("Segundos:", end="")
			seg = int(input())
			print("Corresponde a",convertir_a_segundos(hor,min,seg),"segundos")
		elif opcion==2:
			print("Segundos:", end="")
			segundo = int(input())
			convertir_a_hms(segundo,hor,min,seg)
			print("Corresponde a",hor,":",min,":",seg)
		elif opcion==3:
		
			print("Opcion incorrecta")
		if opcion==3: break
