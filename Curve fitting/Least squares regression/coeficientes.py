# -*- coding: utf-8 -*-
#Importa librerias
import numpy as np
import graficar as gr

#Función que resuleve la regresión polinomial dado el grado deseado
def polinomial(orden,x,y,ley):

    m=orden+1           
    n=len(x)
    z=np.zeros((n,m))       #Se necesita una matriz Z nxm, se inicializa
    y2=np.zeros((n))        #Se inicializa el vector respuesta
    
    for i in range(0,n,1):      #Ciclos para llenar matriz Z, avanza en filas
        for j in range(0,m,1):  #Avanza en columnas
            z[i,j]=x[i]**j          #Llena la matriz 
            
            
    zt=z.transpose()            #Transpone la matriz Z
    mult=np.dot(zt,z)                       #Multiplica Z transpuesta por Z
    a=np.linalg.solve(mult,np.dot(zt,y))    #Resuelve el sistema lineal
    print 'a',orden,'=',a               #Imprime el vector a, vector de coeficientes
    
    sumc=0                      
    sump=0
    for i in range(0,n,1):          #Ciclos para cálculo de R2
        sum=0
        for j in range(0,m,1):          
            sum=sum+a[j]*x[i]**j        #Compila la sumatoria que se utiliza en la ecuación
        y2[i]=sum
        sumc=sumc+(y[i]-sum)**2         #Sumatoria de error aproximación
        sump=sump+(y[i]-y.mean())**2    #sumatoria de error y promedio
    print 'R^2=', (sump-sumc)/sump      #Imprime el R2
    
    ley=gr.graficar(orden,x,y,y2,ley)   #Grafica la regresión
    return ley                  #Retorna el vector de leyenda
