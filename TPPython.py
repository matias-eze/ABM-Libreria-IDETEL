import os.path
import cargar
import listar
import buscar
import menuOps



def menu():
    menu = menuOps.menuOps()
    while menu != '0':
        if menu == '1':
            buscar.buscarPorISBN()
        elif menu == '2':
            buscar.buscarPorTitulo()
        elif menu == '3':
            buscar.buscarPorAutor()
        elif menu == '4':
            buscar.buscarPorGenero()
        elif menu == '5':
            listar.listo()
        elif menu == '6':
            cargar.carga()
        else:
            print('Menu incorrecto ' + menu)
        menu = menuOps.menuOps()
    print("Fin del Programa.")

if os.path.isfile("Libros.txt"):
    menu()
else:
    archi=open("Libros.txt","w")
    archi.close()
    cargar.carga()
    menu()
