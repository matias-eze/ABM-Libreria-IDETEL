def listo():
    archi=open("Libros.txt","r")
    print('')
    print("...LISTADO DE CONTENIDO...")
    print('')
    campos=["--ISBN--", "--Titulo--", "--Autor--", "--Genero--", "--Precio--"]
    print("{:^8}|".format(campos[0]), "|{:^35}|".format(campos[1]), "|{:^20}|".format(campos[2]), "|{:^10}|".format(campos[3]), "|{:^8}".format(campos[4]))
    print("")
    lineas=[]
    for linea in archi:
        if len(linea) > 1:
            nuevaLinea=linea.split(',')
            lineas.append(nuevaLinea)

    for linea in lineas:
        print("{:^8}|".format(linea[0]), "|{:^35}|".format(linea[1]), "|{:^20}|".format(linea[2]), "|{:^10}|".format(linea[3]), "|{:>8}".format(linea[4]))
    print("...FIN DE ARCHIVO...")
    archi.close()
