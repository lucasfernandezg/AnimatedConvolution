# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 18:37:47 2020

@author: Lucas
"""

#CONVOLUSION
import numpy as np
import matplotlib.pyplot as plt

def ConvoA(x1,x2,t,T,quality=1):
    "Necesita tener Numpy y pyplot importado como np y plt. Las dos señales tienen que esta definidas en el mismo t."
    "Si tira ValueError: x and y must have same first dimension y la diferencia es de solo una muestra,"
    "sumar T en el vector tc para que quede t[-1]+t[-1]+T , o quitarlo :SOLUCIONADO CON EL IF."
    "Cuanto mas grande el valor de quality, menos muestras toma, por lo que es mas rapido."
    "from ConvoA import *"
    
    x1 = x1[::quality]   # Si la fs es muy alta o esta muy lento por el nivel de procesamiento
    x2 = x2[::quality]   # requerido, entonces con el parametro quality TOMO MENOS MUESTRAS.
    t = t[::quality]
    T = T*quality
    
    if 0 in t:
        tc = np.arange(t[0]+t[0],t[-1]+t[-1]+T,T) ################
    else:
        tc = np.arange(t[0]+t[0],t[-1]+t[-1],T) ################
        
    xc = T*np.convolve(x1,x2)   # Convolusion
    
    if t[0] != 0.0 :
        x1 = np.hstack([np.zeros(np.abs(int(t[0]/T))), x1])  # Agrego ceros por delante y atras
        x2 = np.hstack([np.zeros(np.abs(int(t[0]/T))), x2])  # para que tengan el mismo largo que la convo
    if t[-1] != 0.0 :
        x1 = np.hstack([x1, np.zeros(np.abs(int(t[-1]/T)))])
        x2 = np.hstack([x2, np.zeros(np.abs(int(t[-1]/T)))])
        
    x1f = x1[::-1]      # Flipeo x1 para hacerla correr en la convolusion
    x1fp = []           # Creo vector vacio que va a ir siendo x1f avanzando
                        # dentro del For.
    d = 2*np.abs(int(t[0]/T))  # Como agregue ceros por delante de x1 y x2, retardo el inicio del 
                               # ploteo de la convolucion ese mismo tiempo. 
                               

    plt.figure()
    for k in range (0,np.size(tc)+ d):
        
        plt.clf()   # Borra el grafico anterior para remplzarlo por el nuevo
        
        if k < np.size(tc):                
            x1fp[0:k] = x1f[-1-k:-1]        # x1 invertida avanzando
            plt.plot(tc[0:k],x1fp[0:k])
        else:
            plt.plot(tc,manipular(x1f,k-np.size(tc)))  # Para cuando x1 llega al fondo
            
        plt.plot(tc,x2)           # x2 estatica
        
        if k >= 2*np.abs(int(t[0]/T)):      # La convolusion avanzando
            plt.plot(tc[0:k-d],xc[0:k-d])
        
        plt.grid(),plt.title("Convolusion Animada")
        plt.pause(0.05)     #Pausa entre graficos para que no crashee
        

def manipular(x,d):        # Para cuando x1 llega al fondo
    n=np.size(x)
    x2=np.zeros(n)
    if n>=d:
        for i in range(0,n-d):
            x2[i]=x[i-d]
    return x2    
    

    
    