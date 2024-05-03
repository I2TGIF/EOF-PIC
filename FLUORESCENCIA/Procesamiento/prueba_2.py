import numpy as np
import math
import scipy.signal
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import entropy
from scipy import integrate
from pathlib import Path
from io import BytesIO
import base64
import pdb
import os
from django.conf import *

import mpld3

#from muestra.views import home


################################################################################################
################################################################################################
######################### Procesamiento de información espectral################################
#########################Extracción de caracteristicas #########################################
################################################################################################
################################################################################################

def fun(x,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d,e,f,g,h,t1):
    Fung = t1 + ((10**(-(0.0000001*d*np.exp(-2*((x-336.35)/34.85)**2) + 0.0000001*e*np.exp(-2*((x-352.03)/46.4)**2) + 0.0000001*f*(np.exp(-2*((x-262.61)/25.8)**2) + 0.45*np.exp(-2*((x-345.51)/54.41)**2)) + 0.0000001*g*(np.exp(-2*((x-260.17)/28.77)**2) + 0.45*np.exp(-2*((x-387.2)/112.29)**2) + 0.5*np.exp(-2*((x-457.57)/100.58)**2)))))*(10**(-(0.0000001*d*np.exp(-2*((337.1-336.35)/34.85)**2) + 0.0000001*e*np.exp(-2*((337.1-352.03)/46.4)**2) + 0.0000001*f*(np.exp(-2*((337.1-262.61)/25.8)**2) + 0.45*np.exp(-2*((337.1-345.51)/54.41)**2)) + 0.0000001*g*(np.exp(-2*((337.1-260.17)/28.77)**2) + 0.45*np.exp(-2*((337.1-387.2)/112.29)**2) + 0.5*np.exp(-2*((337.1-457.57)/100.58)**2)))))*(d*a1*np.exp(-2*((x-b1)/c1)**2) + e*np.exp(-2*((337.1-336.35)/34.85)**2)*a2*np.exp(-2*((x-b2)/c2)**2) + f*np.exp(-2*((337.1-352.03)/46.4)**2)*a3*np.exp(-2*((x-b3)/c3)**2) + g*(np.exp(-2*((337.1-262.61)/25.8)**2) + 0.45*np.exp(-2*((337.1-345.51)/54.41)**2))*a4*np.exp(-2*((x-b4)/c4)**2) + h*(np.exp(-2*((337.1-260.17)/28.77)**2) + 0.45*np.exp(-2*((337.1-387.2)/112.29)**2) + 0.5*np.exp(-2*((337.1-457.57)/100.58)**2))*a5*np.exp(-2*((x-b5)/c5)**2)))
    return Fung
def ObtPara(DAT,i):
    a1=DAT[i,0]
    b1=DAT[i,1]
    c1=DAT[i,2]
    d=DAT[i,3]
    a2=DAT[i,4]
    b2=DAT[i,5]
    c2=DAT[i,6]
    e=DAT[i,7]
    a3=DAT[i,8]
    b3=DAT[i,9]
    c3=DAT[i,10]
    f=DAT[i,11]
    a4=DAT[i,12]
    b4=DAT[i,13]
    c4=DAT[i,14]
    g=DAT[i,15]
    a5=DAT[i,16]
    b5=DAT[i,17]
    c5=DAT[i,18]
    h=DAT[i,19]
    t1=DAT[i,20]
    return a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d,e,f,g,h,t1

#upper_bound = [1, 1, 1, 1, 1, 380, 400, 420, 480, 550, 40, 70, 70, 70, 80, np.inf, np.inf, np.inf, np.inf, np.inf, 1]
#StartPoint = [1, 1, 1, 1, 1, 370, 393.52, 419.87, 454.62, 517.83, 50, 80.88, 75.85, 55.42, 65.51, 0.001, 0.001, 0.001, 0.001, 0.001, 1]
def SaveTXT(NomDat,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,SumGauss,x1,yws,DAT,j):

    datos=[]
    Mparam=np.zeros((j,34))
    for i in range(1,j + 1):
        I1 = integrate.simps(Gauss11[:,i-1],x=x1)
        I2 = integrate.simps(Gauss12[:,i-1],x=x1)
        I3 = integrate.simps(Gauss13[:,i-1],x=x1)
        I4 = integrate.simps(Gauss14[:,i-1],x=x1)
        I5 = integrate.simps(Gauss15[:,i-1],x=x1)
        
        Asum=integrate.simps(SumGauss[:,i-1],x=x1)
        a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d,e,f,g,h,t1=ObtPara(DAT,i-1)
        F=fun(x1,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d,e,f,g,h,t1)
        Aaju=integrate.simps(F,x=x1)
        MeanAjuste=np.mean(F)
        MeanSum=np.mean(SumGauss[:,i-1])
        
        max1 = np.argmax(Gauss11[:,i-1])
        max2 = np.argmax(Gauss12[:,i-1])
        max3 = np.argmax(Gauss13[:,i-1])
        max4 = np.argmax(Gauss14[:,i-1])
        max5 = np.argmax(Gauss15[:,i-1])
        
        dis12 = abs(x1[max1]-x1[max2])
        dis23 = abs(x1[max2]-x1[max3])
        dis34 = abs(x1[max3]-x1[max4])
        dis45 = abs(x1[max4]-x1[max5])
        
        ent = entropy(yws[:,i])
        
        G1 = str(DAT[i-1,0])+"\t"+str(DAT[i-1,1])+"\t"+str(DAT[i-1,2])+"\t"+str(DAT[i-1,3])+"\t"+str(I1)+"\t"
        G2= str(DAT[i-1,4])+"\t"+str(DAT[i-1,5])+"\t"+str(DAT[i-1,6])+"\t"+str(DAT[i-1,7])+"\t"+str(I2)+"\t"
        G3= str(DAT[i-1,8])+"\t"+str(DAT[i-1,9])+"\t"+str(DAT[i-1,10])+"\t"+str(DAT[i-1,11])+"\t"+str(I3)+"\t"
        G4= str(DAT[i-1,12])+"\t"+str(DAT[i-1,13])+"\t"+str(DAT[i-1,14])+"\t"+str(DAT[i-1,15])+"\t"+str(I4)+"\t"
        G5= str(DAT[i-1,16])+"\t"+str(DAT[i-1,17])+"\t"+str(DAT[i-1,18])+"\t"+str(DAT[i-1,19])+"\t"+str(I5)+"\t"
        ByD= str(DAT[i-1,20])+"\t"+str(dis12)+"\t"+str(dis23)+"\t"+str(dis34)+"\t"+str(dis45)+"\t"
        AjuSum=str(Aaju)+"\t"+str(Asum)+"\t"+str(MeanAjuste)+"\t"+str(MeanSum) #+"\t"+str(ent)

        
        datos.append(G1+G2+G3+G4+G5+ByD+AjuSum)

        Mparam[i-1,:]=[DAT[i-1,0],DAT[i-1,1],DAT[i-1,2],DAT[i-1,3],I1,
                       DAT[i-1,4],DAT[i-1,5],DAT[i-1,6],DAT[i-1,7],I2,
                       DAT[i-1,8],DAT[i-1,9],DAT[i-1,10],DAT[i-1,11],I3,
                       DAT[i-1,12],DAT[i-1,13],DAT[i-1,14],DAT[i-1,15],I4,
                       DAT[i-1,16],DAT[i-1,17],DAT[i-1,18],DAT[i-1,19],I5,
                       DAT[i-1,20],dis12,dis23,dis34,dis45,
                       Aaju,Asum,MeanAjuste,MeanSum]
    
    base_dir =settings.MEDIA_ROOT    
    NomDat = os.path.join(base_dir, 'muestra/datos/Datos')
    #pdb.set_trace()
    file = open( NomDat + ".txt", "a")
    for k in range(len(datos)):
        file.write(datos[k] + "\n")
    file.close()

    np.savetxt(NomDat + "_Paciente.txt",Mparam)


def modificarLinea(archivo,buscar,reemplazar):
    #path = os.path.join(os.path.dirname(os.path.realpath(__file__)), archivo)
    base_dir =settings.MEDIA_ROOT    
    my_file = os.path.join(base_dir, archivo)
    file = open(my_file,"r")
    fileN = file.read()
    fileN = fileN.replace(buscar,reemplazar)
    file = open(my_file,"w")
    file.write(fileN)


def Signal(Folder,File,NumEsp,NumStart,Nfolder,NomDat):
    
    StartPoint = [1, 1, 1, 1, 1, 360, 393.52, 419.87, 454.62, 517.83, 20, 35, 35, 55.42, 65.51, 0.001, 0.001, 0.001, 0.001, 0.001, 4]
    lower_bound = [0, 0, 0, 0, 0, 340, 380, 400, 420, 480, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    upper_bound = [1, 1, 1, 1, 1, 380, 400, 420, 480, 550, 40, 70, 70, 70, 80, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf]

    carpeta = Folder + "/"
    #carpeta = carpeta.strip(" ")
    #pdb.set_trace()
    num = NumStart
    cont = num
    Muestra = File 
    e = np.arange(0,NumEsp,1)
    
    for k in e:
        
        if cont < 10:
            Nombre = (carpeta + Muestra + "0000" + str(cont) + ".txt")
        elif (10 <= cont) and (cont < 100):
            Nombre = (carpeta + Muestra + "000" + str(cont) + ".txt")
        elif (100 <= cont) and (cont < 1000):
            Nombre = (carpeta + Muestra + "00" + str(cont) + ".txt")
        
      
        
        modificarLinea(Nombre,",",".")
        base_dir =settings.MEDIA_ROOT    
        my_file = os.path.join(base_dir, Nombre)
        
        file = open(my_file,"r")
        
        fileN = file.read()
       ###para primera base de datos
        M = np.loadtxt(my_file,skiprows=0)  #cambiar ese numero dependiendo del archivo txt
        ###para segunda base de datos
        #M = np.loadtxt(my_file,skiprows=18)
    
    
        if cont > (num + 1):
            z = M[:,1]
            w = np.insert(w, w.shape[1], z, 1)
            
        
        elif cont == num:
            
            x = M[:,0]
            w = M[:,1]
            
        elif cont == (num + 1):
            
            z = M[:,1]
            w = (np.array([w,z])).T
        
        cont = cont + 1
        
    nw = len(w[1,:])
    d = math.ceil(nw/30)
    
    vx=0
    g1=0
    while(vx<349):
        g1 = g1 + 1
        vx=x[g1]
        
    g2=0
    while(vx<599):
        g2 = g2 + 1
        vx=x[g2]
    
    x1 = x[g1:g2+1]
    
    wp = np.zeros((len(x1),NumEsp + 1))
    yw = np.zeros((len(x1),NumEsp + 1))    
    Gauss11=np.zeros((len(x1),NumEsp + 1))
    Gauss12=np.zeros((len(x1),NumEsp + 1))
    Gauss13=np.zeros((len(x1),NumEsp + 1))
    Gauss14=np.zeros((len(x1),NumEsp + 1))
    Gauss15=np.zeros((len(x1),NumEsp + 1))
    SumGauss=np.zeros((len(x1),NumEsp + 1))
    DAT=np.zeros((d,21))
        
    for j in range (1,d + 1):
        
        sum1 = 0
        nt = 0
        
        #for n in range ((6*(j-1)), (6*j)): ######segunda base de datos
        for n in range (4+(30*(j-1)), (30*j)-4): ####primera base 
            
            if n <= nw:
                
                sum1 = w[g1:g2+1, n - 1] + sum1
                nt = nt + 1
                
        wp[:,j-1] = sum1/nt
        
        yw[:,j-1] = scipy.signal.savgol_filter(wp[:,j-1], 115, 9) 
        
        try:            
            f1,f2 = curve_fit(fun, x1, yw[:,j-1], p0 = StartPoint, bounds= (lower_bound,upper_bound))
        except:
            print("No se puede calcular un ajuste óptimo")
        
        a1,a2,a3,a4,a5=f1[0],f1[1],f1[2],f1[3],f1[4]
        b1,b2,b3,b4,b5=f1[5],f1[6],f1[7],f1[8],f1[9]
        c1,c2,c3,c4,c5 = f1[10],f1[11],f1[12],f1[13],f1[14]
        d = f1[15]
        e = f1[16]
        f = f1[17]
        g = f1[18]
        h = f1[19]
        t1 = f1[20]
        DAT[j-1,:]=[a1,b1,c1,d,a2,b2,c2,e,a3,b3,c3,f,a4,b4,c4,g,a5,b5,c5,h,t1]
        
        tx = (10**(-(0.0000001*d*np.exp(-2*((337.1-336.35)/34.85)**2) + 0.0000001*e*np.exp(-2*((337.1-352.03)/46.4)**2) + 0.0000001*f*(np.exp(-2*((337.1-262.61)/25.8)**2) + 0.45*np.exp(-2*((337.1-345.51)/54.41)**2)) + 0.0000001*g*(np.exp(-2*((337.1-260.17)/28.77)**2) + 0.45*np.exp(-2*((337.1-387.2)/112.29)**2) + 0.5*np.exp(-2*((337.1-457.57)/100.58)**2)))))

        Gauss11[:,j-1]=tx*d*a1*np.exp(-2*((x1-b1)/c1)**2)
        Gauss12[:,j-1]=tx*e*np.exp(-2*((337.1-336.35)/34.85)**2)*a2*np.exp(-2*((x1-b2)/c2)**2)
        Gauss13[:,j-1]=tx*f*np.exp(-2*((337.1-352.03)/46.4)**2)*a3*np.exp(-2*((x1-b3)/c3)**2)
        Gauss14[:,j-1]=tx*g*(np.exp(-2*((337.1-262.61)/25.8)**2) + 0.45*np.exp(-2*((337.1-345.51)/54.41)**2))*a4*np.exp(-2*((x1-b4)/c4)**2)
        Gauss15[:,j-1]=tx*h*(np.exp(-2*((337.1-260.17)/28.77)**2) + 0.45*np.exp(-2*((337.1-387.2)/112.29)**2) + 0.5*np.exp(-2*((337.1-457.57)/100.58)**2))*a5*np.exp(-2*((x1-b5)/c5)**2)
        SumGauss[:,j-1]=Gauss11[:,j-1] + Gauss12[:,j-1] + Gauss13[:,j-1] + Gauss14[:,j-1] + Gauss15[:,j-1]
                           
    yws = np.zeros((len(x1), j+1))
    yws[:,0] = x1
    yws[:,1:] = yw[:,0:j]

    SaveTXT(NomDat,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,SumGauss,x1,yws,DAT,j)

    return j,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,SumGauss
#gquien 

def plot(j,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,NomImag,SumGauss):
    
    n=0
    for i in range(1,j + 1):
        n += 1
        fig = plt.figure()
       # plt.plot(x1,yws[:,i],color='k')

        #plt.plot(x1,Gauss11[:,i-1],color='r')
        plt.plot(x1,Gauss12[:,i-1],color='g')
        plt.plot(x1,Gauss13[:,i-1],color='b')
        plt.plot(x1,Gauss14[:,i-1],color='c')
        plt.plot(x1,Gauss15[:,i-1],color='y')
        plt.plot(x1,SumGauss[:,i-1],color='m')
        plt.xlabel('Longitud de Onda (nm)')
        plt.ylabel('Intensidad de Emisión')
        base_dir =settings.MEDIA_ROOT    
        NomImag = os.path.join(base_dir, 'muestra/imagenes/imagen')
        plt.savefig(NomImag +str(n) +".jpg")
        html_graph = mpld3.fig_to_html(fig)
        #buffer = BytesIO()
        #plt.savefig(buffer, format='png')
        #buffer.seek(0)
        #image_png = buffer.getvalue()
        #buffer.close()

        #graphic = base64.b64encode(image_png)
        #graphic = graphic.decode('utf-8')
    return n    
    #return graphic, mpld3.fig_to_html(fig), html_graph
    #return mpld3.fig_to_html(fig), html_graph










#def plot(j,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,NomImag,SumGauss):
    
 #   n=0
 #   for i in range(1,j + 1):
  #      n += 1
   #     fig = plt.figure()
   #     plt.plot(x1,yws[:,i],color='k')
    #    #plt.plot(x1,Gauss11[:,i-1],color='r')
     #   plt.plot(x1,Gauss12[:,i-1],color='g')
      #  plt.plot(x1,Gauss13[:,i-1],color='b')
       # plt.plot(x1,Gauss14[:,i-1],color='c')
       # plt.plot(x1,Gauss15[:,i-1],color='y')
       # plt.plot(x1,SumGauss[:,i-1],color='m')
        
       # plt.savefig(NomImag +str(n) +".jpg")
        
   # return mpld3.fig_to_html(fig)
    


# Create your models here.



    