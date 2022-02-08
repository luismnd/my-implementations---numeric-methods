# -*- coding: utf-8 -*-
#Importa las librerias
import pylab as plt
import numpy as np

#Función graficar
def graficar(orden,x,y,y2,ley): #La función tiene parametros de orden, x, y, y2 y leyenda
    '''Manejo de Graficas'''
    #Grafica la regresión vs el vector x
    plt.plot(x,y2,'-')
    #Actualiza el vecttor leyenda
    ley=np.append(ley,('Aproximacion %i'%orden))
    #Incluye Titulo
    plt.title('Intensidad Reflejada de Luz vs Posicion Laser')
    #Incluye Nombre en los ejes
    plt.xlabel('Posicion laser')
    #Incluye Nombre en los ejes
    plt.ylabel('Intensidad Refleja de Luz')
    return ley              #Retorna el vector leyenda para ser actualizado