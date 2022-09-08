import re

def carga():
	archi=open("Libros.txt","a")
	continua='S'
	while continua == 'S':
		campos=["ISBN: ", "Titulo: ", "Autor: ", "Genero: ", "Precio: "]
		campoImp = 0
		linea= ''
		print('')
		print('...AGREGAR NUEVO LIBRO...')
		print('')
		ISBN=input("Ingrese ISBN: ").strip()
		titulo=input("Ingrese Titulo: ").upper().strip()
		autor=input("Ingrese Autor: ").upper().strip()
		genero=input("Ingrese Genero: ").upper().strip()
		precio=input("Ingrese Precio: ")
		generos= "DRAMA,HISTORIA,ACCION,TERROR"

		while generos.find(genero) == -1:
			print("Genero " + genero + " incorrecro, los generos disponibles son: Drama, Accion, Terror, Historia.")
			genero=input("Ingrese Genero: ").upper().strip()

		ISBNValido= False
		while ISBNValido == False:
			if re.fullmatch("^[0-9]+$", ISBN):
				ISBNValido = True
			else:
				print("ISBN: " + ISBN + " incorrecto, debe ser un numero entero.")
				ISBN=input("Ingrese ISBN: ")
		
		precioValido= False
		while precioValido == False:
			if re.fullmatch("^[+-]?([0-9]*[.])?[0-9]+$", precio):
				precioValido = True
			else:
				print("Precio: " + precio + " incorrecto, debe ser un numero.")
				precio=input("Ingrese precio: ")
		precio=round(float(precio), 2)
		precio=str(precio)
		linea = ISBN + "," + titulo + "," + autor + "," + genero + "," + precio + "\n"
		archi.write(linea)
		print('')
		print('LIBRO CARGADO:')
		print('')
		linea = linea.split(',')
		for campo in linea:
			print(campos[campoImp] + campo)
			campoImp = campoImp + 1
		campoImp = 0
		print('')
		continua=input("Desea continuar con la carga? (S/N): ").upper()
	archi.close()