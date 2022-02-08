# -*- coding: utf-8 -*-

import numpy as np
import ER as er

def newton(x,n):
    x_=np.linspace(0.1,30,n+1)
    s=0
    for i in range (0,n+1,1):
        m=1
        for j in range(0,i,1):
            m=m*(x-x_[j])
            r=er.er(x_[range(i,-1,-1)])
            s=s+m*r
    return s