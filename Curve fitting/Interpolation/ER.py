# -*- coding: utf-8 -*-
import Boussinesq as bq #importa la funcion de la respuesta a la ecuación de Boussinesq


def er(arr):       #Función recursiva
    if len(arr)==1:             #Se establece el caso inicial
        r= bq.bou(arr)
    else:                       #Se establece el caso inductivo
        r= (er(arr[0:-1])-er(arr[1:]))/(arr[0]-arr[-1])
    return r            #Retorna el valor calculado con la función recursiva
    