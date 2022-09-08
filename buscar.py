from xml.etree.ElementInclude import include
import modificar

def buscarPorISBN():
    print('')
    print("...BUSQUEDA POR ISBN...")
    print('')
    ISBN=input("ingrese ISBN a buscar: ")
    archi=open("Libros.txt","r")
    encontrado= False
    campos=["ISBN: ", "Titulo: ", "Autor: ", "Genero: ", "Precio: "]
    campoImp=0
    for linea in archi:
        libro = linea.split(',')
        if libro[0] == ISBN:
            nuevaLinea = linea.split(',')
            print('')
            print("...LIBRO ENCONTRADO...")
            print('')
            for campo in nuevaLinea:
                print(campos[campoImp] + campo)
                campoImp = campoImp + 1
            encontrado = True
            campoImp=0
            modifica=input("desea modificar este libro?(S/N)").upper()
            if modifica == 'S':
                modificar.modificar(ISBN)
    if encontrado == False:
        print(" ISBN: " + ISBN + " incorrecto o inexistente. ")
    
    archi.close()

def buscarPorTitulo():
    print('')
    print("...BUSQUEDA POR TITULO...")
    print('')
    titulo=input("ingrese titulo a buscar: ").upper().strip()
    archi=open("Libros.txt","r")
    encontrado= False
    campos=["ISBN: ", "Titulo: ", "Autor: ", "Genero: ", "Precio: "]
    campoImp=0
    for linea in archi:
        libro = linea.split(',')
        if len(libro) > 1:
            if libro[1] == titulo:
                nuevaLinea = linea.split(',')
                print('')
                print("...LIBRO ENCONTRADO...")
                print('')
                for campo in nuevaLinea:
                    print(campos[campoImp] + campo)
                    campoImp = campoImp + 1
                encontrado = True
                campoImp=0
                modifica=input("desea modificar este libro?(S/N)").upper()
                if modifica == 'S':
                    modificar.modificar(titulo)
    if encontrado == False:
        print(" Titulo: " + titulo + " incorrecto o inexistente. ")
    archi.close()

def buscarPorAutor():
    print('')
    print("...BUSQUEDA POR AUTOR...")
    print('')
    autor=input("ingrese Autor a buscar: ").upper().strip()
    archi=open("Libros.txt","r")
    encontrado= False
    lineas=[]
    for linea in archi:
        if linea.find(autor) != -1:
            nuevaLinea=linea.split(',')
            lineas.append(nuevaLinea)
            encontrado = True
    campos=["--ISBN--", "--Titulo--", "--Autor--", "--Genero--", "--Precio--"]
    print('')
    print("...AUTOR ENCONTRADO...")
    print('')
    print("{:^8}|".format(campos[0]), "|{:^35}|".format(campos[1]), "|{:^20}|".format(campos[2]), "|{:^10}|".format(campos[3]), "|{:^8}".format(campos[4]))
    print("")
    for linea in lineas:
        print("{:^8}|".format(linea[0]), "|{:^35}|".format(linea[1]), "|{:^20}|".format(linea[2]), "|{:^10}|".format(linea[3]), "|{:>8}".format(linea[4]))
    print("...FIN DE AUTOR...")
    if encontrado == False:
        print(" Autor: " + autor + " incorrecto o inexistente. ")
    archi.close()

def buscarPorGenero():
    print('')
    print("...BUSQUEDA POR GENERO...")
    print('')
    genero=input("ingrese Genero a buscar: ").upper().strip()
    archi=open("Libros.txt","r")
    encontrado= False
    lineas = []
    for linea in archi:
        if linea.find(genero) != -1:
            nuevaLinea=linea.split(',')
            lineas.append(nuevaLinea)
            encontrado = True
    campos=["--ISBN--", "--Titulo--", "--Autor--", "--Genero--", "--Precio--"]
    print('')
    print("...GENERO ENCONTRADO...")
    print('')
    print("{:^8}|".format(campos[0]), "|{:^35}|".format(campos[1]), "|{:^20}|".format(campos[2]), "|{:^10}|".format(campos[3]), "|{:^8}".format(campos[4]))
    print("")
    for linea in lineas:
        print("{:^8}|".format(linea[0]), "|{:^35}|".format(linea[1]), "|{:^20}|".format(linea[2]), "|{:^10}|".format(linea[3]), "|{:>8}".format(linea[4]))
    print("...FIN DE GENERO...")
    if encontrado == False:
        print(" Genero: " + genero + " incorrecto o inexistente. ")
    archi.close()