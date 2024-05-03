
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
#from django.conf.settings import local
from django.conf import settings
#from settings import local 
import os
import mpld3


def Plot_PCA(transformada,grupo,NomImag3):
    fig_bif2,ax2_bif = plt.subplots(1,1)
    plt.xlabel("Componente 1")
    plt.ylabel("Componente 2")
    
    n=0
    for i in range(len(grupo)):
        if grupo[i] ==1:
            ax2_bif.scatter(transformada[i,0],transformada[i,1], color='c', marker='+')
        elif grupo[i] ==2:
            ax2_bif.scatter(transformada[i,0],transformada[i,1] , color='r', marker='x')
        else:
            n = n+1
            ax2_bif.scatter(transformada[i,0],transformada[i,1] , color='g', marker='D',s=20)
            ax2_bif.annotate(str(n),xy=(transformada[i,0], transformada[i,1]))
    
   # html_graph = mpld3.fig_to_html(fig)
    graficapca = NomImag3 +".jpg"
    plt.savefig(graficapca)
    
    
    return graficapca 

"""
def Plot_PCA(transformada,grupo,number_image,NomImag3):
    

    fig_bif2,ax2_bif = plt.subplots(1,1)
    plt.xlabel("Componente 1")
    plt.ylabel("Componente 2")
    for i in range(len(grupo)):
        #fig = plt.figure()
        if grupo[i] ==1:
            ax2_bif.scatter(transformada[i,0],transformada[i,1], color='b', marker='+')
        elif grupo[i] ==2:
            ax2_bif.scatter(transformada[i,0],transformada[i,1] , color='r', marker='x')
        else:
            ax2_bif.scatter(transformada[i,0],transformada[i,1] , color='c', marker='D')
        
        #html_graph = mpld3.fig_to_html(fig)
    #number_image = 1
      
    #NomImag3 = os.path.join(base_dir, 'muestra/imagenes1/imagen')
    graficapca = NomImag3 + str(number_image+1) +".jpg"
    plt.savefig(graficapca)
    
    
    return graficapca 
"""
def PCA_puntos():
    base_dir =settings.MEDIA_ROOT
    Datos =os.path.join(base_dir, 'muestra/datos/archivoprueba2.txt')
    Xpca = np.loadtxt(Datos,skiprows=0)
     
    escala=MinMaxScaler()
    escala.fit(Xpca)
    escalada=escala.transform(Xpca)
    pca=PCA(n_components=2)
    pca.fit(escalada)
    transformada=pca.transform(escalada)
    
    return transformada

def Juntar(Xclasificadas,nuevas,Npuntos):
    f=len(Xclasificadas[:,0])
    Mclasi=np.zeros((f+Npuntos,2))
    Mclasi[0:f,:]=Xclasificadas
    for i in range(Npuntos):
        
        Mclasi[f+i,:]=nuevas[i-Npuntos,:]        
    
    return Mclasi

def PCA_SK(paciente,NomImag3):
    base_dir =settings.MEDIA_ROOT    
    Datos=os.path.join(base_dir, 'muestra/datos/archivoprueba2.txt')
    #Datos ="archivoprueba2.txt"
    grupo=os.path.join(base_dir, 'muestra/datos/grupo')
    grupo=np.loadtxt(grupo + ".txt", skiprows=0)
    Xpca = np.loadtxt(Datos,skiprows=0)
    #grupo =np.loadtxt("grupo.txt",skiprows=0)
    
    Xpca1=np.copy(Xpca)
    try:
        c=len(paciente[:,0])
    except:
        c=1
    for j in range(c):
        try:
            pacien=paciente[j,:]
        except:
            pacien=paciente
        grupo=np.append(grupo, 0)
        Xpca1=np.insert(Xpca1, Xpca1.shape[0], np.array(pacien), 0)
    
    escala=MinMaxScaler()
    escala.fit(Xpca1)
    escalada=escala.transform(Xpca1)
    pca=PCA(n_components=2)
    pca.fit(escalada)
    transformada=pca.transform(escalada)
    
    A=PCA_puntos()
    clasificadas=Juntar(A,transformada,c)
    
    graficapca=Plot_PCA(transformada,grupo,NomImag3)
    #graficapca=Plot_PCA(clasificadas,grupo)
        
    return graficapca


   
