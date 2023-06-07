from gestorEmpleados import GestorEmpleados
class Menu:
    __opcion:int
    def __init__(self) -> None:
        self.__opcion=5
    
    def opciones(self,listaEmpleados):
        while self.__opcion!=0:
            print('\n1 - Registrar horas\n2 - Total de tarea\n3 - Ayuda económica\n4 - Calcular Sueldo\n0 - Salir\n')
            self.__opcion=int(input('Ingrese la opción a ejecutar: '))

            if self.__opcion==1:
                print('OPCION 1')
                listaEmpleados.registrarHoras()
            
            if self.__opcion==2:
                print('OPCION 2')
                listaEmpleados.mostrarMonto()

            if self.__opcion==3:
                print('OPCION 3')
                listaEmpleados.listarAyuda()
            
            if self.__opcion==4:
                print('OPCION 4')
                listaEmpleados.calcularSueldo()
        
        else:
            print('\nHA SALIDO DEL SISTEMA')