# -*- coding: utf-8 -*-

import Boussinesq as bq
import numpy as np

def lagrange (x,n):                         #función de lagrange
    x_=np.linspace(0.1,30,n+1)
    s=0
    for i in range(0,n+1,1):                #ciclo de suma
        m=1
        for j in range (0,n+1,1):               #ciclo de multiplicacion
            if j!=i:
                m=m*(x-x_[j])/(x_[i]-x_[j])
        s=s+m*bq.bou(x_[i])
    return s                        #retorna la suma