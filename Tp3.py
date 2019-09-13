# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:29:43 2019

@author: V
"""
### TP3 ###

import numpy as np
from matplotlib import pyplot as plt


Lx = 1500000 # dimensiones de la cuenca en metros
Ly = 1500000
nx = 150 # puntos de grilla
ny = 150
beta = 10**-11 # en metros
D = 2000 # metros

from Cargar import cargar 
psi_temp1,vort_temp1,psiF1,vortF1,QG_diag1,QG_curlw1,X1,Y1,dx1,dy1=cargar("D:/Facultad/Materias/Circulacion/TP3/out_tmp1/",Lx,Ly,nx,ny)
psi_temp2,vort_temp2,psiF2,vortF2,QG_diag2,QG_curlw2,X2,Y2,dx2,dy2=cargar('D:/Facultad/Materias/Circulacion/TP3/out_tmp2/',Lx,Ly,nx,ny)
psi_temp3,vort_temp3,psiF3,vortF3,QG_diag3,QG_curlw3,X3,Y3,dx3,dy3=cargar('D:/Facultad/Materias/Circulacion/TP3/out_tmp3/',Lx,Ly,nx,ny)
psi_temp4,vort_temp4,psiF4,vortF4,QG_diag4,QG_curlw4,X4,Y4,dx4,dy4=cargar('D:/Facultad/Materias/Circulacion/TP3/out_tmp4/',Lx,Ly,nx,ny)
psi_temp5,vort_temp5,psiF5,vortF5,QG_diag5,QG_curlw5,X5,Y5,dx5,dy5=cargar('D:/Facultad/Materias/Circulacion/TP3/out_tmp5/',Lx,Ly,nx,ny)

### Escape inercial ### 
# 1 (despues pruebo otro)
# R = 0.01, eps = 0.025 da exactamente 4 el cociente.
# simulacion x..(la x es de extremo....)
psi_tempx,vort_tempx,psiFx,vortFx,QG_diagx,QG_curlwx,X_x,Yx,dxx,dyx=cargar("D:/Facultad/Materias/Circulacion/TP3/out_tmp_x/",Lx,Ly,nx,ny)

# 2
# R = 0.005, eps = 0.0175
psi_tempxx,vort_tempxx,psiFxx,vortFxx,QG_diagxx,QG_curlwxx,Xxx,Yxx,dxxx,dyxx=cargar("D:/Facultad/Materias/Circulacion/TP3/out_tmp_xx/",Lx,Ly,nx,ny)


Tau = 0.25
U = (2*np.pi*Tau)/(1025*D*(beta)*(Lx))

# el ej 3 (elque dice 1) pide campos de corriente y transportes en Sv, asi que ya paso a Sv ****

corriente1 = psiF1*U*Lx/10**6
corriente2 = psiF2*U*Lx/10**6
corriente3 = psiF3*U*Lx/10**6
corriente4 = psiF4*U*Lx/10**6
corriente5 = psiF5*U*Lx/10**6
corrientex = psiFx*U*Lx/10**6
corrientexx = psiFxx*U*Lx/10**6

vort1 = vortF1*(U/Lx)
vort2 = vortF2*(U/Lx)
vort3 = vortF3*(U/Lx)
vort4 = vortF4*(U/Lx)
vort5 = vortF5*(U/Lx)
vortx = vortFx*(U/Lx)
vortxx = vortFxx*(U/Lx)


# Ej1 
# Energia

plt.figure()
plt.plot(QG_diag1[:,3], label='S1', color = "r")
plt.plot(QG_diag2[:,3], label="S2", color = "orange") # s1 y s3 iguales ya chequeado 2 veces.
plt.plot(QG_diag3[:,3], label="S3", color = "green")
plt.plot(QG_diag4[:,3], label="S4", color = "b")
plt.plot(QG_diag5[:,3], label="S5", color = "purple")
plt.title("Energia Cinetica")
plt.grid()
plt.xlabel("tiempo")
plt.ylabel("Energia cinetica")
plt.legend(loc = "lower right")
plt.savefig("energia_cin.png",dpi=200)

# Agregando las simulaciones de Escape inercial 

plt.figure()
plt.plot(QG_diag1[:,3], label='S1', color = "r")
plt.plot(QG_diag2[:,3], label="S2", color = "orange") # s1 y s3 iguales ya chequeado 2 veces.
plt.plot(QG_diag3[:,3], label="S3", color = "green")
plt.plot(QG_diag4[:,3], label="S4", color = "b")
plt.plot(QG_diag5[:,3], label="S5", color = "purple")
plt.plot(QG_diagx[:,3], label="S E.I", color = "violet")   #interesante resultado!! (esperable?? no hay friccion lateral)
plt.plot(QG_diagx[:,3], label="S E.I 2", color = "black")  # practicamente identico al anterior
plt.title("Energía Cinética")
plt.grid()
plt.xlabel("tiempo")
plt.ylabel("Energía cinética")
plt.legend(loc = "lower right")
plt.savefig("energia_cin_EI.png",dpi=200)


# Funcion corriente

corrientes = (corriente1 ,corriente2, corriente3, corriente4, corriente5)
nombres_c = ("corriente1","corriente2","corriente3","corriente4","corriente5")
titulo_c = ("Corriente S1", "Corriente S2", "Corriente S3","Corriente S4", "Corriente S5")
num = (0,1,2,3,4)
escala = np.arange(-0.8, 0.2, 0.1) 

for i in num:
    plt.figure()
    plt.contourf(X1, Y1, corrientes[i], escala, cmap = 'viridis')
    plt.colorbar(label = "[Sv]")
    plt.contour(X1, Y1, corrientes[i], levels = 0, colors = "w" )
    plt.title(titulo_c[i])
    plt.xlabel('longitud [Km]')
    plt.ylabel('latitud [Km]')
    plt.tight_layout()
    plt.xticks(np.arange(0, 1500000, 500000))
    plt.yticks(np.arange(0, 1500000, 250000))
    plt.savefig(nombres_c[i], dpi = 200)
    plt.show()

# la escala varia mucho con las simulaciones x
# hago otra para esos dos graficos nada masy
corrientes_EI = (corrientex, corrientexx)
nombres_EI = ("Corriente_SEI", "corriente_SEI2")
numx=(0, 1)
#escala_EI
for i in numx:
    plt.figure()
    plt.contourf(X1, Y1, corrientes_EI[i], levels = np.arange(-1.2, 0.16, 0.15), cmap = "viridis")  # lamento no usar winter, pero sino no se aprecian los cambios
    plt.colorbar(label = "[Sv]")
    if i == 1:
        plt.contour(X1, Y1, corrientes_EI[1], cmap = "viridis")
    plt.contour(X1, Y1, corrientes_EI[i], levels = 0, colors = "w" )
    plt.title(nombres_EI[i])
    plt.xlabel('longitud [Km]')
    plt.ylabel('latitud [Km]')
    plt.tight_layout()
    plt.xticks(np.arange(0, 1500000, 500000))
    plt.yticks(np.arange(0, 1500000, 250000))
    plt.savefig(nombres_EI[i], dpi = 200)
    plt.show()    
    
        
   
#isolineas del campo de vorticidad
vort_rel = (vort1, vort2, vort3, vort4, vort5, vortx, vortxx)
num3 = (0, 1, 2, 3, 4, 5, 6)
nombres_v = ("Vort_rel1", "Vort_rel2", "Vort_rel3", "Vort_rel4", "Vort_rel5", "vort_relx", "vort_relxx")
Tit_v = ("Vorticidad relativa 1", "Vorticidad relativa 2", "Vorticidad relativa 3", "Vorticidad relativa 4", "Vorticidad relativa 5", "Vorticidad relativa SEI", "Vorticidad relativa SEI2" )

for i in num3:
    plt.figure()
    plt.contourf(X1, Y1, vort_rel[i], levels = np.arange(-0.0000080, 0.000014, 0.000002), cmap = "jet") 
    plt.colorbar()
    plt.contour(X1, Y1, vort_rel[i], levels = 0, colors = "w" )
    plt.title(Tit_v[i])
    plt.xlabel('longitud [Km]')
    plt.ylabel('latitud[Km]')
    plt.xticks(np.arange(0, 1500000, 500000))
    plt.yticks(np.arange(0, 1500000, 250000))
    plt.savefig(nombres_v[i],dpi = 200)

vort_rel = (vort1, vort2, vort3, vort4, vort5, vortx, vortxx)
num4 = (0, 1, 2, 3, 4, 5, 6)
f= np.flip(-beta*Y1)  
"""
 #CHEQUEAR ESTO!  vorticidad planetaria negativa en HS (por eso el menos)
# invertida para que hacia el norte (ecuador) la vorticidad planetaria sea menor 
#llegando a cer cero en el extremo norte de la cuenca (ecuador)
#    
                  "grafico"
#
# ---------------Ecuador--------------------
#|   
#|O                     
#|E
#|S
#|T
#|E
#|
#|_________________BORDE SUR_______________

"""

from numpy import empty
vort_tot = empty([150,150,7]) #si se usa la simulacion x poner 6 en lugar de 5

titulo_v=("vorticidad total 1","vorticidad total 2","vorticidad total 3","vorticidad total 4","vorticidad total 5","vorticidad total EI","vorticidad total EI2")

columnas = np.arange(0,150,1)

for i in num4:
    for x in columnas:
        vort_tot[:,x,i]= f + vort_rel[i][:,x]
    plt.figure()
    plt.contourf(X1, Y1, vort_tot[:,:,i], levels = np.arange(-1.75e-5, 6e-6, 2.5e-6), cmap = "jet")
    plt.colorbar()
    plt.contour(X1, Y1, vort_tot[:,:,i],  levels = 0, colors = "w" )
    plt.title(titulo_v[i])
    plt.xlabel('Longitud[m]')
    plt.ylabel('Latitud[m]')
    plt.xticks(np.arange(0, 1500000, 500000))
    plt.yticks(np.arange(0, 1500000, 250000))
    plt.savefig(titulo_v[i], dpi = 200)
    plt.show()
    
# la escala de colores "viridis" para dar una idea de los valores negativos  y los pocos valores  # al final la cambie por "jet" y una escala con menos niveles para q sea mas clara..
# positivos donde la vorticidad relativa "vence" a la planetaria.
# vemos que a medida q aumeta la inercia la vorticidad positiva asociada a la CBO va desapareciendo    
# al aumentar rossby aumenta la no linealidad    
    
##### deltas #### (o sigma, nse)

delta_i = np.array([0.00005**(1/2), 0.0005**(1/2), 0.005**(1/2), 0.005**(1/2), 0.005**(1/2), 0.01**(1/2), 0.005**(1/2)])
delta_vi = np.array([0.001**(1/3), 0.001**(1/3), 0.001**(1/3), 0.001**(1/3), 0.001**(1/3), 0,0])
delta_f = np.array([0.01, 0.01, 0.01, 0.025, 0.05, 0.025, 0.175])

cociente1 = delta_i/delta_vi #  deberiamos ponerlo en los graficos
cociente2 = delta_i/delta_f  #  de corriente?? ademas sirve para el ej2

import pandas as pd
cocientes = {" " : ["delta_i/delta_vi", "delta_i/delta_f"],
             "S1":[round(cociente1[0], 2), round(cociente2[0], 2)],
             "S2":[round(cociente1[1], 2), round(cociente2[1], 2)],
             "S3":[round(cociente1[2], 2), round(cociente2[2], 2)],
             "S4":[round(cociente1[3], 2), round(cociente2[3], 2)],
             "S5":[round(cociente1[4], 2), round(cociente2[4], 2)],
             "S_EI":[round(cociente1[5], 2), round(cociente2[5], 2)],
             "S_EI2":[round(cociente1[6], 2), round(cociente2[6], 2)],}
                   
# ahora pasado a un dataframe, los caracteres pasan a las filas y columnas
cocientes = pd.DataFrame(data = cocientes)
cocientes.to_excel("cocientes.xls",index = False)


#las corrientes ya estan en sv

my1 = D*(np.diff(corriente1, n = 1, axis=1))
my2 = D*(np.diff(corriente2, n = 1, axis=1))
my3 = D*(np.diff(corriente3, n = 1, axis=1))
my4 = D*(np.diff(corriente4, n = 1, axis=1))
my5 = D*(np.diff(corriente5, n = 1, axis=1))
myx = D*(np.diff(corrientex, n = 1, axis=1))
myxx = D*(np.diff(corrientexx, n = 1, axis=1))
# campos de transporte meridional


my = (my1, my2, my3, my4, my5)
nombres = ("ej3_my1", "ej3_my2", "ej3_my3", "ej3_my4","ej3_my5")
titulo= ("My S1", "My S2", "My S3", "My S4", "My S5")

for x in num:
    plt.figure()                    
    plt.contourf(X1[0:149], Y1, my[x], levels = np.arange(-480,200,80), cmap = "jet")
    plt.colorbar(label = "[Sv]")
    plt.contour(X1[0:149], Y1, my[x],levels = 0, colors = "w")
    plt.title(titulo[x])
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.xticks(np.arange(0, 1500000, 500000))
    plt.xticks(np.arange(0, 1500000, 250000))
    plt.tight_layout()
    plt.savefig(nombres[x], dpi = 200)
    
# otra vez, las escalas para las simulaciones de escape inercial son muy distintas. 
    
myx = (myx,myxx)
nombres_x = ("ej3_myx", "ej3_myxx")
titulo_x= ("My SEI", "My SEI2")

# cambio cmap, porque no se nota nada sino.

for x in numx:
    plt.figure()                    
    plt.contourf(X1[0:149], Y1, myx[x], levels = np.arange(-1000,800,200), cmap = "jet")
    plt.colorbar(label = "[Sv]")
    plt.contour(X1[0:149], Y1, myx[x], levels = 0, colors = "w")
    plt.title(titulo_x[x])
    plt.xlabel('Longitud')
    plt.ylabel('Latitud')
    plt.xticks(np.arange(0, 1500000, 500000))
    plt.xticks(np.arange(0, 1500000, 250000))
    plt.savefig(nombres_x[x], dpi = 200)
       

220
             "S3":[round(cociente1[2], 2), round(cociente2[2], 2)],
221
             "S4":[round(cociente1[3], 2), round(cociente2[3], 2)],
222
             "S5":[round(cociente1[4], 2), round(cociente2[4], 2)],
223
             "S_EI":[round(cociente1[5], 2), round(cociente2[5], 2)],
224
             "S_EI2":[round(cociente1[6], 2), round(cociente2[6], 2)],}
225
                   
226
# ahora pasado a un dataframe, los caracteres pasan a las filas y columnas
227
cocientes = pd.DataFrame(data = cocientes)
228
cocientes.to_excel("cocientes.xls",index = False)
229
​
230
​
231
#las corrientes ya estan en sv
232
​
233
my1 = D*(np.diff(corriente1, n = 1, axis=1))
234
my2 = D*(np.diff(corriente2, n = 1, axis=1))
235
my3 = D*(np.diff(corriente3, n = 1, axis=1))
236
my4 = D*(np.diff(corriente4, n = 1, axis=1))
237
my5 = D*(np.diff(corriente5, n = 1, axis=1))
238
myx = D*(np.diff(corrientex, n = 1, axis=1))
239
myxx = D*(np.diff(corrientexx, n = 1, axis=1))
240
# campos de transporte meridional
241
​
242
​
243
my = (my1, my2, my3, my4, my5)
244
nombres = ("ej3_my1", "ej3_my2", "ej3_my3", "ej3_my4","ej3_my5")
245
titulo= ("My S1", "My S2", "My S3", "My S4", "My S5")
246
​
247
for x in num:
248
    plt.figure()                    
249
    plt.contourf(X1[0:149], Y1, my[x], levels = np.arange(-480,200,80), cmap = "jet")
250
    plt.colorbar(label = "[Sv]")
251
    plt.contour(X1[0:149], Y1, my[x],levels = 0, colors = "w")
252
    plt.title(titulo[x])
253
    plt.xlabel('Longitud')
254
    plt.ylabel('Latitud')
255
    plt.xticks(np.arange(0, 1500000, 500000))
256
    plt.xticks(np.arange(0, 1500000, 250000))
257
    plt.tight_layout()
258
    plt.savefig(nombres[x], dpi = 200)
259
    
260
# otra vez, las escalas para las simulaciones de escape inercial son muy distintas. 
261
    
262
myx = (myx,myxx)
263
nombres_x = ("ej3_myx", "ej3_myxx")
264
titulo_x= ("My SEI", "My SEI2")
265
​
266
# cambio cmap, porque no se nota nada sino.
267
​
268
for x in numx:
269
    plt.figure()                    
270
    plt.contourf(X1[0:149], Y1, myx[x], levels = np.arange(-1000,800,200), cmap = "jet")
271
    plt.colorbar(label = "[Sv]")
272
    plt.contour(X1[0:149], Y1, myx[x], levels = 0, colors = "w")
273
    plt.title(titulo_x[x])
274
    plt.xlabel('Longitud')
275
    plt.ylabel('Latitud')
276
    plt.xticks(np.arange(0, 1500000, 500000))
277
    plt.xticks(np.arange(0, 1500000, 250000))
278
    plt.savefig(nombres_x[x], dpi = 200)
279
       
280
​
@mjbarboza
Commit changes
