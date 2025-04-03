from modulos.archivo_html import Archivo_Html
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import unittest
import os


class Test_Archivo_Html(unittest.TestCase):
    
    def setUp(self):
        self.__archivo_html = Archivo_Html()
        self.__nombre_archivo = 'archivo_prueba'
        self.__ps = Parametros_de_Simulacion()
        self.__datos = [1, [0, 5, 4, 2, 0, 0, 0], 0.65, 0.9]
        print ('\nsetUp')
      
    #verifica que el archivo se crea con la extension html
    def test_verificar_extension_html(self):
       self.__archivo_html.escribir_archivo(self.__nombre_archivo, self.__ps, self.__datos)
       #ospathexists verifica que el archivo este en la ruta 
       self.assertTrue(os.path.exists(self.__nombre_archivo + ".html"))
    
    #verifica que los parametros se escriben correctamente
    def test_escribir_parametros_simulacion(self):
        self.__archivo_html.escribir_archivo(self.__nombre_archivo, self.__ps, self.__datos)

        with open(self.__nombre_archivo + ".html", "r") as archivo:
            contenido = archivo.read()
        
        #se convierten los parametros a str para la comparacion
        parametros = str(self.__ps.get_parametros())
        self.assertIn(parametros, contenido)

if __name__ == '__main__':
    unittest.main()
    