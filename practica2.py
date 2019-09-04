# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:49:30 2019

@author: Jimena
"""

import numpy as np
from matplotlib import pyplot as plt

# SI HAY ALGUN PROBLEMA CON LOS VALORES, ES DE ESCALA NO DE UNIDADES.
# usamos metros para calcular beta, usamos TODO en metros.
#ejercicio 1
Lx = 1000000 # dimensiones de la cuenca en metros
Ly = 500000
nx = 100 # puntos de grilla
ny = 50
beta = 10**-11 # en metros
D = 2000 # metros
from Cargar import cargar 
psi_temp1,vort_temp1,psiF1,vortF1,QG_diag1,QG_curlw1,X1,Y1,dx1,dy1=cargar('C:/Users/Jimena/Desktop/FCEN/circulación/prácticas/TP2/out_tmp1/',Lx,Ly,nx,ny)
psi_temp2,vort_temp2,psiF2,vortF2,QG_diag2,QG_curlw2,X2,Y2,dx2,dy2=cargar('C:/Users/Jimena/Desktop/FCEN/circulación/prácticas/TP2/out_tmp2/',Lx,Ly,nx,ny)
psi_temp3,vort_temp3,psiF3,vortF3,QG_diag3,QG_curlw3,X3,Y3,dx3,dy3=cargar('C:/Users/Jimena/Desktop/FCEN/circulación/prácticas/TP2/out_tmp3/',Lx,Ly,nx,ny)
psi_temp4,vort_temp4,psiF4,vortF4,QG_diag4,QG_curlw4,X4,Y4,dx4,dy4=cargar('C:/Users/Jimena/Desktop/FCEN/circulación/prácticas/TP2/out_tmp4/',Lx,Ly,nx,ny)
psi_temp5,vort_temp5,psiF5,vortF5,QG_diag5,QG_curlw5,X5,Y5,dx5,dy5=cargar('C:/Users/Jimena/Desktop/FCEN/circulación/prácticas/TP2/out_tmp5/',Lx,Ly,nx,ny)

Tau = 0.25
U = (2*np.pi*Tau)/(1025*D*(beta)*(Lx))

corriente1 = psiF1*U*Lx
corriente2 = psiF2*U*Lx
corriente3 = psiF3*U*Lx
corriente4 = psiF4*U*Lx
corriente5 = psiF5*U*Lx

vort1 = vortF1*(U/Lx)
vort2 = vortF2*(U/Lx)
vort3 = vortF3*(U/Lx)
vort4 = vortF4*(U/Lx)
vort5 = vortF5*(U/Lx)

# Energia cinetica. (no la dimensionalizamos)
plt.figure()
plt.plot(QG_diag1[:,3],'r',label='K1')
plt.plot(QG_diag2[:,3],'g',label="K2")
plt.plot(QG_diag3[:,3],'b',label="K3")
plt.plot(QG_diag4[:,3],'m',label="K4")
plt.plot(QG_diag5[:,3],'c',label="K5")
plt.title("Energia Cinética")
plt.grid()
plt.xlabel("Tiempo")
plt.ylabel("Energia cinética")
plt.legend()
plt.tight_layout()
plt.savefig("energia_cin.png",dpi=200)

#ejercicio 2
# Cuantas iteraciones necesarias para alcanzar el estado estacionario

# invirtiendo la serie temporal para analizar el criterio desde atras hacia adelante
energia1 = np.flip(QG_diag1[:,3],0) 
energia2 = np.flip(QG_diag2[:,3],0)
energia3 = np.flip(QG_diag3[:,3],0)
energia4 = np.flip(QG_diag4[:,3],0)
energia5 = np.flip(QG_diag5[:,3],0)

energia = (energia1,energia2,energia3,energia4,energia5)
num = np.arange(0,5,1)
iteraciones = []
iteraciones.extend([None]*5)

for x in num:
    i = 0 
    dif_E = 0
    while dif_E < 1:
        dif_E = (np.abs((energia[x][0]-energia[x][i]))/energia[x][0])*100
        i += 1 
    iteraciones[x] = 10000 - i  # por mas que cuente desde 0, i vale uno mas que cuando se cumple la condiciones del while
    print(iteraciones[x])                           # por eso directamente 10000 - i
#pregunta si diste vuelta el vector y calculas la iteracion en la cual converge
#no deberia restarle de nuevo los 10000 para obtener la posición real
# grafico de energia cinetica
plt.figure()
plt.plot(QG_diag1[:,3],label='Ev1_1',color = "r")
plt.plot(QG_diag2[:,3],label="EV1_2",color = "orange")
plt.plot(QG_diag3[:,3],label="Ev1_3",color = "yellow")
plt.plot(QG_diag4[:,3],label="EV1_4",color = "b")
plt.plot(QG_diag5[:,3],label="EV1_5",color = "purple")
plt.title("Energia Cinetica")
plt.grid()
plt.xlabel("tiempo")
plt.ylabel("Energia cinetica")
plt.legend(loc = "lower right")
plt.axvline(x = iteraciones[0], color = "r")
plt.axvline(x = iteraciones[1], color = "orange")     #
plt.axvline(x = iteraciones[2], color = "yellow")     #ponemos esto ,lineas verticales marcando 
plt.axvline(x = iteraciones[3], color = "b")          # el tiempo donde se alcanza el estado estacionario
plt.axvline(x = iteraciones[4], color = "purple")
plt.tight_layout()
plt.savefig("energia_cin1.png",dpi=200)

#ejercicio 3

# Funcion corriente
#Lu: no es necesario escalarlo pues da todo en el mismo rango
#pide isolíneas
corrientes = (corriente1,corriente2,corriente3,corriente4,corriente5)
nombres_c = ("corriente1","corriente2","corriente3","corriente4","corriente5")
titulo_c = ("Corriente K1", "Corriente K2", "Corriente K3","Corriente K4", "Corriente K5")
num = (0,1,2,3,4)

for i in num:
    plt.figure()
    plt.contour(X1,Y1,corrientes[i],cmap='winter')
    plt.colorbar()
    plt.title(titulo_c[i])
    plt.xlabel('longitud')
    plt.ylabel('latitud')
    plt.grid()
    plt.xticks(np.arange(0,1000000,300000))
    plt.tight_layout()
    plt.savefig(nombres_c[i],dpi=200)

#isolineas del campo de vorticidad
vort_rel = (vort1,vort2,vort3,vort4,vort5)
esc_v = np.arange(-0.000007,0.000041,0.00000002)
esc_v = np.arange(-0.000012,0.000041,0.0000001) #ojo con esta escala,dan muy extraños
nombres_v = ("Vort. rel. 1","Vort. rel. 2","Vort. rel. 3","Vort. rel. 4","Vort. rel. 5")
Tit_v = ("Vort. rel. 1","Vort. rel. 2","Vort. rel. 3","Vort. rel. 4","Vort. rel. 5")
#ojo no está guardando los graficos, y la escala no está como debería
for i in num:
    plt.figure()
    plt.contour(X1,Y1,vort_rel[i],esc_v,cmap='winter') 
    plt.colorbar()
    plt.title(Tit_v[i])
    plt.xlabel('longitud')
    plt.ylabel('latitud')
    plt.grid()
    plt.xticks(np.arange(0,1000000,300000))
    plt.tight_layout()
    plt.show()
    #plt.savefig(nombres_v[i],dpi=200,format=png)
#ejercicio 4

#corte zonal en latitud central de la cuenca   
# transporte meridional, en Sverdrups
# duda estaremos en el eje que corresponde?
my1 = D*(np.diff(corriente1,n=1,axis=1))/(10**6)
my2 = D*(np.diff(corriente2,n=1,axis=1))/(10**6)
my3 = D*(np.diff(corriente3,n=1,axis=1))/(10**6)
my4 = D*(np.diff(corriente4,n=1,axis=1))/(10**6)
my5 = D*(np.diff(corriente5,n=1,axis=1))/(10**6)
# campos de transporte meridional
escala_my = np.arange(-1380,290,50) #escala para los graficos 
# --> quedan valores de -1380 a 270 Sv, es bastante pero no tanto como la vez anterior
my = (my1,my2,my3,my4,my5)
nombres = ("ej1_my1","ej1_my2","ej1_my3","ej1_my4","ej1_my5")
titulo= ("My K1","My K2", "My K3", "My K4", "My K5")

for x in num:
    plt.figure()                    
    plt.contourf(X1[0:99],Y1,my[x],escala_my,cmap='winter')
    plt.colorbar()
    plt.title(titulo[x])
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.xticks(np.arange(0,1000000,300000))
    plt.tight_layout()
    plt.savefig(nombres[x],dpi=200)

# corte zonal en la latitud central de la cuenca

plt.figure()
plt.plot(my1[25,:],'r',label="K1")
plt.plot(my2[25,:],'g',label="K2")
plt.plot(my3[25,:],'b',label="K3")
plt.plot(my4[25,:],'m',label="K4")
plt.plot(my5[25,:],'c',label="K5")
plt.plot(my5[0,:],'k-.')
plt.ylabel("My[Sv]")
plt.xlabel("Latitud[km]")
plt.title("Transporte meridional")
plt.legend()
plt.tight_layout()
plt.savefig("transporte_meridional", dpi=200)


# lo mismo con la vorticidad
plt.figure()
plt.plot(X1[0:100]/1000,vort1[25,:],'r', label = "K1") #dividido 1000 para que de en km
plt.plot(X1[0:100]/1000,vort2[25,:],'g', label = "K2") 
plt.plot(X1[0:100]/1000,vort3[25,:],'b', label = "K3")
plt.plot(X1[0:100]/1000,vort4[25,:],'c', label = "K4") 
plt.plot(X1[0:100]/1000,vort5[25,:],'m', label = "K5")  
plt.plot(vort1[0,:],'k-.')
plt.xlabel("Latitud[Km]")
plt.title("Vorticidad relativa")
plt.ylabel("Vort. relativa")
plt.legend()
plt.tight_layout()
plt.savefig("vorticidad_relativa", dpi=200)

###----------------4---------------###
# my pero de la cbo
# buscado a mano... my[50,:], cambia de signo en 7<-- extensión de la cbo
# esto tambien funca ---> np.where(my1[25,:]==0) 
# hay q buscar donde cambia de signo, puede q no existan ceros ya q no es continuo
#Los busco manualmente
 #cambio de signo en 7
my_cbo1=my1[25,:] # latitud (y) primera coordenada del array numero 25(centro de la cuenca)
my_cbo1_F=np.sum(my_cbo1[0:7])
my_cbo1_total=np.sum(my_cbo1) # esto ya estaba en sv
extension_cbo1=X1[7]
 #---> cambio de signo en 6
my_cbo2=my2[25,:]
my_cbo2_F=np.sum(my_cbo2[0:6])
my_cbo2_total=np.sum(my_cbo2) 
extension_cbo2=X2[6]

 #---> cambio de signo en 5
my_cbo3=my3[25,:] 
my_cbo3_F=np.sum(my_cbo3[0:5])
my_cbo3_total=np.sum(my_cbo3) 
extension_cbo3=X3[5]

#---> cambio de signo en 4
my_cbo4=my4[25,:] 
my_cbo4_F=np.sum(my_cbo4[0:4])
my_cbo4_total=np.sum(my_cbo4) 
extension_cbo4=X4[4]

#---> cambio de signo en 2
my_cbo5=my5[25,:] 
my_cbo5_F=np.sum(my_cbo5[0:2])
my_cbo5_total=np.sum(my_cbo5) 
extension_cbo5=X5[2]

# hay q presentarlo como tabla --> guardamos en excel usando:
# import pandas
# ordenando 
# variable.to_excel()

import pandas as pd

# se crea un archivo tipo dict ( "dictionary" ~ lista en R )
# solo rendondeo del total ya que da con ordenes 10^-7 pero no cero
# el transporte de borde oste no hace falta

ej_4 = {" " : ["My borde oeste","My total","Extension cbo"],
        "K1":[(my_cbo1_F),round(my_cbo1_total),extension_cbo1],
        "K2":[(my_cbo2_F),round(my_cbo2_total),extension_cbo2],
        "K3":[(my_cbo3_F),round(my_cbo3_total),extension_cbo3],
        "K4":[(my_cbo4_F),round(my_cbo4_total),extension_cbo4],
        "K5":[(my_cbo5_F),round(my_cbo5_total),extension_cbo5],}

# ahora pasado a un dataframe, los caracteres pasan a las filas y columnas
ej_4 = pd.DataFrame(data=ej_4)
ej_4.to_excel("ej_4.xls",index = False)

###----------------5----------------###
#ejercicio 5

termino1 = ((np.diff(psiF1,n=1, axis=1)))[25,:] 

# segundo termino, menos rotor del viento (-QG_curlw )

termino2 = -QG_curlw1[26,:] # porque tiene 52...

# laplaciano
from laplaciano import Calc_del2
lapla = Calc_del2(vort_temp1[:,:,0],0.1)

# tercer termino # 0.79 valor del eps 2
termino3 =  -0.025*lapla[25,:]

plt.figure()
plt.plot(termino1,"c",label = "Termino de Transporte")
plt.plot(termino2,"r",label = "Termino del Rotor de viento")
plt.plot(termino3,"m",label = "Termino de fricción")
plt.axhline(y = 0, color = "black") # marco la linea de y = 0
plt.xlabel("X")
plt.ylabel("valores adimensionales")
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("ej_3.png",dpi = 200)
#veamos que da cero o cercano a cero
#promedio cada termino
prom1=np.mean(termino1)
prom2=np.mean(termino2)
prom3=np.mean(termino3)
munk=prom1+prom2+prom3
error = (abs(0 -munk))*100
print(f'El error asociado es {error} %')
 ### LAS UNIDADES QUEDAN RARAS, MUY GRANDES, RESPETAMOS TOMAR TODO EN METROS
### DESDE EL CALCULO DE BETA, LOS VALORES INGRESADOS EN LA FUNCION CARGAR Y LAS CONVERSIONES
###----------------\m/----------------###
plt.grid()
plt.savefig("ej_5.png",dpi = 200)

###----------------\m/----------------###
 
