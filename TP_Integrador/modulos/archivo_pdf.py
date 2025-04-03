

from modulos.gestor_archivo import Archivo_Informe

from reportlab.pdfgen import canvas
from textwrap import wrap

#tiene herencia con Archivo_Informe
#es una subclase
#utiliza parametros para escribir el archivo, dependencia
class Archivo_PDF(Archivo_Informe):

    def __init__(self):
        super().__init__()
        
    def _crear_archivo(self, p_archivo): 
        p_archivo.drawString(100, 750, 'Datos del programa')

    #polimorfismo, utiliza un metodo que ya esta definido en la clase madre, empleandolo de forma distinta
    def escribir_archivo(self, p_nom_archivo, p_parametros, p_datos):
        if '.pdf' not in p_nom_archivo:
            p_nom_archivo = p_nom_archivo + '.pdf'
        archivo = canvas.Canvas(p_nom_archivo)
        self._crear_archivo(archivo)  
        #crea el histograma con los datos de la inteligencia
        self.crear_histograma(p_datos[1])
        
        #agrega fecha y hora actual al archivo
        archivo.drawString(100, 720, "Fecha y hora actuales:")
        archivo.drawString(100, 700, str(self.obtener_fecha_hora()))
        
        # convierto los parametros a texto
        texto = str(p_parametros.get_parametros())
        archivo.drawString(100, 680, "Parametros de la simulacion:")
        #posicion inicial del texto de parametros
        y_position = 660
        #el ancho que ocupa es 80 caracteres por linea
        max_ancho = 80  
        lineas = wrap(texto, width=max_ancho) #la funcion wrap divide el texto
        #para cada linea, modifica el valor de y_position
        for linea in lineas:
            archivo.drawString(100, y_position, linea)
            y_position -= 20
        
        #creo una lista de tuplas con los demas datos
        archivo.setFont("Helvetica", 12)
        datos_lista= [
            ("Época:", p_datos[0]),
            ("Inteligencia:", p_datos[1]),
            ("Inteligencia promedio:", p_datos[2]),
            ("Desviación estándar:", p_datos[3])
        ]
        for nombre_datos, valor in datos_lista:
            archivo.drawString(100, y_position, nombre_datos)
            y_position -= 20  
            #convierte el valor a string y lo separa en caso de que no entre en el ancho de la pagina
            texto_valor = str(valor)
            lineas_valor = wrap(texto_valor, width = max_ancho)

            for linea in lineas_valor:
                if y_position < 50:
                    archivo.showPage()
                    y_position = 750  
                archivo.drawString(120, y_position, linea)
                y_position -= 20  
                
        #salto de pagina, para realizar el histograma en la siguiente
        archivo.showPage()
        
        archivo.drawString(100, 720, "Histograma con datos de la inteligencia de los microorganismos:")
        archivo.drawImage('grafico.png', 100, 400, width=400, height=300) 
        archivo.showPage()  
        
        archivo.save()  
        
# if __name__ == '__main__':
#     pdf = Archivo_PDF()
#     ps = Parametros_de_Simulacion()
#     p_datos = [10, [5,3,2,1,1], 2.5, 0.9]
#     pdf.escribir_archivo('archi_prueba', ps, p_datos)