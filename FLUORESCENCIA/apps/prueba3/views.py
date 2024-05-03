from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import *
from django.conf import settings
from django.views.generic import View
from sklearn.cluster import KMeans
from sklearn.metrics.cluster import entropy
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from skimage.color import label2rgb
from pathlib import Path
from apps.prueba3.forms import prueba3formu, prueba3formu2
from apps.prueba3.formse import UploadFileForm, UploadFileForm1
from apps.prueba3.formsg import ImageForm
from apps.prueba3.models import IngresoPaciente, NotasMedicas, PCAgraf, Entrada, Entrada1, Image
from Procesamiento.PCA1 import PCA_SK, Plot_PCA
from Procesamiento.ImagenPROCESA import compANdrem, estrac, ProcesImag
from Procesamiento.prueba_2 import fun, SaveTXT, modificarLinea, Signal, plot
from apps.prueba3.utils import render_to_pdf
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
import pdb  


########################################################################
########   Lleva a la vista de no registro en caso de no cumplir #######
########   con la autentificación segun el rol de usuario.       #######
########################################################################
@login_required
def nopermiso(request):
    return render(request, 'base/nopermiso.html')

########################################################################
########   Permite ingresar un nueva paciente, muestra el        #######
########   formulario de ingreso y lo guarda.                    #######
########################################################################    
@login_required
def ingreso(request):
  if request.user.is_authenticated:  
    if request.method == 'POST':
        form = prueba3formu(request.POST)
        if form.is_valid():
           form.save()
           return redirect('welcome') ##cambiar solo a index,, prueba1:
        else:
          print(form.errors)
          return render(request,'Prueba3/formulario.html',{'form':form,})
    else:
        form = prueba3formu() 
    return render(request,'Prueba3/formulario.html',{'form':form,}) 
  return redirect('/login')

########################################################################
########   Permite listar los registros por orden de creación.   #######
########################################################################  
@login_required
def registro_lista(request):
  if request.user.is_authenticated:
    search_flag = False
    if request.GET.get('q'):
      search = request.GET.get('q', '')
      registro = IngresoPaciente.objects.filter(Q(Nombre__startswith=search) | Q(Apellido__startswith=search) | Q(DocumentoIdentificacion__startswith=search)).order_by('id')
      search_flag = True
      return render(request,'Prueba3/registro.html', {'registro':registro, 'search_flag':search_flag})
    registro = IngresoPaciente.objects.all().order_by('id')###para organizar por id
    return render(request,'Prueba3/registro.html', {'registro':registro, 'search_flag':search_flag})
  return redirect('/login')

########################################################################
########   Permite editar el registro de la paciente.            #######
########################################################################
@login_required  
def editar_registro(request, id_registro):
    registro = IngresoPaciente.objects.get(id=id_registro)
    if request.method == 'GET':
       form = prueba3formu(instance=registro)
    else:
        form = prueba3formu(request.POST,instance=registro)
        if form.is_valid():
         form.save()
        return redirect('/Paginaprincipal/registro') 
    
    return render(request,'Prueba3/formulario.html',{'form':form})  

########################################################################
########   Permite eliminar el registro de la paciente.          #######
######################################################################## 
@login_required  
def eliminar_registro(request, id_registro):
    registro = IngresoPaciente.objects.get(id=id_registro)
    if request.method == 'POST':
        registro.delete()
        return redirect('/Paginaprincipal/registro')
    
    return render(request,'Prueba3/eliminaregis.html',{'registro':registro})  
 
########################################################################
########   Ingresa al registro de la paciente si es médico       #######
########   o superusuario o retorna al template de no permiso    #######
########################################################################   
@login_required          
def patient(request, id_registro):
  user = request.user
  if user.is_medical or user.is_superuser:
    registro = IngresoPaciente.objects.get(id=id_registro)
    flag_result = Image.objects.filter(name = registro).exists()
    return render(request,'Prueba3/patient.html',{'registro':registro, 'flag_result':flag_result,})
  else :
    return redirect('/Paginaprincipal/nopermiso') 

########################################################################
########   Ingresa al registro de la paciente si es investigador #######
########   o superusuario o retorna al template de no permiso    #######
########################################################################
@login_required 
def patient2(request, id_registro):
  user = request.user
  if user.is_investigador or user.is_superuser:
    registro = IngresoPaciente.objects.get(id=id_registro)
    flag_result = Image.objects.filter(name = registro).exists()
    return render(request,'Prueba3/patient2.html',{'registro':registro,'flag_result':flag_result,})
  else :
    return redirect('/Paginaprincipal/nopermiso') 
  
##########################ROL MéDICO####################################
########   Permite subir la muestra de imagen videocolposcopica  #######
########   y guardarla. Llama a la función de procesamiento de   #######
########   imagen y retorna la dirección de la imagen procesada. #######
########################################################################
@login_required 
def sample(request, id_registro):
  image_flag = False
  registro = IngresoPaciente.objects.get(id=id_registro)
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      new_image = Image(image = form.cleaned_data["image"],    name = registro )
      new_image.save()
      image_flag = True
      base_dir = settings.MEDIA_ROOT    
      carpetaimagen=os.path.join(base_dir)
      fol=(carpetaimagen + "/")  
      #######llama a la imagen subida de la paciente          
      folder = fol+new_image.image.name    
      img = cv2.imread(folder)            
      imaBGR = cv2.resize(img, dsize=(250, 216), interpolation=cv2.INTER_CUBIC)
      fil,col,cap = imaBGR.shape          
      ProcesImag(carpetaimagen,imaBGR,fil,col,cap, new_image.image.name)
      #carpeta donde esta la imagen
      base_dir =settings.MEDIA_URL 
      FoldSave=os.path.join(base_dir)
      #####GUARDAR LAS NUEVAS IMAGENES PROCESADAS
      folder = FoldSave + "/"+ 'procesada' + new_image.image.name
      img = cv2.imread(folder)
      path_image_processing = new_image.image.name.replace('gallery/','')
      new_image_processing = Image(image = 'procesadagallery/' + path_image_processing, name = registro )
      new_image_processing.save()
      images = Image.objects.filter(name = registro)
      return redirect('sample', id_registro = id_registro)   
  else:
    form = ImageForm()    
  if Image.objects.filter(name = registro).exists():
    image_flag = True
    images = Image.objects.filter(name = registro)
    return render(request,'Prueba3/sample.html',{'registro':registro, 'form': form,'images': images, 'image_flag': image_flag})
  return render(request,'Prueba3/sample.html',{'registro':registro, 'form': form, 'image_flag': image_flag})


########################ROL INVESTIGADOR################################
########   Permite subir la muestra de imagen videocolposcopica  #######
########   y guardarla. Llama a la función de procesamiento de   #######
########   imagen y retorna la dirección de la imagen procesada. #######
########################################################################
@login_required 
def sample2(request, id_registro):
  image_flag = False
  registro = IngresoPaciente.objects.get(id=id_registro)
  if request.method == 'POST':
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
      new_image = Image(image = form.cleaned_data["image"],    name = registro )
      new_image.save()
      image_flag = True
      base_dir = settings.MEDIA_ROOT    
      carpetaimagen=os.path.join(base_dir)
      fol=(carpetaimagen + "/")  
      #######llama a la imagen subida de la paciente          
      folder = fol+new_image.image.name    
      img = cv2.imread(folder)            
      imaBGR = cv2.resize(img, dsize=(250, 216), interpolation=cv2.INTER_CUBIC)
      fil,col,cap = imaBGR.shape          
      ProcesImag(carpetaimagen,imaBGR,fil,col,cap, new_image.image.name)
      #carpeta donde esta la imagen
      base_dir =settings.MEDIA_URL 
      FoldSave=os.path.join(base_dir)
      #####GUARDAR LAS NUEVAS IMAGENES PROCESADAS
      folder = FoldSave + "/"+ 'procesada' + new_image.image.name
      img = cv2.imread(folder)
      path_image_processing = new_image.image.name.replace('gallery/','')
      new_image_processing = Image(image = 'procesadagallery/' + path_image_processing, name = registro )
      new_image_processing.save()
      images = Image.objects.filter(name = registro)
      return redirect('sample2', id_registro = id_registro)   
  else:
    form = ImageForm()    
  if Image.objects.filter(name = registro).exists():
    image_flag = True
    images = Image.objects.filter(name = registro)
    return render(request,'Prueba3/sample2.html',{'registro':registro, 'form': form,'images': images, 'image_flag': image_flag})
  return render(request,'Prueba3/sample2.html',{'registro':registro, 'form': form, 'image_flag': image_flag})

########################ROL MEDICO######################################
########   Permite subir los archivos de espectroscopia de       #######
########   fluorescencia y conectar con la función encarga-      #######
########   del procesamiento espectral y PCA.  Retorna las       #######
########   graficas de la descomposición por punto de analisis   #######
########   y la clasificación.                                   #######
########################################################################


@login_required 
def spectrography(request, id_registro):
  registro = IngresoPaciente.objects.get(id=id_registro)
  process_flag = False
  file_present = False
  form_file = UploadFileForm()
  form3 = UploadFileForm1()
  if Entrada.objects.filter(Nombre_Paciente = registro).count() > 0:
    file_present = True 
  if request.method == 'POST':
    form3 = UploadFileForm1(request.POST)
    form_file = UploadFileForm(request.POST, request.FILES)
    files = request.FILES.getlist('document')
    if form_file.is_valid():
      #Entrada.objects.filter(Nombre_Paciente = registro).delete()
      for f in files:
        new_image = Entrada( document = f, Nombre_Paciente = registro )
        new_image.save()
      folder = Entrada.objects.filter(Nombre_Paciente = registro)
      field_name = f.name
      file_present = True
      return render(request,'Prueba3/spectrography.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})
    if form3.is_valid():
      if file_present:
        file_name = Entrada.objects.filter(Nombre_Paciente = registro)[0].document.name
        file_name = file_name.replace('.txt','')
        file_name = file_name.replace('muestra/','')
        file_name = file_name.replace('00001','')           
        new = Entrada1( Numero_espectros=form3.cleaned_data["Numero_espectros"] )
        new.save()   
        field_name1 = 'Numero_espectros'
        obj = Entrada1.objects.last()
        field_value1 = getattr(obj, field_name1)
        Muestra = file_name
        NumEsp = field_value1
        carpeta = "muestra"
        num = 1
        try:
          Nfolder = "media\muestra\datos"
          Nfolder.mkdir(parents=True)
          Nfolder = "media\muestra\imagenes"
          Nfolder.mkdir(parents=True)
        except: 
          pass
        NomDat = "media\muestra\datos\Datos"
        j,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,SumGauss=Signal(carpeta,Muestra,NumEsp,num,Nfolder,NomDat)
        base_dir =settings.MEDIA_URL
        NomImag = base_dir +'muestra/imagenes/imagen'
        count_images = plot(j,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,NomImag,SumGauss)
        process_flag = True
        return render(request,'Prueba3/spectrography.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag,'count_images': range(count_images),'NomImag': NomImag, 'file_present': file_present})
      else:
        return render(request,'Prueba3/spectrography.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})
    else:
      return render(request,'Prueba3/spectrography.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})
  else:
    return render(request,'Prueba3/spectrography.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})

########################ROL INVESTIGADOR################################
########   Permite subir los archivos de espectroscopia de       #######
########   fluorescencia y conectar con la función encarga-      #######
########   del procesamiento espectral y PCA.  Retorna las       #######
########   graficas de la descomposición por punto de analisis   #######
########   y la clasificación.                                   #######
########################################################################
@login_required 
def spectrography2(request, id_registro):
  registro = IngresoPaciente.objects.get(id=id_registro)
  process_flag = False
  file_present = False
  form_file = UploadFileForm()
  form3 = UploadFileForm1()
  if Entrada.objects.filter(Nombre_Paciente = registro).count() > 0:
    file_present = True 
  if request.method == 'POST':
    form3 = UploadFileForm1(request.POST)
    form_file = UploadFileForm(request.POST, request.FILES)
    files = request.FILES.getlist('document')
    if form_file.is_valid():
      #Entrada.objects.filter(Nombre_Paciente = registro).delete()
      for f in files:
        new_image = Entrada( document = f, Nombre_Paciente = registro )
        new_image.save()
      folder = Entrada.objects.filter(Nombre_Paciente = registro)
      field_name = f.name
      file_present = True
      return render(request,'Prueba3/spectrography2.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})
    if form3.is_valid():
      if file_present:
        file_name = Entrada.objects.filter(Nombre_Paciente = registro)[0].document.name
        file_name = file_name.replace('.txt','')
        file_name = file_name.replace('muestra/','')
        file_name = file_name.replace('00001','')           
        new = Entrada1( Numero_espectros=form3.cleaned_data["Numero_espectros"] )
        new.save()   
        field_name1 = 'Numero_espectros'
        obj = Entrada1.objects.last()
        field_value1 = getattr(obj, field_name1)
        Muestra = file_name
        NumEsp = field_value1
        carpeta = "muestra"
        num = 1
        try:
          Nfolder = "media\muestra\datos"
          Nfolder.mkdir(parents=True)
          Nfolder = "media\muestra\imagenes"
          Nfolder.mkdir(parents=True)
        except: 
          pass
        NomDat = "media\muestra\datos\Datos"
        j,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,SumGauss=Signal(carpeta,Muestra,NumEsp,num,Nfolder,NomDat)
        base_dir =settings.MEDIA_URL
        NomImag = base_dir +'muestra/imagenes/imagen'
        count_images = plot(j,Gauss11,Gauss12,Gauss13,Gauss14,Gauss15,x1,yws,NomImag,SumGauss)
        process_flag = True
        return render(request,'Prueba3/spectrography2.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag,'count_images': range(count_images),'NomImag': NomImag, 'file_present': file_present})
      else:
        return render(request,'Prueba3/spectrography2.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})
    else:
      return render(request,'Prueba3/spectrography2.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})
  else:
    return render(request,'Prueba3/spectrography2.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})

########################ROL MEDICO#################################
########   Genera un formulario con los campos necesarios   #######
########   para que el medico coloque sus observaciones.    #######
###################################################################
@login_required 
def notas_medicas(request, id_registro):
    registro = IngresoPaciente.objects.get(id=id_registro)
    if request.method == 'POST':
        formN = prueba3formu2(request.POST)
        
        if formN.is_valid():
            formN.save()
            id_registro =str(id_registro)    
            A="/Paginaprincipal/registro-patient/"+ id_registro + "/"
            return redirect(A) ##cambiar solo a index,, prueba1:
        else:
            print(formN.errors)
            return render(request,'Prueba3/nota.html',{'formN':formN,'registro':registro,})
    else:
        formN = prueba3formu2()
        
    return render(request,'Prueba3/nota.html',{'formN':formN,'registro':registro}) 

########################ROL MEDICO#####################################
########   Genera un formulario con los campos necesarios       #######
########   para que el investigador coloque sus observaciones.  #######
#######################################################################
@login_required 
def notas_medicas2(request, id_registro):
    registro = IngresoPaciente.objects.get(id=id_registro)
    if request.method == 'POST':
        formN = prueba3formu2(request.POST)
        
        if formN.is_valid():
            formN.save()
            id_registro =str(id_registro)    
            A="/Paginaprincipal/registro-patient2/"+ id_registro + "/"
            return redirect(A) ##cambiar solo a index,, prueba1:
        else:
          #Imprime errores en la consola y renderiza el formulario con los campos de error
            print(formN.errors)
            return render(request,'Prueba3/nota2.html',{'formN':formN,'registro':registro,})
    else:
        formN = prueba3formu2()
        
    return render(request,'Prueba3/nota2.html',{'formN':formN,'registro':registro}) 


@login_required 
def resultado2(request, id_registro):
    
    registro = IngresoPaciente.objects.get(id=id_registro)
    
    nota= NotasMedicas.objects.last()
    image_flag = False
    process_flag = False
    if Image.objects.filter(name = registro).exists():
        image_flag = True
        process_flag = True
        images = Image.objects.filter(name = registro)
        images5= Image.objects.filter(name = registro).last().image.name
        n=1
        base_dir =settings.MEDIA_URL    
        #breakpoint()    
        images7 = (base_dir + images5 )
    
        images3, graficapca, NomImag4,n = PCAF(id_registro)
        return render(request, 'Prueba3/resultados2.html',{'nota':nota,'image_flag':image_flag,'process_flag':process_flag,'registro':registro,'images7':images7,'n':range(n),'NomImag4':NomImag4,})
    else:
      #return render(request, 'Prueba3/resultados2.html',{'nota':nota,'image_flag':image_flag,'process_flag':process_flag,'registro':registro,'n':range(n),'NomImag4':NomImag4,})
      return redirect('/Paginaprincipal/nopermiso')




@login_required 
def resultado(request, id_registro):
    registro = IngresoPaciente.objects.get(id=id_registro)
    nota= NotasMedicas.objects.last()
    image_flag = False
    process_flag = False
    if Image.objects.filter(name = registro).exists():
        image_flag = True
        process_flag = True
        images = Image.objects.filter(name = registro)
        images5= Image.objects.filter(name = registro).last().image.name
        n=1
        #breakpoint()
        #images5 = images5.replace('E:\\proyecto_fluo\\fluorescencia\\media/procesadagallery/','') 
        base_dir =settings.MEDIA_URL       
        images7 = (base_dir + images5 )
        images3, graficapca, NomImag4,n = PCAF(id_registro)
        return render(request, 'Prueba3/resultados.html',{'nota':nota,'image_flag':image_flag,'process_flag':process_flag,'registro':registro,'images7':images7,'n':range(n),'NomImag4':NomImag4,})
    else:
      #return render(request, 'Prueba3/resultados2.html',{'nota':nota,'image_flag':image_flag,'process_flag':process_flag,'registro':registro,'n':range(n),'NomImag4':NomImag4,})
      return redirect('/Paginaprincipal/nopermiso')


@login_required 
def delete_spectrography(request, id_registro):
  process_flag = False
  file_present = False
  form_file = UploadFileForm()
  form3 = UploadFileForm1()
  registro = IngresoPaciente.objects.get(id=id_registro)
  if Entrada.objects.filter(Nombre_Paciente = registro).count() > 0:
    Entrada.objects.filter(Nombre_Paciente = registro).delete()
  return render(request,'Prueba3/spectrography.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})


@login_required 
def delete_sample(request, id_registro):
  image_flag = False
  form = ImageForm()
  registro = IngresoPaciente.objects.get(id=id_registro)
  if Image.objects.filter(name = registro).exists():
    Image.objects.filter(name = registro).delete()
  return render(request,'Prueba3/sample.html',{'registro':registro, 'form': form, 'image_flag': image_flag})

@login_required 
def delete_spectrography2(request, id_registro):
  process_flag = False
  file_present = False
  form_file = UploadFileForm()
  form3 = UploadFileForm1()
  registro = IngresoPaciente.objects.get(id=id_registro)
  if Entrada.objects.filter(Nombre_Paciente = registro).count() > 0:
    Entrada.objects.filter(Nombre_Paciente = registro).delete()
  return render(request,'Prueba3/spectrography2.html',{'registro':registro, 'form_file': form_file, 'form3':form3, 'process_flag': process_flag, 'file_present': file_present})

@login_required 
def delete_sample2(request, id_registro):
  image_flag = False
  form = ImageForm()
  registro = IngresoPaciente.objects.get(id=id_registro)
  if Image.objects.filter(name = registro).exists():
    Image.objects.filter(name = registro).delete()
  return render(request,'Prueba3/sample2.html',{'registro':registro, 'form': form, 'image_flag': image_flag})

@login_required 
def reporte(request, id_registro):
    registro2 = IngresoPaciente.objects.get(id=id_registro)
    nota2= NotasMedicas.objects.last()
    image_flag2 = False
    process_flag2 = False
    if Image.objects.filter(name = registro2).exists():
      image_flag2 = True
      process_flag2 = True
      images = Image.objects.filter(name = registro2)
      images5= Image.objects.filter(name = registro2).last().image.name
      n2=1
      #breakpoint()
      #images5 = images5.replace('E:\\proyecto_fluo\\fluorescencia\\media/procesadagallery/','') 

      base_dir =settings.MEDIA_URL    
      #breakpoint()    
      images8 = (base_dir + images5 )
    images3, graficapca, NomImag4,n = PCAF(id_registro)
    return render(request,'Prueba3/reporte.html',{'nota2':nota2,'image_flag2':image_flag2,'process_flag2':process_flag2,'registro2':registro2,'images8':images8,'n2':range(n2),'NomImag4':NomImag4,})

def PCAF (id_registro):
    #pdb.set_trace()
    registro = IngresoPaciente.objects.get(id=id_registro)
    #breakpoint()
    Atributo = id_registro
    base_dir =settings.MEDIA_ROOT   
    paciente =os.path.join(base_dir, 'muestra/datos/Datos_Paciente')
    #paciente=os.path.join(base_dir, 'muestra/datos/Daryeni_param')
    #plt.savefig(NomImag +st) +".jpg")
    
    paciente_txt = np.loadtxt(paciente + ".txt")  
    base_dir =settings.MEDIA_ROOT
    NomImag3 = os.path.join(base_dir, 'muestra/imagenes1/imagen'+ str(Atributo) ) 
    graficapca= PCA_SK(paciente_txt,NomImag3)
    images3 = 1 #PCAgraf.objects.filter(name3 = registro).first()
    #breakpoint()
    images3 = 1 #images3.image3.name se deberia eleiminar images 3 no se esta usando 
    base_dir =settings.MEDIA_URL            
    NomImag4 = os.path.join(base_dir, 'muestra/imagenes1/imagen'+ str(id_registro) ) 
    n=1   
    return images3, graficapca, NomImag4,n


    

######PDF ##############



def pdf(request,id_registro):
    #breakpoint()
    #########################################################################
    image_flag2 = False
    process_flag2 = False
    registro2 = IngresoPaciente.objects.get(id=id_registro)
    nota2= NotasMedicas.objects.last()
    
    if Image.objects.filter(name = registro2).exists():
        image_flag2 = True
        process_flag2 = True
        images = Image.objects.filter(name = registro2)
        images5= Image.objects.filter(name = registro2).last().image.name
        n2=1
        #breakpoint()
        #images5 = images5.replace('E:\\proyecto_fluo\\fluorescencia\\media/procesadagallery/','') 

        base_dir =settings.MEDIA_URL    
        #breakpoint()    
        images8 = (base_dir + images5 )
        images3, graficapca, NomImag4,n = PCAF(id_registro)
    


        data = {'nota2':nota2,'image_flag2':image_flag2,'process_flag2':process_flag2,'registro2':registro2,'images8':images8,'n2':range(n2),'NomImag4':NomImag4,}  
        pdf = render_to_pdf('prueba3/reporte.html', data)
    #html  = 
        return HttpResponse(pdf, content_type='apps/pdf')
    else:
      #return render(request, 'Prueba3/resultados2.html',{'nota':nota,'image_flag':image_flag,'process_flag':process_flag,'registro':registro,'n':range(n),'NomImag4':NomImag4,})
      return redirect('/Paginaprincipal/nopermiso')



def pdf2(request,id_registro):
    #breakpoint()
    #########################################################################
    image_flag2 = False
    process_flag2 = False
    registro2 = IngresoPaciente.objects.get(id=id_registro)
    nota2= NotasMedicas.objects.last()
    
    if Image.objects.filter(name = registro2).exists():
        image_flag2 = True
        process_flag2 = True
        images = Image.objects.filter(name = registro2)
        images5= Image.objects.filter(name = registro2).last().image.name
        n2=1
        #breakpoint()
        #images5 = images5.replace('E:\\proyecto_fluo\\fluorescencia\\media/procesadagallery/','') 

        base_dir =settings.MEDIA_URL    
        #breakpoint()    
        images8 = (base_dir + images5 )
        images3, graficapca, NomImag4,n = PCAF(id_registro)
    


        data = {'nota2':nota2,'image_flag2':image_flag2,'process_flag2':process_flag2,'registro2':registro2,'images8':images8,'n2':range(n2),'NomImag4':NomImag4,}  
        pdf = render_to_pdf('prueba3/reporte2.html', data)
    #html  = 
        return HttpResponse(pdf, content_type='apps/pdf')
    else:
      #return render(request, 'Prueba3/resultados2.html',{'nota':nota,'image_flag':image_flag,'process_flag':process_flag,'registro':registro,'n':range(n),'NomImag4':NomImag4,})
      return redirect('/Paginaprincipal/nopermiso')


