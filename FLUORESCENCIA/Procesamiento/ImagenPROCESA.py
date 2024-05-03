import cv2
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import entropy
from skimage.color import label2rgb
from pathlib import Path
from django.conf import settings
import os
import mpld3

################################################################################################
################################################################################################
######################### Procesamiento de imágenes ############################################
#########################Algoritmos de segmentación ############################################
################################################################################################
################################################################################################

def compANdrem(A,M,com,rem):
    N=M
    for i in range(len(M[:,1,1])):
        for j in range(len(M[1,:,1])):
            for k in range(len(M[1,1,:])):
                if A[i,j] != com:
                    N[i,j,k]=rem
    return N

def estrac(ima_gray):
    DesEstandar2=np.zeros((27,25))
    Varianza2=np.zeros((27,25))
    media2=np.zeros((27,25))
    entropia2=np.zeros((27,25))
    for i in range(27):
        pos=0
        for j in range(25):
            DesEstandar=ima_gray[((i-1)*8)+1:(i*8),((j-1)*10)+1:(j*10)]
            DesEstandar1=((DesEstandar.T).ravel())
            
            if sum(DesEstandar1) != 0:
                PosNoCeros=np.where(DesEstandar1 != 0)[0]
                valor_real_des=[]
                for k in range(len(PosNoCeros)):
                    valor_real_des.append(DesEstandar1[PosNoCeros[k]]) 
            else:
                valor_real_des=0
            DesEstandar2[i,pos]=np.std(valor_real_des)
            #############################################
            Varianza=ima_gray[((i-1)*8)+1:(i*8),((j-1)*10)+1:(j*10)]
            Varianza1=((Varianza.T).ravel())
            
            if sum(Varianza1) != 0:
                PosNoCeros1=np.where(Varianza1 != 0)[0]
                valor_real_var=[]
                for k in range(len(PosNoCeros1)):
                    valor_real_var.append(Varianza1[PosNoCeros1[k]])
            else:
                valor_real_var=0
            Varianza2[i,pos]=np.var(valor_real_var)
            ###############################################
            media=ima_gray[((i-1)*8)+1:(i*8),((j-1)*10)+1:(j*10)]
            media1=((media.T).ravel())
            
            if sum(media1) != 0:
                PosNoCeros2=np.where(media1 != 0)[0]
                valor_real_media=[]
                for k in range(len(PosNoCeros2)):
                    valor_real_media.append(media1[PosNoCeros2[k]])
            else:
                valor_real_media=0
            media2[i,pos]=np.mean(valor_real_media)
            #################################################
            entropia=ima_gray[((i-1)*8)+1:(i*8),((j-1)*10)+1:(j*10)]
            entropia1=((media.T).ravel())
            
            if sum(entropia1) != 0:
                entropia2[i,pos]=entropy(entropia)
    
            else:
                entropia2[i,pos]=0
            
            pos += 1
        varianza_energia = Varianza2**2
        
    return DesEstandar2,Varianza2,media2,entropia2,varianza_energia


def ProcesImag(carpetaimagen,imaBGR,fil,col,cap, nombre_image):  #nomImagen  
    #fol=(carpetaimagen + "\ ")
    
    #folder=fol+"10853255647" + ".jpg"
    #img=cv2.imread(folder)
    #imaBGR = cv2.resize(img, dsize=(250, 216), interpolation=cv2.INTER_CUBIC)
    #fil,col,cap=imaBGR.shape
    
    imaLAB=cv2.cvtColor(imaBGR,cv2.COLOR_BGR2LAB)
    imaRGB=cv2.cvtColor(imaBGR,cv2.COLOR_BGR2RGB)
    ##############################################################
    
    c=imaLAB[:,:,1:3]
    ab=np.reshape(c,(fil*col,2))
    
    kmeans = KMeans(n_clusters=4, random_state=0,n_init=4).fit(ab)
    cluster_idx=kmeans.labels_
    cluster_centers=kmeans.cluster_centers_
    pixel_labels = np.reshape(cluster_idx,(fil,col))
    segmented_images = np.zeros((fil,col,3,4))
    rgb_label = pixel_labels
    color = np.array([imaRGB,imaRGB,imaRGB,imaRGB])
    
    for k in range(4):
        segmented_images[:,:,:,k]=compANdrem(rgb_label,color[k],k,0)
    
    segmented_images1=segmented_images[:,:,:,0]
    segmented_images2=segmented_images[:,:,:,1]
    segmented_images3=segmented_images[:,:,:,2]
    segmented_images4=segmented_images[:,:,:,3]
    
    ###########################################################
    
    segmented_images1=np.array (segmented_images1, dtype = np.uint8)
    segmented_images2=np.array (segmented_images2, dtype = np.uint8)
    segmented_images3=np.array (segmented_images3, dtype = np.uint8)
    segmented_images4=np.array (segmented_images4, dtype = np.uint8)
    im_interes1=cv2.cvtColor(segmented_images1,cv2.COLOR_RGB2GRAY)
    im_interes2=cv2.cvtColor(segmented_images2,cv2.COLOR_RGB2GRAY)
    im_interes3=cv2.cvtColor(segmented_images3,cv2.COLOR_RGB2GRAY)
    im_interes4=cv2.cvtColor(segmented_images4,cv2.COLOR_RGB2GRAY)
    
    des_standar1,varianza1,media1,entropia1,homogenidad1=estrac(im_interes1)
    des_standar2,varianza2,media2,entropia2,homogenidad2=estrac(im_interes2)
    des_standar3,varianza3,media3,entropia3,homogenidad3=estrac(im_interes3)
    des_standar4,varianza4,media4,entropia4,homogenidad4=estrac(im_interes4)
    ##########################################################
    
    prom= [np.max(media1.ravel()),np.max(media2.ravel()),np.max(media3.ravel()),np.max(media4.ravel())]
    posmin=np.where(prom == np.min(prom))[0]
    posmax=np.where(prom == np.max(prom))[0]
    
    cluster_interes=[]
    
    for i in range(4):
        if i != posmin:
            if i != posmax:
                cluster_interes.append(i)
                
    pos_interes=cluster_interes[0]
    pos_interes1=cluster_interes[1]
    
    if prom[pos_interes] > prom[pos_interes1]:
        pato=segmented_images[:,:,:,pos_interes]
        normal=segmented_images[:,:,:,pos_interes1]
    else:
        pato=segmented_images[:,:,:,pos_interes1]
        normal=segmented_images[:,:,:,pos_interes]
    
    pato=np.array (pato, dtype = np.uint8)
    normal=np.array (normal, dtype = np.uint8)
    patogray=cv2.cvtColor(pato,cv2.COLOR_RGB2GRAY)
    normalgray=cv2.cvtColor(normal,cv2.COLOR_RGB2GRAY)
    
    des_standar,varianza,media,entropia,homogenidad=estrac(patogray)
    des_standar0,varianza0,media0,entropia0,homogenidad0=estrac(normalgray)
    
    medpato=np.mean(media.ravel())
    mednor=np.mean(media0.ravel())
    im_pat=np.copy(patogray)
    
    rows=len(im_pat[:,1])
    cols=len(im_pat[1,:])
    
    for i in range(rows):
        for j in range(cols):
            if im_pat[i,j]>0:
                im_pat[i,j]=255
            else:
                 im_pat[i,j]=0
    
    im_pat=np.array(im_pat, dtype = np.uint8)
    Lrgb=label2rgb(im_pat,image=imaRGB,colors=[(1,0,0),(10,0,0)],)
    
    Lrgb2=np.zeros((fil,col,3))
    Lrgb2[:,:,0]=Lrgb[:,:,2]*255
    Lrgb2[:,:,1]=Lrgb[:,:,1]*255
    Lrgb2[:,:,2]=Lrgb[:,:,0]*215
    Lrgb2=np.array (Lrgb2, dtype = np.uint8)

    base_dir =settings.MEDIA_ROOT    
    FoldSave=os.path.join(base_dir)

    
    
    #FoldSave=(carpeta +"\Imagenes_Cuello\ ")
    #cv2.imwrite(FoldSave + nomImagen + '.jpg', imaBGR)
    cv2.imwrite(FoldSave + "/"+ 'procesada' + nombre_image, Lrgb2)

   



#carpeta="media" #"cedula_nombre"  #carpeta de la paciente (donde se guardaran las imagenes)
#nomImagen="1085325647"
#carpetaimagen="gallery" #carpeta donde esta la imagen
#ProcesImag(carpetaimagen,nomImagen,carpeta)

