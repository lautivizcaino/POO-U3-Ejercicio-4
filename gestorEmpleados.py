import numpy as np
import csv
from datetime import datetime
from empleado import Empleado
from planta import Planta
from contratado import Contratado
from externo import Externo

class GestorEmpleados:
    __listaEmpleados:list
    __dimension:int
    __cantidad:int
    __incremento:int
    def __init__(self,dimension,incremento=1):
        self.__listaEmpleados=np.empty(dimension,dtype=Empleado)
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0

    def agregarEmpleado(self,empleado):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__cantidad
            self.__listaEmpleados.resize(self.__dimension)
        self.__listaEmpleados[self.__cantidad]=empleado
        self.__cantidad+=1

    def leerArchivo(self):
        filePlanta=open('planta.csv',encoding='utf-8')
        fileContratados=open('contratados.csv',encoding='utf-8')
        fileExternos=open('externos.csv',encoding='utf-8')

        readerPlanta=csv.reader(filePlanta,delimiter=';')
        readerContratados=csv.reader(fileContratados,delimiter=';')
        readerExternos=csv.reader(fileExternos,delimiter=';')
        
        for row in readerPlanta:
            dePlanta=Planta(row[0],row[1],row[2],row[3],float(row[4]),int(row[5]))
            self.agregarEmpleado(dePlanta)
        primeraLinea=True
        for row in readerContratados:
            if primeraLinea:
                Contratado.setValorHora(int(row[0]))
                primeraLinea=False
            else:
                unContratado=Contratado(row[0],row[1],row[2],row[3],str(row[4]),str(row[5]),int(row[6]))
                self.agregarEmpleado(unContratado)
        for row in readerExternos:
            unExterno=Externo(row[0],row[1],row[2],row[3],str(row[4]),str(row[5]),datetime.strptime(row[6],'%d/%m/%y'),float(row[7]),float(row[8]),float(row[9]))
            self.agregarEmpleado(unExterno)
        filePlanta.close()
        fileContratados.close()
        fileExternos.close()


    def registrarHoras(self):
        dni=input('Ingrese DNI del empleado: ')
        cant=int(input('Ingrese cantidad de horas trabajadas: '))
        i=0
        while i<len(self.__listaEmpleados):
            if self.__listaEmpleados[i].getDni()==dni:
                self.__listaEmpleados[i].setHoras(cant)
                print(self.__listaEmpleados[i])
                i=len(self.__listaEmpleados)
            i+=1

    def mostrarMonto(self):
        tarea=input('Ingrese la tarea a consultar: ')
        tot=0.0
        for empleado in self.__listaEmpleados:
            if isinstance(empleado,Externo):
                if empleado.getTarea()==tarea:
                    if empleado.getFechaFin()<datetime.today():
                        tot+=empleado.getCostoObra()
        print('Costo a pagar por %s:%.2f'%(tarea,tot))


    def listarAyuda(self):
        for empleado in self.__listaEmpleados:
            if empleado.getSueldo()<150000:
                print('Nombre:%s Dirección:%s DNI:%s'%(empleado.getNombre(),empleado.getDireccion(),empleado.getDni()))
    
    def calcularSueldo(self):
        for empleado in self.__listaEmpleados:
            print('Nombre:%s Teléfono:%s Sueldo:$%.2f'%(empleado.getNombre(),empleado.getTelefono(),empleado.getSueldo()))

    def __str__(self) -> str:
        s=''
        for empleado in self.__listaEmpleados:
            s+=str(empleado) + '\n'
        return s