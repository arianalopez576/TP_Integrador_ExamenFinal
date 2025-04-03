
from datos.parametros_de_simulacion import Parametros_de_Simulacion
ps = Parametros_de_Simulacion

class Gestor_de_Alimento:
    
    def __init__(self, p_parametros):
        self.__matriz_alimento = [[0 for i in range(p_parametros.dic_parametros['max_columnas'])] for j in range(p_parametros.dic_parametros['max_filas'])]
        self.__parametros = p_parametros
      
    #para la siembra
    def agregar_alimento_en_posicion(self, p_fila, p_columna):
        if self._comprobar_dimension_fila_columna(p_fila, p_columna) == True:
            if self.retornar_alimento_en_posicion(p_fila, p_columna) + self.__parametros.dic_parametros['alimento_siembra'] >= self.__parametros.dic_parametros['cant_max_alimento_celda']:
                self.__matriz_alimento[p_fila][p_columna] = self.__parametros.dic_parametros['cant_max_alimento_celda']
            else:
                self.__matriz_alimento[p_fila][p_columna] = self.retornar_alimento_en_posicion(p_fila, p_columna) + self.__parametros.dic_parametros['alimento_siembra']
        else:
            pass #si no esta en el rango del territorio, no hace nada
     
    #se utiliza en el invierno
    def vaciar_matriz_alimento(self):
        for i in range(self.__parametros.dic_parametros['max_filas']):
            for j in range(self.__parametros.dic_parametros['max_columnas']):
                self.__matriz_alimento[i][j] = 0
    
    #se utiliza cuando el MO come
    def quitar_alimento_en_posicion (self, p_fila, p_columna, p_alimento_quitar):
            alimento_quitado = 0
            if self._comprobar_dimension_fila_columna(p_fila, p_columna) == True: 
                alimento_en_posicion = self.retornar_alimento_en_posicion(p_fila, p_columna)
                #si hay alimento en esa posicion
                if alimento_en_posicion > 0:
                    #si la cantidad de alimento es mayor a la que puede ingerir el MO, entonces se resta
                    if alimento_en_posicion >= self.__parametros.dic_parametros['cant_max_alimento_ingerir']:
                        self.__matriz_alimento[p_fila][p_columna] = self.__matriz_alimento[p_fila][p_columna] - p_alimento_quitar
                        alimento_quitado = p_alimento_quitar
                    #si la cant alimento es menor a la que puede ingerir el MO, se quita toda la comida restante
                    else:
                        alimento_quitado = self.retornar_alimento_en_posicion(p_fila, p_columna)
                        self.__matriz_alimento[p_fila][p_columna] = 0
            else:
                pass
            return alimento_quitado
            
                    
    #devuelve la cantidad de alimento en una posicion dada        
    def retornar_alimento_en_posicion(self, p_fila, p_columna):
        posicion_en_rango = self._comprobar_dimension_fila_columna(p_fila, p_columna)
        if posicion_en_rango == True:
            cant_alimento = int(self.__matriz_alimento[p_fila][p_columna])
            return cant_alimento
        else:
            return 0
        
    #para asegurarse que la comida que se quiere agregar/quitar esta en el rango del territorio
    def _comprobar_dimension_fila_columna(self, p_fila, p_columna):
        if ((p_fila >= 0) and (p_fila < self.__parametros.dic_parametros['max_filas']) and (p_columna >= 0) and (p_columna < self.__parametros.dic_parametros['max_columnas'])):
            return True 
        else:
            return False

    #devuelve datos del alimento en cada posicion
    def retornar_posicion_y_cantidad_alimento(self):
        posiciones_y_cantidad_alimento = []
        for i in range(self.__parametros.dic_parametros['max_filas']):
             for j in range(self.__parametros.dic_parametros['max_columnas']):
                 fila = i
                 columna = j
                 cant_alimento = self.retornar_alimento_en_posicion(i, j)
                 if cant_alimento > 0:
                     posiciones_y_cantidad_alimento.append((fila, columna, cant_alimento))
        return posiciones_y_cantidad_alimento #devuelve una lista de tuplas
    
    def set_parametros(self, p_nuevos):
        self.__parametros = p_nuevos
 
if __name__=="__main__":
    ga = Gestor_de_Alimento(ps)
    ga.agregar_alimento_en_posicion(1, 1)
    print(ga.retornar_alimento_en_posicion(1,1))
    ga.quitar_alimento_en_posicion(1, 1, 5)
    print(ga.retornar_alimento_en_posicion(1,1))
    