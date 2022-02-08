# -*- coding: utf-8 -*-
import numpy as np                      #importa todas las librerias
import pylab as plt
import lagrange as lr
import newton2 as nw
import Boussinesq as bq




datos=np.linspace(0.1,30,500)

#Primera gráfica
ley=['Funcion','Newton','Lagrange']         #Crea un vector de leyenda
plt.subplot(3,1,1)              #Crea un wrapper de dos filas y una columna
plt.title('Grado 2')
plt.plot(datos,bq.bou(datos),'-')               #Grafica los datos iniciales
plt.plot(datos,nw.newton(datos,2),'-.')               #Grafica newton
plt.plot(datos,lr.lagrange(datos,2),'.')               #Grafica lagrange
plt.legend(ley)                 #Grafica el vector leyenda

plt.subplot(3,1,2)            
plt.title('Grado 4')
plt.plot(datos,bq.bou(datos),'-')               #Grafica los datos iniciales
plt.plot(datos,nw.newton(datos,4),'-.')               #Grafica newton
plt.plot(datos,lr.lagrange(datos,4),'.')               #Grafica lagrange
plt.legend(ley)                 #Grafica el vector leyenda

plt.subplot(3,1,3)         
plt.title('Grado 6')
plt.plot(datos,bq.bou(datos),'-')               #Grafica los datos iniciales
plt.plot(datos,nw.newton(datos,6),'-.')               #Grafica newton
plt.plot(datos,lr.lagrange(datos,6),'.')               #Grafica lagrange
plt.legend(ley)                 #Grafica el vector leyenda

plt.show() #muestra la gráfica