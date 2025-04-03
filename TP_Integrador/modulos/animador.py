import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import numpy as np


class Animador:
    
    def __init__(self, cant_filas, cant_columnas, p_func_ani, p_interval=50):
        
        self._fig = None
        self._ax = None
        self._scatter = None
        self._animation = None
        self._func_ani = p_func_ani
        self._interval = p_interval
        
        self._fig = plt.figure(figsize=(6, 4), facecolor="white", dpi=100)
        self._ax = self._fig.add_axes([0, 0, 1, 1], frameon=False)
        self._scatter = self._ax.scatter([], [], s=50, linewidth=0.5, edgecolors=[], facecolors=[]) 
       
        #limites de los ejes
        self._ax.set_xlim(0, cant_filas)
        self._ax.set_xticks([])
        self._ax.set_ylim(0, cant_columnas)
        self._ax.set_yticks([])
        
    def animar(self):   
        self._animation = animation.FuncAnimation(self._fig, self._func_ani, fargs=(self._scatter,), interval = self._interval)
        plt.show(block = False) 
    
        
    def pausar(self):
        if self._animation is not None:
            self._animation.pause()
        else:
            print("Error, la animacion no comenzo")
        
    def continuar(self):
        if self._animation is not None:
            self._animation.resume()
        else:
            print('Error, la animacion no comenzo')
            
    def actualizar_dimensiones_animacion(self, cant_filas, cant_columnas):
        self._ax.set_xlim(0,cant_filas)
        self._ax.set_ylim(0,cant_columnas)
    
    def existe_animacion(self):
        return self._animation is not None