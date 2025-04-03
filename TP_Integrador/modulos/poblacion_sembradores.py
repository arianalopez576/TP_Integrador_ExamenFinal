from modulos.sembrador import Sembrador 


#composicion con sembrador
#agregacion con el mundo, que le pasa parametros de simulacion
class Poblacion_Sembradores:
    
    def __init__(self, p_parametros_simulacion):
        
        self.__lista_sembradores = []
        for _ in range(p_parametros_simulacion.dic_parametros['cant_semb_inicial']):
            sembrador = Sembrador(p_parametros_simulacion)
            self.__lista_sembradores.append(sembrador)
        
        
    def devolver_lista_sem(self):
        return self.__lista_sembradores
    
    #devuelve una lista con las posiciones de todos los sembradores
    def devolver_posicion_sembradores(self):
        lista_posiciones = []
        for sembrador in self.__lista_sembradores:
            lista_posiciones.append(sembrador.devolver_posicion())
        return (lista_posiciones)
    
    def devolver_alimento(self, p_fila, p_columna):
        for sembrador in self.__lista_sembradores:
            return sembrador.devolver_cant_comida(p_fila, p_columna)     
    
    def calcular_cant_sembradores(self):
        return len(self.__lista_sembradores)

    def set_parametros(self, p_nuevos):

        for sembrador in self.__lista_sembradores:
            sembrador.set_parametros(p_nuevos)

    
   
    
# if __name__ == '__main__':
#     ga = Gestor_de_Alimento(p_s)
#     s = Sembrador()
#     s.sembrar_alimento(ga)
#     s.sembrar_alimento(ga)
#     s.sembrar_alimento(ga)
#     poblacion_semb = Poblacion_Sembradores()
#     print(poblacion_semb.devolver_posicion_sembradores())
#     print(poblacion_semb.calcular_cant_sembradores())
    
#     print('datos_comida', poblacion_semb.retornar_posicion_y_cantidad_alimento(ga))
    
    
#p_s.dic_parametros['cant_semb_inicial']