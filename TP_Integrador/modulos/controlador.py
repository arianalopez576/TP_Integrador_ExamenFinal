from modulos.modelo import InterfazModeloSimulacion
from modulos.animador import Animador
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use('TkAgg')


class ControladorDeSimulador:
    
    def __init__(self,mundo):
        self.__interfaz = InterfazModeloSimulacion()
        self.__mundo = mundo
        parametros = mundo.get_parametros_simulacion()
        filas, columnas = parametros.get_parametro('max_filas'), parametros.get_parametro('max_columnas')
        self.__animador = Animador(filas,columnas,p_func_ani = self._actualizar)
    
    def set_mundo(self, mundo):
        self.__mundo = mundo
        
    def fijar_parametros_simulacion(self):
        self.__interfaz.cargar_parametros_simulacion()
    
    def _actualizar(self, frame, p_scatter):

        

        self.__interfaz.simular_un_paso(self.__mundo)
        
        S = self.__interfaz.devolver_datos_semb()
        
        M = self.__interfaz.devolver_datos_MOs()
        
        A = self.__interfaz.devolver_datos_alimento()
        
        posiciones = np.concatenate ([S["position"], M["position"], A["position"]])
        colores = np.concatenate([S["color"], M["color"], A["color"]])
        
        p_scatter.set_facecolors(colores)
        p_scatter.set_offsets(posiciones)

        
    
        return (p_scatter,)

    def simular_y_graficar(self, mundo):
        self.__interfaz.cargar_parametros_simulacion(mundo)
        if not self.__animador.existe_animacion():
            self.__animador.animar()
        
    
    def pausar_simulacion(self):
        self.__animador.pausar()
    
    def continuar_simulacion(self):
        self.__animador.continuar()
    
        
if __name__ == "__main__":
    cs = ControladorDeSimulador()
    cs.simular_y_graficar()
    