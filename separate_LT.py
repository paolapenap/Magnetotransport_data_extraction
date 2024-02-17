#PROGRAMA PARA SEPARAR DATOS DE RESISTIVIDAD EM FUNCION DE CAMPO PARA DIFERENTES TEMPERATURAS

import numpy as np#para poder hacer arreglos de numeros
from numpy import *
import matplotlib.pyplot as plt # para hacer graficos
from pylab import *
from matplotlib import rc, rcParams
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})


p=open('x_0_rh_200k.dat','r').readlines()# esta linea abre el archivo en formato .txt o .dat y lo importa como string, el comando 'r' es para especificar abrir en modo lectura. readlines() es para leer el archivo linea por linea.


# NOTAS IMPORTANTES: 
# 1. Para un archivo RxT las columnas importantes son la de temperatura (col.4) y las columnas de resistencia medida en el canal 1 (col.13)
# y resistencia en el canal 2 (col.14). Si la medida fue hecha con campo aplicado tambien es importante imprimir la columna de campo (col.5)
# 2. Para un archivo RxH las columnas importantes son el campo (col. 5) y las columnas de  resistencia en los canales 1 y 2 (col. 13 y 14 respectivamente).
# 3. En general las columnas importantes en medidas  PPMS son: Temperatura (col4), campo (col5), corriente aplicada (col7), frecuencia de la corriente AC (col8), resistencia canal 1 (col13), resistencia en canal 2 (col14), SD canal 1 (col15) e SD canal 2 (col16).


i=1
v1=zeros((3)) # crear un vector fila con 3 elementos
v2=zeros((3))

for e in p[0::]: # para cada elemento e que se encuentra en p
  if i ==1: #filas impares que son las que contienen R del canal 1
    e=e.split(',')# decir que cada elemento de cada fila esta separado del siguiente por una coma, colocar ; o el que sea el separador 
    v1=row_stack((v1,array([float(e[3]),float(e[4]),float(e[12])]))) # row_stack es un comando de numpy para apilar las filas unas encima de otras. En este caso se forma una matriz de 3 columnas formadas por las filas apiladas de las columnas 3,4 y 12 del archivo .dat
    i=0;   
  else: # filas pares que contienen R del canal 2
    e=e.split(',') 
    v2=row_stack((v2,array([float(e[3]),float(e[4]),float(e[13])])))   
    i=1


v1=v1[1::]#para contar v1 solo a partir de la fila 1 omitiendo la 0 que es la fila de zeros dada inicialmente  
v2=v2[1::]


## SEPARACION DE MEDIDAS DEL CANAL LONGITUDINAL DEL TRANSVERSAL


np.savetxt('200KL', v1, delimiter=' ', fmt='%1.8e')
np.savetxt('200KT', v2, delimiter=' ', fmt='%1.8e')



Tl=v1[:,1]
Rl=v1[:,2]

Tt=v2[:,1]
Rt=v2[:,2]

#pm=np.loadtxt("x_0_rh_80k_mod.txt")
#Tm=pm[:,0]
#Rm=pm[:,1]



plt.figure()
plt.plot(Tl, Rl, 'ro', label='Longitudinal')
plt.plot(Tt, Rt, 'bo', label='Transversal')
plt.legend(loc='best')
plt.show()
#   
#plt.figure()
#plt.plot(Tm, Rm, 'bo')
#plt.show()
