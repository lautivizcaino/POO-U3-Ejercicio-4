from empleado import Empleado
from datetime import datetime
class Externo(Empleado):
    __tarea:str
    __fechaInicio:str
    __fechaFin:datetime
    __montoViático:float
    __costoObra:float
    __montoSeguro:float
    def __init__(self, dni, nombre, direccion, telefono,tarea,fechaInicio,fechaFin,montoViático,costoObra,montoSeguro):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea=tarea
        self.__fechaInicio=fechaInicio
        self.__fechaFin=fechaFin
        self.__montoViático=montoViático
        self.__costoObra=costoObra
        self.__montoSeguro=montoSeguro
    
    def getTarea(self):
        return self.__tarea
    def getFechaFin(self):
        return self.__fechaFin
    def getCostoObra(self):
        return self.__costoObra
    
    def getSueldo(self):
        return self.__costoObra-self.__montoViático-self.__montoSeguro
    
    def __str__(self):
        return super().__str__() + 'Tarea:%s Fecha de Inicio:%s Fecha de Finalización:%s Monto de Viático:%s Costo de Obra:%s Monto de Seguro:%s'%(self.__tarea,self.__fechaInicio,self.__fechaFin,self.__montoViático,self.__costoObra,self.__montoSeguro)