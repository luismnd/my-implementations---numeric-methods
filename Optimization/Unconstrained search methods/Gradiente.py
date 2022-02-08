# -*- coding: utf-8 -*-
#--------Importación librerias y funciones---------------------------
import Funciones as fn          #Importa la librería numpy como np
import BusquedaDorada as bd     #Importa el archivo de busquedaDorada como bd
#-------Variables iniciales-----------------------------------------   
x0=0.                           #Inicializa x0 en 0
y0=0.                           #Inicializa y0 en 0
grad=fn.nabla(x0,y0)            #Calcula el gradiente inicial como la evaluación de la función nabla en (x0,y0)
f=fn.func(x0,y0)                #Calcula la función inicial como la evaluación de la función func en (x0,y0)
tol=10.**-5.                    #Inicializa la tolerancia
i=1                             #Inicializa el indicador de iteraciones en 1
#--------Operación del método-----------------------------------------
while grad>tol:                     #Condicional mientras gradiente sea mayor a la tolerancia
    hopt=bd.busquedaDorada(x0,y0)   #Se busca h óptimo utilizando busqueda dorada
    x0=x0+hopt*fn.dx(x0,y0)         #Actualiza x0 con el nuevo hoptimo y el x,y anterior
    y0=y0+hopt*fn.dy(x0,y0)         #Actualiza y0 con el nuevo hoptimo y el x,y anterior
    grad=fn.nabla(x0,y0)            #Recalcula el valor del gradiente con los nuevos valores
    f2=fn.func(x0,y0)               #Calcula el valor de la función evaluada en los nuevos parámetros
    e=f2-f                          #Calcula el error o diferencia en la evaluación de las funciones
    print "-----------------Iteracion Gradiente-------------------------------"
    print "-----------------Iteracion   X0   Y0    Grad    f    e-------------------------------"    
    print i,x0,y0,grad,f2,e         #Imprime los valores solicitados
    f=f2                            #Actualiza el valor de la función al nuevo valor
    i=i+1                           #Actualiza el contador de iteraciones