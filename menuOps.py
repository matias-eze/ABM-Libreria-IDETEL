
def menuOps():
    print('')
    print('Menu Opciones de Librería:')
    menuOps= ["1- Buscar por ISBN", "2- Buscar por Titulo", "3- Buscar por Autor", "4- Buscar por Genero", "5- Listar todo el contenido", "6- Agregar un Nuevo Libro", "0- Salida"]
    for ops in menuOps:
        print(ops)
    menu=input("ingrese una de las opciones numericas: ")
    return menu