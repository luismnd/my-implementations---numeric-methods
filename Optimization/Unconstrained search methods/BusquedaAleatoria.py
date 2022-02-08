# -*- coding: utf-8 -*-
#--------Importación librerias y funciones---------------------------
import numpy as np              #Importa la librería numpu como np
import Funciones as fn          #Importa el archivo de funciones como fn
#--------Método------------------------------------------------------
#-------Variables iniciales-----------------------------------------    
x0=np.random.uniform(0.,1.)     #Inicializa el valor de x0 como número random entre 0 y 1
y0=np.random.uniform(0.,1.)     #Inicializa el valor de y0 como número random entre 0 y 1
e=1                             #Inicializa el error en 1
tol=0.1                         #Inicializa el valor de la tolerancia
i=0                             #Inicializa el número de iteraciones
#--------Operación del método-----------------------------------------
print '-----------Busqueda Aleatoria--------------' 
print '-----------iteracion', 'X', 'Y', 'error', 'f(x,y)--------------'  #Imprime los titulos de las variables a mostrar
while e>tol:                                #Condicional mientras el valor de la tolerancia sea mayor al error
    x=np.random.uniform(0.,1.)              #Establece el valor de x como un número random entre 0 y 1
    y=np.random.uniform(0.,1.)              #Establece el valor de y como un número random entre 0 y 1
    a=fn.func(x0,y0)                        #Calcula la variable a como la evaluación de la función en (x0,y0)
    b=fn.func(x,y)                          #Calcula la variable a como la evaluación de la función en (x,y)
    e=np.abs(fn.nabla(x,y))                 #Calcula el error como el valor absoluto de la función nabla que es el la norma del vector gradiente
    i=i+1                                   #Avanza en el contador de iteraciones
    
    if e<tol and b<a:                       #Condicional para imprimir los valores de la última iteración cuando el método termina y b<a         
        print i,x,y,e,fn.func(x,y)
    
    if b>a:                                 #Condicional para imprimir los valores de la última iteración en el ciclo               
        x0=x                                #Actualiza el valor de x0
        y0=y                                #Actualiza el valor de y0
        print i,x,y,e,fn.func(x,y)          #Impresion de la iteración