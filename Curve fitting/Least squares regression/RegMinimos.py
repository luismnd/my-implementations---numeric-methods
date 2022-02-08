# -*- coding: utf-8 -*-
import numpy as np
import pylab as plt

def polinomial(orden):

    datos=np.loadtxt('Retina.txt')
    x=datos[:,0.]
    y=datos[:,1.]
    yl=np.log(y)
    m=orden+1
    n=len(x)
    z=np.zeros((n,m))
    y2=np.zeros((n))
    
    for i in range(0,n,1):
        for j in range(0,m,1):
            z[i,j]=x[i]**j
            
            
    zt=z.transpose()
    mult=np.dot(zt,z)
    a=np.linalg.solve(mult,np.dot(zt,y))
    print 'a',orden,'=',a
    
    sum2=0
    for i in range(0,n,1):
        sum=0
        for j in range(0,m,1):
            sum=sum+a[j]*x[i]**j
            y2[i]=sum
        sum2=sum2+(y[i]-sum)**2
    print 'R^2=',np.sqrt(sum2/(n-(m+1)))
    
    '''Manejo de Graficas'''
    #Se crea una figura para grabarla en un archivo
   # fig=plt.figure(orden)
    #Grafica la funcion 1 aplicada a x,y vs. Y en linea continua
    plt.plot(x,y,'-.')
    #Grafica la segunda fila de la matriz B vs. la segunda columna de la matriz A, en puntos
    plt.plot(x,y2,'-')
    #Incluye leyenda
    plt.legend(['Datos','Aproximacion'])
    #Incluye Titulo
    plt.title('Intensidad Reflejada de Luz vs Posicion Laser')
    #Incluye Nombre en los ejes
    plt.xlabel('Posicion laser')
    #Incluye Nombre en los ejes
    plt.ylabel('Intensidad Refleja de Luz')
    if orden ==1:
        plt.savefig('Figura1.png')
    if orden==2:
        plt.savefig('Figura2.png')
    if orden==2:
        plt.savefig('Figura3.png')
    plt.show()
    
def exponencial(orden):

    datos=np.loadtxt('Retina.txt')
    x=datos[:,0.]
    y=datos[:,1.]
    yl=np.log(y)
    m=orden+1
    n=len(x)
    z=np.zeros((n,m))
    y2=np.zeros((n))
    
    for i in range(0,n,1):
        for j in range(0,m,1):
            z[i,j]=x[i]**j
            
            
    zt=z.transpose()
    mult=np.dot(zt,z)
    a=np.linalg.solve(mult,np.dot(zt,y))
    print 'a',orden,'=',a
    
    sum2=0
    for i in range(0,n,1):
        sum=0
        for j in range(0,m,1):
            sum=sum+a[j]*x[i]**j
            y2[i]=sum
        sum2=sum2+(y[i]-sum)**2
    print 'R^2=',np.sqrt(sum2/(n-(m+1)))
    
    '''Manejo de Graficas'''
    #Se crea una figura para grabarla en un archivo
   # fig=plt.figure(orden)
    #Grafica la funcion 1 aplicada a x,y vs. Y en linea continua
    plt.plot(x,y,'-.')
    #Grafica la segunda fila de la matriz B vs. la segunda columna de la matriz A, en puntos
    plt.plot(x,y2,'-')
    #Incluye leyenda
    plt.legend(['Datos','Aproximacion'])
    #Incluye Titulo
    plt.title('Intensidad Reflejada de Luz vs Posicion Laser')
    #Incluye Nombre en los ejes
    plt.xlabel('Posicion laser')
    #Incluye Nombre en los ejes
    plt.ylabel('Intensidad Refleja de Luz')
    if orden ==1:
        plt.savefig('Figura1.png')
    if orden==2:
        plt.savefig('Figura2.png')
    if orden==2:
        plt.savefig('Figura3.png')
    plt.show()
    
polinomial(1)
polinomial(2)
polinomial(3)
exponencial(1)
exponencial(2)
exponencial(3)
