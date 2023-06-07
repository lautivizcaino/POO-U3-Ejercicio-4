from gestorEmpleados import GestorEmpleados
from menu import Menu
def test():
    listaEmpleados=GestorEmpleados(int(input('Ingrese dimensión del arreglo: ')))
    listaEmpleados.leerArchivo()
    print(listaEmpleados)
    menu=Menu()
    menu.opciones(listaEmpleados)

if __name__=='__main__':
    test()