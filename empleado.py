class Empleado:
    __dni:str
    __nombre:str
    __direccion:str
    __telefono:str
    def __init__(self,dni,nombre,direccion,telefono):
        self.__dni=dni
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
    
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono

    def __str__(self):
        return 'DNI:%s Nombre:%s Dirección:%s Teléfono:%s '%(self.__dni,self.__nombre,self.__direccion,self.__telefono)