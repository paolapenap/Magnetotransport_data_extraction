#PROGRAMA PARA ENCONTRAR EL COEFICIENTE DE HALL R_H DE LOS DATOS DE RESISTIVIDAD IMPAR EN EL CANAL TRANSVERSAL

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


p95=loadtxt('9_5KT_impar')# esta linea abre el archivo en formato .txt o .dat 
p18=loadtxt('18KT_impar')
p20=loadtxt('20KT_impar')
p22=loadtxt('22KT_impar')
p40=loadtxt('40KT_impar')
p60=loadtxt('60KT_impar')
p80=loadtxt('80KT_impar')


H95=p95[:,0]
R95=p95[:,1]
H18=p18[:,0]
R18=p18[:,1]
H20=p20[:,0]
R20=p20[:,1]
H22=p22[:,0]
R22=p22[:,1]
H40=p40[:,0]
R40=p40[:,1]
H60=p60[:,0]
R60=p60[:,1]
H80=p80[:,0]
R80=p80[:,1]



s=9.63e-5 # espesura de la muestra en m


from scipy.ndimage.filters import gaussian_filter1d as gf1d  


mu_H95=H95/10000 # campo aplicado en T
rho_H95=R95*s # resistividad Hall (ohm*m)
mu_H18=H18/10000 # campo aplicado en T
rho_H18=R18*s 
mu_H20=H20/10000 # campo aplicado en T
rho_H20=R20*s 
mu_H22=H22/10000 # campo aplicado en T
rho_H22=R22*s 
mu_H40=H40/10000 # campo aplicado en T
rho_H40=R40*s  
mu_H60=H60/10000 # campo aplicado en T
rho_H60=R60*s 
mu_H80=H80/10000 # campo aplicado en T
rho_H80=R80*s 
 
 

plt.figure() # grafico de la resistividad transversal
#plt.plot(mu_H95, rho_H95, 'bo-', label='95 K')
plt.plot(mu_H18, rho_H18, 'rs-', label='18 K')
plt.plot(mu_H20, rho_H20, 'g>-', label='20 K')
plt.plot(mu_H22, rho_H22, 'y<-', label='22 K')
plt.plot(mu_H40, rho_H40, 'mp-', label='40 K')
plt.plot(mu_H60, rho_H60, 'ch-', label='60 K')
plt.plot(mu_H80, rho_H80, 'kd-', label='80 K')
#text(2.3, -1e-7, r'BaFe$_{2}$As$_2$', fontsize=20) 
text(2.3, -1e-7, r'P-3', fontsize=22)
xlabel('$\mu_0$H (T)',fontsize=25) # para colocar la leyenda del eje x en tamano 20 (fontsize=20)
ylabel(r'$\rho_{xy}$ ($\Omega\cdot m$)', fontsize=25) # para colocar la leyenda del eje y en tamano 20 (fontsize=20)
plt.legend(loc='best', numpoints=1, handlelength=1)
plt.show()

#COEFICIENTE DE HALL

R_H95=rho_H95/mu_H95 # calculo do coeficiente de Hall
R_H18=rho_H18/mu_H18
R_H20=rho_H20/mu_H20
R_H22=rho_H22/mu_H22
R_H40=rho_H40/mu_H40
R_H60=rho_H60/mu_H60
R_H80=rho_H80/mu_H80




#plt.figure()# grafico del coeficiente de Hall en funcion del campo
##plt.plot(mu_H95, R_H95, 'bo-', label='9.5 K')
#plt.plot(mu_H18, R_H18, 'rs-', label='18 K')
#plt.plot(mu_H20, R_H20, 'g>-', label='20 K')
#plt.plot(mu_H22, R_H22, 'y<-', label='22 K')
#plt.plot(mu_H40, R_H40, 'mp-', label='40 K')
#plt.plot(mu_H60, R_H60, 'ch-', label='60 K')
#plt.plot(mu_H80, R_H80, 'kd-', label='80 K')
##plt.axvline(x=0.25, color='k')
#plt.axvline(x=2, color='k')
#plt.axvline(x=4, color='k')
#plt.axvline(x=6, color='k')
#plt.axvline(x=8, color='k')
#xlabel('$\mu_0$H (T)',fontsize=20) # para colocar la leyenda del eje x en tamano 20 (fontsize=20)
#ylabel(r'R$_H$ (m$^3$/C)', fontsize=20) # para colocar la leyenda del eje y en tamano 20 (fontsize=20)
#plt.legend(loc='best')
#plt.show()
