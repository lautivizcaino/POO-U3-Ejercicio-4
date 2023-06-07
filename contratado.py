from empleado import Empleado
class Contratado(Empleado):
    __fechaInicio:str
    __fechaFin:str
    __cantidadHoras:int
    #Atributo de clase
    __valorHora:float
    def __init__(self, dni, nombre, direccion, telefono,fechaInicio,fechaFin,horas):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fechaInicio=fechaInicio
        self.__fechaFin=fechaFin
        self.__cantidadHoras=horas
    #Métodos de clase
    @classmethod
    def setValorHora(cls,valor):
        cls.__valorHora=valor
    
    #Métodos de instancia
    def setHoras(self,cant):
        self.__cantidadHoras+=cant
    def getSueldo(self):
        return self.__cantidadHoras*self.__valorHora


    def __str__(self):
        return super().__str__() +'Fecha de Inicio:%s Fecha de Finalización:%s Cantidad de horas:%s Valor de hora:%s'%(self.__fechaInicio,self.__fechaFin,self.__cantidadHoras,self.__valorHora)
