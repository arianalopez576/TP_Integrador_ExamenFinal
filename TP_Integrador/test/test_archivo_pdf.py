
from modulos.archivo_pdf import Archivo_PDF
from datos.parametros_de_simulacion import Parametros_de_Simulacion
import unittest
import os


class Test_Archivo_PDF(unittest.TestCase):
    
    def setUp(self):
        self.__archivo_pdf = Archivo_PDF()
        self.__nombre_archivo = 'archivo_prueba'
        self.__ps = Parametros_de_Simulacion()
        self.__datos = [1, [0, 5, 4, 2, 0, 0, 0], 0.65, 0.9]
        print ('\nsetUp')
      
    #verifica que el archivo se crea con la extension html
    def test_verificar_extension_pdf(self):
        self.__archivo_pdf.escribir_archivo(self.__nombre_archivo, self.__ps, self.__datos)
        #ospathexists verifica que el archivo este en la ruta 
        self.assertTrue(os.path.exists(self.__nombre_archivo + ".pdf"))
    
    #verifica que el archivo no este vacio
    def test_contenido_archivo(self):
        self.__archivo_pdf.escribir_archivo(self.__nombre_archivo, self.__ps, self.__datos)
        self.assertGreater(os.path.getsize(self.__nombre_archivo + ".pdf"), 0)
        

if __name__ == '__main__':
    unittest.main()
    