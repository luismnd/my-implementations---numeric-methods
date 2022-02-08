# -*- coding: utf-8 -*-

import numpy as np

def bou(z):
    #razones adimensionales
    a=4.6              #dimensiones zapata
    b=14.              #dimensiones zapata
    q=1000./(a*b)              #carga
    m=a/z           #adimensional
    n=b/z           #adimensional
    #solución de la ecuación de Boussinesq
    sigma=q/(4*3.141589)*((2*m*n*(m**2+n**2+1)**0.5)/(m**2+n**2+1+(m**2)*(n**2))*(m**2+n**2+2)/(m**2+n**2+1)+np.arcsin((2*m*n*(m**2+n**2+1)**0.5)/(m**2+n**2+1+(m**2)*(n**2))))
    return sigma
