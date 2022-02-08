# -*- coding: utf-8 -*-
#Importa las librerias
import numpy as np
import coeficientes as cf
import pylab as plt
#Declara matriz de datos, datos seccionados, vectores x,y y vectores x,y seccionados
datos=np.loadtxt('Retina.txt')
parte1=np.loadtxt('parte1.txt')
parte2=np.loadtxt('parte2.txt')
y1=parte1[:,1]
x1=parte1[:,0]
y2=parte2[:,1]
x2=parte2[:,0]
x=datos[:,0.]
y=datos[:,1.]
#Declara el logaritmo de los vectores y
yl=np.log(y)
yl1=np.log(y1)
yl2=np.log(y2)

#Primera gráfica
ley=['Datos iniciales']         #Crea un vector de leyenda
plt.subplot(2,1,1)              #Crea un wrapper de dos filas y una columna
plt.plot(x,y,'o')               #Grafica los datos iniciales
print 'Polinomial grado 1'      
ley=cf.polinomial(1,x,y,ley)    #Ejecuta regresión de orden 1
print 'Polinomial grado 2'
ley=cf.polinomial(2,x,y,ley)    #Ejecuta regresión de orden 2
print 'Polinomial grado 3'
ley=cf.polinomial(3,x,y,ley)    #Ejecuta regresión de orden 3
plt.legend(ley)                 #Grafica el vector leyenda

#Segunda gráfica
ley=['Datos iniciales','Datos iniciales']   #Crea nuevo vector de leyenda
plt.subplot(2,1,2)                  #Selecciona el wrapper 2
plt.plot(x1,yl1,'o')                #Grafica los datos iniciales
plt.plot(x2,yl2,'o')
print 'Exponencial 1 grado 1'
ley=cf.polinomial(1,x1,yl1,ley)     #Ejecuta regresión de orden 1 de la primera parte
print 'Exponencial 1 grado 2'
ley=cf.polinomial(2,x1,yl1,ley)     #Ejecuta regresión de orden 2 de la primera parte
print 'Exponencial 1 grado 3'
ley=cf.polinomial(3,x1,yl1,ley)     #Ejecuta regresión de orden 3 de la primera parte
print 'Exponencial 2 grado 1'
ley=cf.polinomial(1,x2,yl2,ley)     #Ejecuta regresión de orden 1 de la segunda parte
print 'Exponencial 2 grado 2'
ley=cf.polinomial(2,x2,yl2,ley)     #Ejecuta regresión de orden 2 de la segunda parte
print 'Exponencial 2 grado 3'
ley=cf.polinomial(3,x2,yl2,ley)     #Ejecuta regresión de orden 3 de la segunda parte
plt.legend(ley)                     #Imprime el vector leyenda en la gráfica
plt.savefig('Regresiones.png')      #Guarda la gráfica como imagen

plt.show()                          #Muestra la gráfica

