#PROGRAMA DE PRUEBA PARA TRABAJAR CON DATOS DE RESISTIVIDAD EM FUNCION DE TEMPERATURA EXTRAIDOS DE PPMS

import numpy as np#para poder hacer arreglos de numeros
from numpy import *
import matplotlib.pyplot as plt # para hacer graficos
from pylab import *
from matplotlib import rc, rcParams
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})
import matplotlib as mpl
#mpl.rcParams['axes.labelsize']= 21 # tamanho de las letras en el grafico
mpl.rcParams['legend.fontsize']= 20 # tamanho de las letras en la leyenda
#mpl.rcParams['xtick.major.size']= 8
#mpl.rcParams['xtick.minor.size']= 4
#mpl.rcParams['ytick.major.size']= 8
#mpl.rcParams['ytick.minor.size']= 4
mpl.rcParams['xtick.labelsize']=25 # tamanho los numeros en el eje x
mpl.rcParams['ytick.labelsize']= 25 # tamanho los numeros en el eje y

p=open('x_0_rt.dat','r').readlines()# esta linea abre el archivo en formato .txt o .dat y lo importa como string, el comando 'r' es para especificar abrir en modo lectura. readlines() es para leer el archivo linea por linea.


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
    v1=row_stack((v1,array([float(e[3]),float(e[4]),float(e[12])])))# row_stack es un comando de numpy para apilar las filas unas encima de otras
# en este caso se forma una matriz de 3 columnas formadas por las filas apiladas de las columnas 3,4 y 12 del archivo .dat
    i=0;   
  else: # filas pares que contienen R del canal 2
    e=e.split(',') 
    v2=row_stack((v2,array([float(e[3]),float(e[4]),float(e[13])])))   
    i=1
#      for a in v2:
#         if a > 0:
#         v21=row_stack((v21,array([float(e[3]),float(e[4]),float(e[13])])))
#         
#        v22=row_stack((v22,array([float(e[3]),float(e[4]),float(e[13])])))

v1=v1[1::]#para contar v1 solo a partir de la fila 1 omitiendo la 0 que es la fila de zeros dada inicialmente  
v2=v2[1::]

#print v1
#print v2
#print v1[0:5,1]


A=1.4397e-7 # area de la seccion transversal en m2
l1=0.61e-3 # distancia entre los contactos de tension medida en el canal 1 en m
l2=0.24e-3 # distancia entre los contactos de tension medida en el canal 2 en m

T1=v1[:,0]
T2=v2[:,0]
R1=(A/l1)*v1[:,2] # resistividad en el canal 1
R2=(A/l2)*v2[:,2] # resistividad en el canal 2

#print R1

plt.figure()
plt.plot(T1,R1, 'bo') # grafica T como eje x, R1 como eje y
#plt.plot(T2,R2/1e-6, 'go', label='Resistividade transversal')
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0)) 
plt.legend(loc='best') # para colocar una leyenda dentro del grafico en la mejor localizacion posible(loc='best')
xlabel('T (K)',fontsize=25) # para colocar la leyenda del eje x en tamano 20 (fontsize=20)
ylabel(r'$\rho$ ($\Omega\cdot$m)', fontsize=25) # para colocar la leyenda del eje y en tamano 20 (fontsize=20)
plt.annotate('$T_N\sim$ 136 K', xy=(138, 3.89e-6), xytext=(184, 3.2e-6), fontsize=20,
            arrowprops=dict(facecolor='red', shrink=0.1),
            )
text(200, 1.5e-6, r'BaFe$_{2}$As$_2$', fontsize=20)
plt.show() # para mostrar el grafico creado


gra=np.gradient(R1) # obtener la primera derivada
sgra=np.gradient(gra)

#plt.figure()
#plt.plot(T1,-gra/1e-7, 'b') # grafica T como eje x, R1 como eje y en triangulitos de color azul (b^) 
#xlabel('T (K)',fontsize=20) # para colocar la leyenda del eje x en tamano 20 (fontsize=20)
#ylabel(r'd$\rho$/dT (10$^{-7}\Omega\cdot$m)/K', fontsize=20) # para colocar la leyenda del eje y en tamano 20 (fontsize=20)
#plt.annotate('T$_N=$ 135.8 K', xy=(136.5, 2.79), xytext=(190, 1.91), fontsize=20,
#            arrowprops=dict(facecolor='red', shrink=0.1),
#            )
#plt.annotate('T$_S=$ 132.1 K', xy=(131.7, 4.17), xytext=(185.9, 3.44), fontsize=20,
#            arrowprops=dict(facecolor='red', shrink=0.1),
#            )
#text(20, 3, r'BaFe$_{2}$As$_2$', fontsize=20)
#plt.show() # para mostrar el grafico creado


# para guardar los resultados en un archivo reescribible en formato .txt: 

R=column_stack((T1, R1))
np.savetxt('RxT_Ni0', R, delimiter=' ', fmt='%1.8e')

#GRAFICO DE RESISTIVIDAD Y DERIVADA JUNTOS 
plt.figure()
ax = plt.gca()#comandos que dejan crear dos ejes 'y' diferentes
ax2 = ax.twinx()#comandos que dejan crear dos ejes 'y' diferentes
plt.axis('normal')#comandos que dejan crear dos ejes 'y' diferentes
ax.plot(T1,R1*1e6, 'bo') 
plt.arrow(100, 1, -40, 0, fc='b', ec='b', head_width=0.2, head_length=3)
plt.arrow(250, 1, 50, 0, fc='k', ec='k', head_width=0.2, head_length=3)
ax.set_xlabel('T (K)',fontsize=25)
ax.set_ylabel(r'$\rho$ (10$^{-6}$ $\Omega\cdot$m)', fontsize=25) # para colocar la leyenda del eje y en tamano 20 (fontsize=20)
#ax.text(25, 4, r'BaFe$_{2}$As$_2$', fontsize=22)
ax.text(25, 4, r'P-3', fontsize=22)
ax2.plot(T1,-gra*1e7, 'k')#, T1, sgra, 'r') # grafica T como eje x, R1 como eje y en triangulitos de color azul (b^) 
ax2.set_ylim(ymax=4.5)
ax2.annotate('T$_N=$ 136 K', xy=(136.5, 2.79), xytext=(190, 1.91), fontsize=22,
            arrowprops=dict(facecolor='red', shrink=0.1),
            )
#ax2.annotate('T$_S=$ 132.1 K', xy=(131.7, 4.17), xytext=(155.9, 3.94), fontsize=20,
#            arrowprops=dict(facecolor='red', shrink=0.1),
#            )
ax2.set_ylabel(r'd$\rho$/dT (10$^{-7}$ $\Omega\cdot$m)/K', fontsize=25, rotation=-90)
plt.show() # para mostrar el grafico creado
