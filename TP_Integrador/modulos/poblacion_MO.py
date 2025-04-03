from modulos.microorganismo import Microorganismo
from datos.parametros_de_simulacion import Parametros_de_Simulacion

import numpy as np

p_s = Parametros_de_Simulacion()

class Poblacion_MO:     
    
    def __init__(self, parametros_simulacion):
        self.__lista_MO = []
        #se inicializa la lista de MO determinada por el parametro
        for _ in range(parametros_simulacion.dic_parametros['cant_MO_inicial']):
            MO = Microorganismo()
            self.__lista_MO.append(MO)
        self.__parametros = parametros_simulacion
        
    #funcion para agregar MO que nacen, si la funcion tiene un indice, se modifica en ese lugar de la lista
    def set_MO(self, MO, indice = None):
        if indice is None:
            self.__lista_MO.append(MO)
        else:
            self.__lista_MO[indice] = MO
      
    def get_MOs_vivos(self):
        MOs_vivos = []
        for mo in self.__lista_MO:
            if mo.verificar_vida() == True:
                MOs_vivos.append(mo)
        
        return MOs_vivos
    
    def devolver_MO(self, p_indice):
        return self.__lista_MO[p_indice]
    
    def devolver_lista_MO(self):
        return self.__lista_MO
    
    def devolver_posicion_MOs(self):
        lista_posiciones = []
        for MO in self.__lista_MO:
            lista_posiciones.append(MO.get_posicion())
        return lista_posiciones
    
    def crear_lista_energia_MOs(self):
        lista_energia = []
        for MO in self.__lista_MO:
            lista_energia.append(MO.get_energia())
        return lista_energia
    
    def crear_lista_inteligencia_MOs(self):
        lista_inteligencia = []
        for mo in self.__lista_MO:
            inteligencia = mo.devolver_inteligencia()
            lista_inteligencia.append(inteligencia)
        return lista_inteligencia
    
    def calcular_desviacion_estandar(self):
        return np.std(self.crear_lista_inteligencia_MOs())
    
    def calcular_cant_MO(self):
        MO_vivos = 0
        for MO in self.__lista_MO:
            if MO.verificar_vida() == True:
                MO_vivos += 1
        return MO_vivos
    
    #para calcular la inteligencia, tambien deberia verificar que los MO esten vivos?
    def calcular_inteligencia_promedio(self):
        inteligencia_total = 0
        for MO in self.__lista_MO:
            inteligencia_total += MO.devolver_inteligencia()
        inteligencia_prom = inteligencia_total/self.calcular_cant_MO() 
        return inteligencia_prom

    def set_parametros(self, p_nuevos):
        self.__parametros = p_nuevos
        

    
    