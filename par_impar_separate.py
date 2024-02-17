#PROGRAMA PARA SEPARAR LAS PARTES PAR Y IMPAR DE LOS DATOS DE TENSION LONGITUDINAL

import numpy as np#para poder hacer arreglos de numeros
from numpy import *
import matplotlib.pyplot as plt # para hacer graficos
from pylab import *
from matplotlib import rc, rcParams
rc('text',usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern']})


p=loadtxt('200KL')# esta linea abre el archivo en formato .txt o .dat y lo importa como string, el comando 'r' es para especificar abrir en modo lectura. readlines() es para leer el archivo linea por linea.



A=1 # area de la seccion transversal en m2
l=1 # distancia entre los contactos de tension medida en el canal 2 transversal

   
### RESISTENCIA POSITIVA Y NEGATIVA EN CAMPO EN EL CANAL longitudinal

H=p[:,1]
R=p[:,2]


pos21=where(p[:,1] > 0)[0]
Hp2=take(p[:,1],pos21)
Rp2=take((A/l)*p[:,2],pos21)
fp2=np.column_stack((Hp2,Rp2)) 


pos22=where(p[:,1] < 0)[0]
Hn2=take(p[:,1],pos22)
Rn2=take((A/l)*p[:,2],pos22)
fn2=np.column_stack((Hn2,Rn2))


from scipy import interpolate
from scipy.interpolate import interp1d

Hpor2=Hp2.argsort() # Ver explicacion en las lineas de comando de la resistencia en el canal 1
Hp2=take(Hp2,Hpor2) 
Rp2=take(Rp2,Hpor2) 
#print Hp2

Hnor2=Hn2.argsort() # igual que los comandos para ordenar el vector Hn1
Hn2=take(Hn2,Hnor2)
Rn2=take(Rn2,Hnor2)
#print Hn2

s5= interp1d(Hp2, Rp2, kind='slinear') # comando para interpolacion linear de los datos Hp2 y Rp2
s6= interp1d(Hn2, Rn2, kind='slinear')


ming2=min(Hp2) # calcular el minino del vector de campos positivos.
if min(Hp2)<min(-1*Hn2) : ming2=min(-1*Hn2) # esta linea es para que el vector para el cual se va a calcular la funcion interpolada este dentro del intervalo de campos tomados experimentalmente y que posteriormente se creen dos vectores con la misma cantidad de puntos para los valores positivos y negativos del campo.


maxg2=max(Hp2) # calcular el maximo del vector Hp2
if max(-1*Hn2) < max(Hp2) : maxg2=max(-1*Hn2) # mismas razones que con el minimo. Estas lineas limitan el intervalo de la interpolacion. 

#raw_input()
#print ming2, maxg2


xnewp2 = np.linspace(ming2,maxg2,25) 
xnewn2 = np.linspace(-ming2,-maxg2,25) 
ynew5p = s5(xnewp2)
ynew6n = s6(xnewn2)

#print xnewp2
#print xnewn2
#print ynew5p
#print ynew6n

plt.figure() # este comando crea una nueva figura
plt.plot(Hp2,Rp2,'bx',xnewp2, ynew5p,'r', Hn2, Rn2, 'bx', xnewn2, ynew6n, 'g')
#plt.plot(Hp2,Rp2,'bx', Hn2, Rn2, 'bx')
plt.show()


#Hpar=(xnewp2+xnewn2)/2
#print Hpar
Rpar2=(ynew5p+ynew6n)/2 # calculo de la parte par de la resistencia
Rimpar2=(ynew5p-ynew6n)/2 # calculo de la parte impar de la resistencia

#print Rpar2
#print Rimpar2

plt.figure()
plt.plot(xnewp2, Rpar2, 'bo-') # grafica T como eje x, R1 como eje y en triangulitos de color azul (b^)
plt.legend(['Par'], loc='best')
plt.show()

plt.figure()
plt.plot(xnewp2, Rimpar2, 'ro-')
plt.legend(['Impar'], loc='best')
plt.show()

fpar=np.column_stack((xnewp2,Rpar2)) 
fimpar=np.column_stack((xnewp2,Rimpar2)) 

#np.savetxt('160kL_par', fpar, delimiter=' ', fmt='%1.8e')
#np.savetxt('160KL_impar', fimpar, delimiter=' ', fmt='%1.8e')

