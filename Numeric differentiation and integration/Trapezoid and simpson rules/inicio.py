# -*- coding: utf-8 -*-
import numpy as np      #importa librerias
import pylab as plt

#funciones velocidad
def vl(t):      #función velocidad leopardo
    vl=t/(200*(np.sin(t**2+3*t)+1))+4
    return vl
def vc(t):      #función velocidad canguro
    vc=20/3*np.exp(-np.sin(t**3+4.5*t**2-6.75*t+1.375))-1.2
    return vc    
def vt(t):      #función velocidad tortuga
    vt=80/3*np.log(t+10)-60
    return vt

#Método trapecio
def tr(a,b,f,n):                #definicion del metodo
    x=np.linspace(a,b,n+1)      #vector de tiempo
    suma=0                      
    tr=np.zeros(n)              #inicializa el vector respuesta
    for i in range(0,n-1):      #metodo para la sumatoria
        suma=suma+f(x[i])       #actualiza la sumatoria
        tr[i+1]=(b-a)/(2*n)*(f(a)+suma+f(b))        #actualiza la respuesta       
    return tr       #retorna el valor calculado
    
#Método Simpson
def s(a,b,f,n):             #definicion del metodo
    x=np.linspace(a,b,n)    #vector de tiempo
    s=np.zeros(n)           #inicializa el vector respuesta
    sumai=0                 #inicializa suma de impares
    sumap=0                     #inicializa suma de pares
    for i in range(0,n):        #metodo para sumatoria
        if i % 2 == 0:          #condicional de pares e impares
            par=1
        else:
            par=0
        if par==1:
            sumai=sumai+f(x[i])         #actualiza la suma de pares
        else:
            sumap=sumap+f(x[i])         #actualiza la suma de impares
        s[i]=(b-a)/(3*n)*(f(a)+4*sumai+2*sumap+f(b))    #actualiza la respuesta
    return s                #retorna la respuesta

#Métodos diferenciación
def dc(a,b,f,n):                #derivada centrada
    x=np.linspace(a,b,n)        #vector tiempo
    h=(b-a)/n                   #variable h
    dc=np.zeros(n)              #inicializa vector respuesta
    for i in range(1,n-1):      #recorre a lo alrgo del tiempo
        dc[i]=(f(x[i+1])-f(x[i-1]))/(2*h)       #crea vector de respuesta
    return dc           #retorna el vector de respuesta
    
def dap(a,b,f,n):               #derivada alta precisión
    x=np.linspace(a,b,n)                #vector de tiempo
    h=(b-a)/n                   #variables h
    dc=np.zeros(n)              #inicializa respuesta
    for i in range(2,n-2):      
        dc[i]=(-f(x[i+2])+8*f(x[i+1])-8*f(x[i-1])+f(x[i-2]))/(12*h)     #actualiza el vector respuesta
    return dc               #retorna la respuesta



#.--------manejo de gráficas------------------------.#


#Gráficas de posición Trapecio
plt.subplot(3,1,1)          #wrapper
plt.title('Dist. Trapecio leopardo trapecio')     
plt.plot(np.linspace(0,5,2),tr(0.,5.,vl,2), label="n=2")
plt.plot(np.linspace(0,5,10),tr(0.,5.,vl,10), label="n=10")
plt.plot(np.linspace(0,5,100),tr(0.,5.,vl,100), label="n=100")
plt.legend()

plt.subplot(3,1,2)           #wrapper
plt.title('Dist. Trapecio canguro trapecio')
plt.plot(np.linspace(0,5,2),tr(0.,5.,vc,2), label="n=2")
plt.plot(np.linspace(0,5,10),tr(0.,5.,vc,10), label="n=10")
plt.plot(np.linspace(0,5,100),tr(0.,5.,vc,100), label="n=100")
plt.legend()

plt.subplot(3,1,3)           #wrapper
plt.title('Dist. Trapecio tortuga trapecio')
plt.plot(np.linspace(0,5,2),tr(0.,5.,vt,2), label="n=2")
plt.plot(np.linspace(0,5,10),tr(0.,5.,vt,10), label="n=10")
plt.plot(np.linspace(0,5,100),tr(0.,5.,vt,100), label="n=100")
plt.legend()
plt.show()


#Gráficas de posición Simpson
plt.subplot(3,1,1)       #wrapper
plt.title('Dist. leopardo Simpson')
plt.plot(np.linspace(0,5,2),s(0.,5.,vl,2), label="n=2")
plt.plot(np.linspace(0,5,10),s(0.,5.,vl,10), label="n=10")
plt.plot(np.linspace(0,5,100),s(0.,5.,vl,100), label="n=100")
plt.legend()

plt.subplot(3,1,2)           #wrapper
plt.title('Dist. canguro Simpson')
plt.plot(np.linspace(0,5,2),s(0.,5.,vc,2), label="n=2")
plt.plot(np.linspace(0,5,10),s(0.,5.,vc,10), label="n=10")
plt.plot(np.linspace(0,5,100),s(0.,5.,vc,100), label="n=100")
plt.legend()

plt.subplot(3,1,3)           #wrapper
plt.title('Dist. Simpson n=10')
plt.plot(np.linspace(0,5,2),s(0.,5.,vt,2), label="n=2")
plt.plot(np.linspace(0,5,10),s(0.,5.,vt,10), label="n=10")
plt.plot(np.linspace(0,5,100),s(0.,5.,vt,100), label="n=100")
plt.legend()
plt.show()



#Gráficas aceleración
plt.subplot(3,1,1)           #wrapper
plt.title("Ac. leopardo")
plt.plot(np.linspace(0,5,1000),dc(0.,5.,vl,1000),label="Centrada")
plt.plot(np.linspace(0,5,1000),dap(0.,5.,vl,1000),label="Alta P.")
plt.legend()

plt.subplot(3,1,2)           #wrapper
plt.title('Ac. canguro')            
plt.plot(np.linspace(0,5,1000),dc(0.,5.,vc,1000),label="Centrada")
plt.plot(np.linspace(0,5,1000),dap(0.,5.,vc,1000),label="Alta P.")
plt.legend()

plt.subplot(3,1,3)               #wrapper
plt.title('Ac. tortuga')
plt.plot(np.linspace(0,5,1000),dc(0.,5.,vt,1000),label="Centrada")
plt.plot(np.linspace(0,5,1000),dap(0.,5.,vt,1000),label="Alta P.")
plt.legend()
plt.show()



print 'Todos estan descalificados por usar sustancias no permitidas, el ganador de la carrera es la tortuga.'