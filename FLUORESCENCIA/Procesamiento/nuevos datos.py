################################NO SE ESTÁ USUANDO################################################



import numpy as np
import math
import scipy.signal
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pathlib import Path
from scipy.stats import entropy
from scipy import integrate

def fun(x,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d,e,f,g,h,t1):
    Fung = t1 + ((10**(-(0.0000001*d*np.exp(-2*((x-336.35)/34.85)**2) + 0.0000001*e*np.exp(-2*((x-352.03)/46.4)**2) + 0.0000001*f*(np.exp(-2*((x-262.61)/25.8)**2) + 0.45*np.exp(-2*((x-345.51)/54.41)**2)) + 0.0000001*g*(np.exp(-2*((x-260.17)/28.77)**2) + 0.45*np.exp(-2*((x-387.2)/112.29)**2) + 0.5*np.exp(-2*((x-457.57)/100.58)**2)))))*(10**(-(0.0000001*d*np.exp(-2*((337.1-336.35)/34.85)**2) + 0.0000001*e*np.exp(-2*((337.1-352.03)/46.4)**2) + 0.0000001*f*(np.exp(-2*((337.1-262.61)/25.8)**2) + 0.45*np.exp(-2*((337.1-345.51)/54.41)**2)) + 0.0000001*g*(np.exp(-2*((337.1-260.17)/28.77)**2) + 0.45*np.exp(-2*((337.1-387.2)/112.29)**2) + 0.5*np.exp(-2*((337.1-457.57)/100.58)**2)))))*(d*a1*np.exp(-2*((x-b1)/c1)**2) + e*np.exp(-2*((337.1-336.35)/34.85)**2)*a2*np.exp(-2*((x-b2)/c2)**2) + f*np.exp(-2*((337.1-352.03)/46.4)**2)*a3*np.exp(-2*((x-b3)/c3)**2) + g*(np.exp(-2*((337.1-262.61)/25.8)**2) + 0.45*np.exp(-2*((337.1-345.51)/54.41)**2))*a4*np.exp(-2*((x-b4)/c4)**2) + h*(np.exp(-2*((337.1-260.17)/28.77)**2) + 0.45*np.exp(-2*((337.1-387.2)/112.29)**2) + 0.5*np.exp(-2*((337.1-457.57)/100.58)**2))*a5*np.exp(-2*((x-b5)/c5)**2)))
    return Fung

def Graf_save(j,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,NomImag,SumGauss):
    
    for i in range(1,j + 1):
    
        plt.plot(x1,yws[:,i],color='k')
        #plt.plot(x1,Gauss11[:,i-1],color='r')
        plt.plot(x1,Gauss12[:,i-1],color='g')
        plt.plot(x1,Gauss13[:,i-1],color='b')
        plt.plot(x1,Gauss14[:,i-1],color='c')
        plt.plot(x1,Gauss15[:,i-1],color='y')
        plt.plot(x1,SumGauss[:,i-1],color='m')
        
        plt.savefig(NomImag + ".jpg")
        plt.show()

def SaveTXT(NomDat,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d,e,f,g,h,t1,j):

    file = open( NomDat + ".txt", "w")
    file.write("Amplitudes" + "\n")
    file.write(str(a1)+"\t"+str(a2) +"\t"+str(a3)+"\t"+str(a4)+"\t"+str(a5)+ "\n")
    file.write("Longitudes de Onda Centrales" + "\n")
    file.write(str(b1)+"\t"+str(b2) +"\t"+str(b3)+"\t"+str(b4)+"\t"+str(b5)+ "\n")
    file.write("FWHM" + "\n")
    file.write(str(c1)+"\t"+str(c2) +"\t"+str(c3)+"\t"+str(c4)+"\t"+str(c5)+ "\n")
    file.write("Concentraciones" + "\n")
    file.write(str(d)+"\t"+str(e) +"\t"+str(f)+"\t"+str(g)+"\t"+str(h)+ "\n")
    
    for i in range(1,j + 1):
    
        I1 = integrate.simps(Gauss11[:,i-1],x=x1)
        I2 = integrate.simps(Gauss12[:,i-1],x=x1)
        I3 = integrate.simps(Gauss13[:,i-1],x=x1)
        I4 = integrate.simps(Gauss14[:,i-1],x=x1)
        I5 = integrate.simps(Gauss15[:,i-1],x=x1)
        
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
        file.write("Areas" + "\n")
        file.write(str(I1)+"\t"+str(I2) +"\t"+str(I3)+"\t"+str(I4)+"\t"+str(I5)+ "\n")
        file.write("background = " + str(t1) +"\n")
        file.write("Entropia = " + str(ent) +"\n")
        file.write("Distancia 2a3 = " + str(dis23) +"\n")
        file.write("Distancia 3a4 = " + str(dis34) +"\n")
        file.write("Distancia 4a5 = " + str(dis45) +"\n")
        file.close()

def modificarLinea(archivo,buscar,reemplazar):
    
    file = open(archivo,"r")
    fileN = file.read()
    fileN = fileN.replace(buscar,reemplazar)
    file = open(archivo,"w")
    file.write(fileN)
    file.close()

def Proces(carpeta,Mues,NumEsp,n1,num):
    
    StartPoint = [1, 1, 1, 1, 1, 360, 393.85, 405.48, 474.58, 570, 50, 80.88, 50, 55.42, 65.51, 0.001, 0.001, 0.001, 0.001, 0.001, 1]
    lower_bound = [0, 0, 0, 0, 0, 350, 370, 400, 470, 550, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
    upper_bound = [1, 1, 1, 1, 1, 370, 400, 420, 515, 580, 60, 85, 70, 70, 80, np.inf, np.inf, np.inf, np.inf, np.inf, 1]
    
    #FolderImag= carpeta + " imagenes"
    FolderDat= carpeta + " Datos"
    carpeta = carpeta + "\ "
    carpeta = carpeta.strip(" ")
    cont = num
    
    try:
        #Nfolder = Path(carpeta + FolderImag)
        Nfolder.mkdir(parents=True)
        Nfolder = Path(carpeta + FolderDat)
        Nfolder.mkdir(parents=True)
    except: 
        pass
    
    #FolderImag = FolderImag + "\ "
    FolderDat = FolderDat + "\ "
    #FolderImag = FolderImag.strip(" ")
    FolderDat = FolderDat.strip(" ")
    A=0
    for D in np.arange(1,n1 + 1):
        A += 1    
        Muestra = (Mues).format(A)
        cont = 1
        #NomImag=carpeta + FolderImag + ("1082A9_{0}").format(A)
        NomDat=carpeta + FolderDat + ("1082A9_{0}").format(A)
        
        for k in np.arange(1,NumEsp+1):
            
            if cont < 10:
                Nombre = (carpeta + Muestra + str(cont) + ".txt")
            
            modificarLinea(Nombre,",",".")
            
            file = file = open(Nombre,"r")
            M = np.loadtxt(Nombre,skiprows=18)
                
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
            file.close()
        
        nw = len(w[1,:])
        d = math.ceil(NumEsp/30)
        
        g1 = 580
        g2 = 1500
        x1 = x[g1:g2]
        wp = np.zeros((g2-g1,NumEsp + 1))
        yw = np.zeros((g2-g1,NumEsp + 1))
        Gauss11=np.zeros((g2-g1,NumEsp + 1))
        Gauss12=np.zeros((g2-g1,NumEsp + 1))
        Gauss13=np.zeros((g2-g1,NumEsp + 1))
        Gauss14=np.zeros((g2-g1,NumEsp + 1))
        Gauss15=np.zeros((g2-g1,NumEsp + 1))
        SumGauss=np.zeros((g2-g1,NumEsp + 1))
            
        for j in range (1,d + 1):
            
            sum1 = 0
            nt = 0
            
            for n in range (4+(30*(j-1)), (30*j)-4):
                
                if n <= nw:
                    
                    sum1 = w[g1:g2, n - 1] + sum1
                    nt = nt + 1                
            
            wp[:,j-1] = sum1/nt
            
            yw[:,j-1] = scipy.signal.savgol_filter(wp[:,j-1], 115, 9) 
            
            try:
                f1,f2 = curve_fit(fun, x1, yw[:,j-1], p0 = StartPoint, bounds= (lower_bound,upper_bound))
            except:
                print("No se puede calcular un ajuste optimo")           
            a1,a2,a3,a4,a5=f1[0],f1[1],f1[2],f1[3],f1[4]
            b1,b2,b3,b4,b5=f1[5],f1[6],f1[7],f1[8],f1[9]
            c1,c2,c3,c4,c5 = f1[10],f1[11],f1[12],f1[13],f1[14]
            d = f1[15]
            e = f1[16]
            f = f1[17]
            g = f1[18]
            h = f1[19]
            t1 = f1[20]
            
            tx = (10**(-(0.0000001*d*np.exp(-2*((337.1-336.35)/34.85)**2) + 0.0000001*e*np.exp(-2*((337.1-352.03)/46.4)**2) + 0.0000001*f*(np.exp(-2*((337.1-262.61)/25.8)**2) + 0.45*np.exp(-2*((337.1-345.51)/54.41)**2)) + 0.0000001*g*(np.exp(-2*((337.1-260.17)/28.77)**2) + 0.45*np.exp(-2*((337.1-387.2)/112.29)**2) + 0.5*np.exp(-2*((337.1-457.57)/100.58)**2)))))
            
            Gauss11[:,j-1]=tx*d*a1*np.exp(-2*((x1-b1)/c1)**2)
            Gauss12[:,j-1]=tx*e*np.exp(-2*((337.1-336.35)/34.85)**2)*a2*np.exp(-2*((x1-b2)/c2)**2)
            Gauss13[:,j-1]=tx*f*np.exp(-2*((337.1-352.03)/46.4)**2)*a3*np.exp(-2*((x1-b3)/c3)**2)
            Gauss14[:,j-1]=tx*g*(np.exp(-2*((337.1-262.61)/25.8)**2) + 0.45*np.exp(-2*((337.1-345.51)/54.41)**2))*a4*np.exp(-2*((x1-b4)/c4)**2)
            Gauss15[:,j-1]=tx*h*(np.exp(-2*((337.1-260.17)/28.77)**2) + 0.45*np.exp(-2*((337.1-387.2)/112.29)**2) + 0.5*np.exp(-2*((337.1-457.57)/100.58)**2))*a5*np.exp(-2*((x1-b5)/c5)**2)
            SumGauss[:,j-1]=Gauss11[:,j-1] + Gauss12[:,j-1] + Gauss13[:,j-1] + Gauss14[:,j-1] + Gauss15[:,j-1]
                    
        yws = np.zeros((g2-g1, j+1))
        yws[:,0] = x1
        yws[:,1:] = yw[:,0:j]
        
        SaveTXT(NomDat,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,c1,c2,c3,c4,c5,d,e,f,g,h,t1,j)
        Graf_save(j,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,NomImag,SumGauss)
        
        
carpeta = "1082A9-2"
Mues = "1082A9_{0}_HR4C9521_" 
NumEsp = 5 
n1 = 7 #numero de archivos por grupo de NumEsp
num = 1 #numero inicial
Proces(carpeta,Mues,NumEsp,n1,num)
