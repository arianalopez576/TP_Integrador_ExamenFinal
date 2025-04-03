
import json

class Archivo_Json:
    #para almacenar los parametros de simulacion o establecer nuevos valores
    
    def __init__(self):
        pass
    
    def escribir_archi_json(self, p_nom_archi, p_datos):
        #nuevo_json = open(p_nom_archi,"w")
        #json.dump('Parametros de la simulacion:', nuevo_json)
        #json.dump(p_datos, nuevo_json)
        #nuevo_json.close()

        if '.json' not in p_nom_archi:
            p_nom_archi = p_nom_archi + '.json'
        with open(p_nom_archi,'w') as archi:
            json.dump(p_datos, archi)
    
    
    def leer_archi_json(self, p_nom_archi):
        try:
            with open (p_nom_archi, 'r') as archi_json:
                datos_json = json.load(archi_json)
            if datos_json is not None:
                return datos_json
            else:
                print('El archivo esta vacio, o se no se cargo correctamente.')
                return
                #return 'Error, los datos no se cargaron correctamente'
        except FileNotFoundError:
            print('El archivo no existe, o no se encuentra.')
    
    
if __name__=="__main__":
    archi_json = Archivo_Json()
    datos = archi_json.leer_archi_json(r'C:\Users\Usuario\Desktop\ProgAvanzada\ExamenFinal_ProgAv\ExamenFinal\TP-3\pruebalectura.json')
    print(datos)