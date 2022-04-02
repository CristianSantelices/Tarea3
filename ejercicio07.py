"""Crear una subrutina llamada “Login”, que recibe 
un nombre de usuario y una contraseña
 y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
 Además recibe el número de intentos que se ha intentado hacer login y si 
 se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y
 una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo."""

def login(nombre, contrasena, intentos):
	eslogin = bool()
	if nombre=="usuario1" and contrasena=="asdasd":
		eslogin = True
	else:
		eslogin = False
		intentos = intentos+1
	return eslogin

if __name__ == '__main__':
	usuario = str()
	clave = str()
	cuantas = int()
	veces = int()
	entrar = bool()
	cuantasveces = 0
	while True:
		print("Usuario:", end="")
		usuario = input()
		print("Contrasena:", end="")
		clave = input()         
		entrar = login(usuario,clave,cuantasveces)
		if not entrar:
			print("Error. Nombre de usuario o contrasena incorrecta.")
		
		if entrar or cuantasveces==3: break
	
	if entrar:
		print("Bienvenidos al sistema")
		
	else:
		print("No ha entrado en el sistema")
