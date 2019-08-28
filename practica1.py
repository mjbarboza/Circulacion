# -*- coding: utf-8 -*-
"""
Practica 1 - Circulacion
grupo: Micaela; Luciano.
"""

import numpy as np
from matplotlib import pyplot as plt

#SI HAY ALGUN PROBLEMA CON LOS VALORES, ES DE ESCALA NO DE UNIDADES.

#usamos metros para calcular beta --> eps por lo tanto usamos TODO en metros.
Lx=4000000#dimenciones de la cuenca en metros
Ly=2000000
nx=200 #puntos de grilla
ny=100
beta= 10**-11 #en metros
D=2000 #metros

#arrays (y,x) !

from Cargar import cargar 
psi_temp1,vort_temp1,psiF1,vortF1,QG_diag1,QG_curlw1,X1,Y1,dx1,dy1=cargar("D:/Facultad/Materias/Circulacion/TP1/out_tmp1/",Lx,Ly,nx,ny)
psi_temp2,vort_temp2,psiF2,vortF2,QG_diag2,QG_curlw2,X2,Y2,dx2,dy2=cargar('D:/Facultad/Materias/Circulacion/TP1/out_tmp2/',Lx,Ly,nx,ny)
psi_temp3,vort_temp3,psiF3,vortF3,QG_diag3,QG_curlw3,X3,Y3,dx3,dy3=cargar('D:/Facultad/Materias/Circulacion/TP1/out_tmp3/',Lx,Ly,nx,ny)

###----------------1----------------###

#dimensionalizando 
Tau= 0.25
U= (2*np.pi*Tau)/(1025*D*(beta)*(Lx))

corriente1= psiF1*U*Lx
corriente2= psiF2*U*Lx
corriente3= psiF3*U*Lx

vort1=vortF1*(U/Lx)
vort2=vortF2*(U/Lx)
vort3=vortF3*(U/Lx)


#Energia cinetica.
plt.figure()
plt.plot(QG_diag1[:,3],label='K1')
plt.plot(QG_diag2[:,3],label="K2")
plt.plot(QG_diag3[:,3],label="K3")
plt.title("Energia Cinetica")
plt.xlabel("tiempo")
plt.ylabel("Energia cinetica")
plt.legend()
plt.savefig("energia_cin.png",dpi=200)


#Funcion corriente
escala=np.arange(-420000,60000,70000)

##...como hago para graficar y guardar con un for en phyton!!??

plt.figure()
plt.contourf(corriente1,escala)
plt.colorbar()
plt.title("Corriente K1")
plt.xlabel("corriente1")
plt.savefig("corriente1.png",dpi=200)

plt.figure()
plt.contourf(corriente2,escala)
plt.colorbar()
plt.title("Corriente K2")
plt.xlabel("corriente2")
plt.savefig("corriente2.png",dpi=200)

plt.figure()
plt.contourf(corriente3,escala)
plt.colorbar()
plt.title("Corriente K3")
plt.xlabel("corriente3")
plt.savefig("corriente3.png",dpi=200)


#transporte meridional, en Sverdrups
my1=D*Lx/(nx)*(np.diff(corriente1,n=1,axis=1))/10**6
my2=D*Lx/(nx)*(np.diff(corriente2,n=1,axis=1))/10**6
my3=D*Lx/(nx)*(np.diff(corriente3,n=1,axis=1))/10**6
#v= np.diff(corriente1,n=1,axis=-1)      #AXIS... 1 O -1 .. NO RECUERDO 


# campos de transporte meridional
escala_my=np.arange(-3200000,800000,400000) 
plt.figure()
plt.contourf(my1,escala_my) #hasta 199 porque en la derivacion diff se fue un x 
plt.title("My K1")
plt.colorbar()
plt.savefig("ej1_my1", dpi=200)
plt.show()

plt.figure()
plt.contourf(my2,escala_my) #hasta 199 porque en la derivacion diff se fue un x 
plt.title("My K2")
plt.colorbar()
plt.savefig("ej1_my2", dpi=200)
plt.show()

plt.figure()
plt.contourf(my3,escala_my) #hasta 199 porque en la derivacion diff se fue un x 
plt.title("My K3")
plt.colorbar()
plt.savefig("ej1_my3", dpi=200)
plt.show()
"""por si no funciona, agregué esto
plt.contourf(X1,Y1,corriente1)
plt.colorbar(levels)
plt.title('Funcion corriente 1')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.xticks(np.arange(0,4000000,1000000))

#plt.savefig('Campo de funcion corriente1.png')
plt.show()

plt.contourf(X2,Y2,corriente2)
plt.colorbar()
plt.title('Funcion corriente 2')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.xticks(np.arange(0,4000000,1000000))

#plt.savefig('Campo de funcion corriente2.png')
plt.show()

plt.contourf(X3,Y3,corriente3)
plt.colorbar()
plt.title('Funcion corriente 3')
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.xticks(np.arange(0,4000000,1000000))
#plt.savefig('Campo de funcion corriente3.png')
plt.show()
"""
#corte zonal en la latitud central de la cuenca-->y=50 ESTA BIEN??? my[:,50] o[[ my1[50,:] ]], si arrays de cargar.py (y,x)
plt.figure()
plt.plot(my1[50,:],label="K1")
plt.plot(my2[50,:],label="K2")
plt.plot(my3[50,:],label="K3")
plt.ylabel("My")
plt.xlabel("km")
plt.title("Transporte meridional")
plt.legend()
plt.savefig("transporte_meridional", dpi=200)
plt.show()

#lo mismo con la vorticidad
plt.figure()
plt.plot(X1[0:200]/1000,vort1[50,:], label="K1") #dividido 1000 para que de en km
plt.plot(X1[0:200]/1000,vort2[50,:], label="K2") 
plt.plot(X1[0:200]/1000,vort3[50,:], label="K3") 
plt.xlabel("Km")
plt.title("Vorticidad relativa")
plt.ylabel("vort. relativa")
plt.legend()
plt.savefig("vorticidad_relativa", dpi=200)
plt.show()
###----------------2----------------###
#my pero de la cbo
#buscado a mano... my[50,:], cambia de signo en 22°
# esto tambien funca ---> np.where(my1[50,:]==0) 
#hay q buscar donde cambia de signo, puede q no existan ceros ya q no es continuo
# EN TODOS HAY CEROS.

my_cbo1=my1[50,:] #latitud (y) primera coordenada del array numero 50 (centro de la cuenca)
my_cbo1_F=np.sum(my_cbo1[0:22])
my_cbo1_total=np.sum(my_cbo1) # esto ya estaba en sv
extension_cbo1=X1[22]

np.where(my2[50,:]==0)  #---> dos posiciones 46 y 49, viendo la matriz tiene valor 0 -algo + ese mismo algo 0, elijo 49
my_cbo2=my2[50,:]
my_cbo2_F=np.sum(my_cbo2[0:49])
my_cbo2_total=np.sum(my_cbo2) 
extension_cbo2=X2[49,]

np.where(my3[50,:]==0)  #---> varias posiciones, eijo la ultima 66 \m/
my_cbo3=my3[50,:] 
my_cbo3_F=np.sum(my_cbo3[0:66])
my_cbo3_total=np.sum(my_cbo3) 
extension_cbo3=X3[66,]

# hay q presentarlo como tablA-->guardamos en excel usando:
# import pandas
# ordenando 
# variable.to_excel()

import pandas as pd

# se crea un archivo tipo dict ( "dictionary" ~ lista en R )

ej_2= {" " : ["My borde oeste","My total","Extension cbo"],
       "K1":[round(my_cbo1_F),round(my_cbo1_total),extension_cbo1],
       "K2":[round(my_cbo2_F),round(my_cbo2_total),extension_cbo2],
       "K3":[round(my_cbo3_F),round(my_cbo2_total),extension_cbo3]}

# ahora pasado a un dataframe, los caracteres pasan a las filas y columnas
ej_2 = pd.DataFrame(data=ej_2)
ej_2.to_excel("ej_2.xls",index = False)

###----------------3----------------###
#ejercicio 3
"""adimensionalizamos rotor del viento, función de corriente y fricción """
v= np.diff(corriente2,n=1,axis=-1)
rotorviento= QG_curlw2*Tau*-1
friccion= eps3*vortF2*(beta*L)
ef=K2/(beta*(L**2))
corriente= corriente2*ef
plt.plot(vortF2[50,:],'r',label='rotor de viento')
plt.plot(QG_curlw2[50,:],'m',label='fricción')
plt.plot(v[50,:],'c',label='función corriente')
plt.legend()

plt.show()
