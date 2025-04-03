from modulos.control_del_mundo import Mundo
from modulos.archivo_json import Archivo_Json
from modulos.controlador import ControladorDeSimulador
from modulos.archivo_pdf import Archivo_PDF
from modulos.archivo_html import Archivo_Html

import os

class InterfazUsuario:
    
    def __init__(self):
        self.__archivo_parametros = Archivo_Json()
        self.__mundo = Mundo()
       
        #self.__parametros = self.__mundo.retornar_parametros_simulacion()
        self.__control_simulador = ControladorDeSimulador(self.__mundo)
        self.__informe_datos_pdf = Archivo_PDF()
        self.__informe_datos_html = Archivo_Html()
    
    def poner_funcionamiento(self):
        self.__control_simulador.simular_y_graficar(self.__mundo)
    
    def get_parametros(self):
        return self.__parametros
    
    def modificar_param(self, mundo):
        menu_anterior = True
        parametros_simulacion = mundo.get_parametros_simulacion()
        while menu_anterior == True:

            print('''
                  Ingrese el numero del parametro que desea modificar:
                  1- Número de filas del territorio
                  2- Número de columnas del territorio
                  3- Población (número de individuos) de Microorganismos
                  4- Energía inicial de cada MO
                  5- Energía máxima de cada MO
                  6- Cantidad máxima de alimento que puede ingerir un MO
                  7- Energía que consume cada MO al desplazarse
                  8- Población (número de individuos) de Sembradores
                  9- Cantidad alimento que siembra un sembrador
                  10- Épocas de reproducción
                  11- Probabilidad de mutación
                  12- Probabilidad de cambio de dirección del sembrador
                  13- Probabilidad de cambio de dirección del MO
                  14- Cantidad máxima de alimento en cada celda del territorio
                  15- Probabilidad eliminación total del alimento (invierno)
                  0- Volver al menu anterior
                  ''')
        
            op_modif = int(input())
            
            if 1<= op_modif <= 15:
                print('Opcion elegida: ',op_modif)
                print('Ingrese el nuevo valor')
                valor_modificar = int(input())
                clave_elegida = list(parametros_simulacion.get_parametros())[op_modif - 1]
                parametros_simulacion.set_parametro(clave_elegida,valor_modificar)
                print('Valor modificado:', clave_elegida, valor_modificar)
                '''
                for i, clave in enumerate(self.__parametros.keys()):
                    if i == op_modif - 1:
                        self.__parametros[clave] = valor_modificar
                        print('Valor modificado:', clave, valor_modificar)
                        break
                '''
            elif op_modif == 0:
                mundo.modificar_parametros_simulacion(parametros_simulacion)
                menu_anterior = False
                
            else:
                print('Error, ingrese la opcion nuevamente')
    
    def leer_param_archi(self):
        cwd = os.getcwd()  #Devuelve la ubicacion de carpetas
        files = os.listdir(cwd)  # Devuelve los archivos en esa ubicacion
        print("Files in %r: %s" % (cwd, files))
        print('Ingrese el nombre del archivo que desea leer')
        
        nom_archi = input()
        nuevos_datos = self.__archivo_parametros.leer_archi_json(nom_archi)
        parametros = self.__mundo.get_parametros_simulacion()
        for clave in parametros.get_parametros().keys():
            parametros.set_parametro(clave,nuevos_datos[clave])
        self.__mundo.modificar_parametros_simulacion(parametros)
    
    def pausar(self):
        en_pausa = bool()
        self.__control_simulador.pausar_simulacion()
        en_pausa = True
        return en_pausa

    
    def continuar(self):
        self.__control_simulador.continuar_simulacion()
    
    def guardar_parametros_archivo(self):
        print('Ingrese el nombre del archivo que desea crear')
        nom_archi = input()
        dic_parametros = self.__mundo.get_parametros_simulacion().get_parametros()
        self.__archivo_parametros.escribir_archi_json(nom_archi, dic_parametros)   
        
    def _retornar_datos_informe(self):
        datos = []
        # [1] epoca
        # [2] lista inteligencia
        # [3] inteligencia promedio
        # [4] desviacion estandar 
        datos.append(self.__mundo.retornar_epoca())
        datos.append(self.__mundo.retornar_lista_inteligencia_MOs())
        datos.append(self.__mundo.retornar_inteligencia_promedio())
        datos.append(self.__mundo.retornar_desviacion_estandar())
        return datos
        
    def interaccion_usuario(self):
        while(True):
            
    
            print('''
                  Elija lo que desea realizar:
                      
                      Opcion 1: Poner en funcionamento la simulacion
                      Opcion 2: Poner en pausa la simulacion
                      Opcion 3: Reanudar la simulacion
                      Opcion 4: Modificar los parametros de la simulacion
                      Opcion 5: Poner en funcionamiento el mundo con parametros del archivo
                      Opcion 6: Guardar los parametros de simulacion en un archivo JSON
                      Opcion 7: Guardar los datos de la simulacion en un archivo PDF
                      Opcion 8: Guardar los datos de la simulacion en un archivo HTML
                  
                  ''')
                  
            opcion_elegida = int(input())
            
            if opcion_elegida == 1:
                self.poner_funcionamiento()
            
            if opcion_elegida == 2:
                self.pausar()
            
            if opcion_elegida == 3:
                self.continuar()
            
            if opcion_elegida == 4:
                finalizo_modificaciones = False
                while not finalizo_modificaciones:
                    print('''
                          1- Realizar modificaciones de parametros
                          2-No realizar mas modificaciones, poner el mundo en funcionamiento''')
                    opcion = int(input())
                    if opcion == 1:
                        self.modificar_param(self.__mundo)
                    if opcion == 2:
                        finalizo_modificaciones = True
                        self.__control_simulador.set_mundo(self.__mundo)
                    if opcion not in {1,2}:
                        print('Error, ingrese nuevamente')
                #self.poner_funcionamiento()
                
                
            if opcion_elegida == 5:
                self.leer_param_archi()
                self.poner_funcionamiento()
            
            if opcion_elegida == 6:
                self.pausar()
                self.guardar_parametros_archivo()
                
            if opcion_elegida == 7:
                self.pausar()
                print('Ingrese el nombre del archivo que desea crear')
                nom_archi = input()
                self.__informe_datos_pdf.escribir_archivo(nom_archi, self.__mundo.get_parametros_simulacion(), self._retornar_datos_informe())
                
            if opcion_elegida == 8:
                self.pausar()
                print('Ingrese el nombre del archivo que desea crear')
                nom_archi = input()
                self.__informe_datos_html.escribir_archivo(nom_archi, self.__mundo.get_parametros_simulacion(), self._retornar_datos_informe())
                 
            if opcion_elegida not in {1,2,3,4,5,6,7}:
                print('Error, ingrese nuevamente')
                opcion_elegida = True

            
           
        
        