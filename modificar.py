import re

def modificar(ISBNTITULO):
    archi=open("Libros.txt","r")
    docu= []
    nuevoLibro = []
    campos=["ISBN", "Titulo", "Autor", "Genero", "Precio"]
    campoImp=0
    ISBNTITULO = str(ISBNTITULO)
    for linea in archi:
        docu.append(linea)
    for libro in docu:
        if len(libro) > 1:
            libro = libro.split(',')
            if (ISBNTITULO == libro[0]) or (ISBNTITULO == libro[1]):
                print('')
                print("...MODIFICANDO: " + ISBNTITULO + "...")
                for i in range(len(libro)):
                    print('')
                    print("El " + campos[campoImp] + " actual es: " + libro[i])
                    print('')
                    nuevoCampo = input("ingrese nuevo " + campos[campoImp] + " o N para continuar: ").upper().strip()
                    campoImp = campoImp+1
                    if nuevoCampo != 'N':
                        if i == 0:
                            ISBNValido= False
                            while ISBNValido == False:
                                if re.fullmatch("^[0-9]+$", nuevoCampo):
                                    ISBNValido = True
                                else:
                                    print("ISBN: " + nuevoCampo + " incorrecto, debe ser un numero entero.")
                                    nuevoCampo=input("Ingrese ISBN: ")
                            nuevoLibro.append(nuevoCampo)
                        elif i == 3:
                            generos= "DRAMA,HISTORIA,ACCION,TERROR"
                            while len(nuevoCampo) < 4 or generos.find(nuevoCampo) == -1:
                                print("Genero " + nuevoCampo + " incorrecro, los generos disponibles son: Drama, Accion, Terror, Historia.")
                                nuevoCampo=input("Ingrese Genero: ").upper().strip()
                            nuevoLibro.append(nuevoCampo)
                                
                        elif i == 4:
                            precioValido= False
                            while precioValido == False:
                                if re.fullmatch("^[+-]?([0-9]*[.])?[0-9]+$", nuevoCampo):
                                    precioValido = True
                                else:
                                    print("Precio: " + nuevoCampo + " incorrecto, debe ser un numero.")
                                    nuevoCampo=input("Ingrese precio: ")
                            nuevoCampo=round(float(nuevoCampo), 2)
                            nuevoCampo=str(nuevoCampo)
                            nuevoCampo=nuevoCampo+'\n'
                            print(nuevoCampo)
                            nuevoLibro.append(nuevoCampo)
                        else:
                            nuevoLibro.append(nuevoCampo)
                    elif nuevoCampo == 'N':
                        nuevoLibro.append(libro[i])
                campoImp = 0
    for libro in docu:
        if ISBNTITULO in libro:
            indice = docu.index(libro)
            docu.pop(indice)
            nuevoLibro = ','.join(nuevoLibro)
            print(nuevoLibro)
            docu.append(nuevoLibro)
            archi.close()
            archi=open("Libros.txt","w")
            for linea in docu:
                archi.write(linea)
            print('')
            print("LIBRO MODIFICADO: ")
            nuevoLibro = nuevoLibro.split(',')
            for campo in nuevoLibro:
                print(campos[campoImp] + ": " + campo)
                campoImp = campoImp + 1
            campoImp = 0
            archi.close()
    docu= []
    print("...MODIFICACION TERMINADA...")
    archi.close()
