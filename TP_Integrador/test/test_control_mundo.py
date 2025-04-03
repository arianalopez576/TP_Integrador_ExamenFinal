from modulos.control_del_mundo import Mundo
import unittest

class Test_Archivo_Html(unittest.TestCase):
    
    def setUp(self):
        self.__mundo = Mundo()
        print ('\nsetUp')
    
    #verifica que se sume una epoca por cada vivir del mundo
    def test_aumentar_epoca(self):
        epoca1 = self.__mundo.retornar_epoca()
        self.__mundo.vivir()
        epoca2 = self.__mundo.retornar_epoca()
        
        self.assertEqual(epoca1+1, epoca2)
        
    def test_reproducir_MO(self):
        epoca_reproduccion = self.__mundo.get_parametros_simulacion().get_parametro('epoca_rep')
        for _ in range(epoca_reproduccion):  
            self.__mundo.vivir()
            
        self.assertGreaterEqual(self.__mundo.retornar_cantidad_MOs(), 2) #a > b

if __name__ == '__main__':
    unittest.main()
    