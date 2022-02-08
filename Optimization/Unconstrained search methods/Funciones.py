# -*- coding: utf-8 -*-
#--------Importación librerias y funciones---------------------------
import numpy as np                   #Importa la librería numpy como np
#------Definición de funciones para los métodos--------------#
def func(x,y):                                  #Función base del ejercicio
    f = 5.*x**2. -5.*x*y +2.5*y**2. -x -1.5*y   #EValuación de la función
    return f                                    #Retorna el valor de f
    
def dx(x,y):                #Función de la derivada parcial respecto a x
    dx=10.*x-5.*y-1.        #Evaluación de la función
    return dx               #retorna el valor de la evaluación
    
def dy(x,y):                #Función de la deivada parcial respecto a y
    dy=-5.*x+5.*y-1.5       #Evaluación de la función
    return dy               #Retorna el valor de la evaluación
    
def nabla(x,y):                     #Función de gradiente
    nabla=np.sqrt((dx(x,y))**2.+(dy(x,y))**2.)    #Evaluación de la función
    return nabla                    #Retorna el valor de la evaluación
    
def g(h,x,y):                           #Función g del método de gradiente
    g=func(x+h*dx(x,y),y+h*dy(x,y))     #Evaluación de la función
    return g                            #Retorna el valor de la evaluación
    