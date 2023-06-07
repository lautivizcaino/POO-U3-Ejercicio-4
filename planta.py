from empleado import Empleado
class Planta(Empleado):
    __sueldo:float
    __antiguedad:int
    def __init__(self, dni, nombre, direccion, telefono,sueldo,antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldo=sueldo
        self.__antiguedad=antiguedad
    
    def getSueldo(self):
        return self.__sueldo+self.__sueldo*0.01*self.__antiguedad
    def __str__(self):
        return super().__str__() + 'Sueldo:%s Antiguedad:%s'%(self.__sueldo,self.__antiguedad)