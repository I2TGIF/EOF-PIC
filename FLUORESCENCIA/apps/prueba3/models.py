from django.db import models



class NotasMedicas(models.Model):
    Hallazgo_imagen = models.CharField(max_length=300, null=False,)

    Nota = models.CharField(max_length=300, null=False,)

# Create your models here.
 

class IngresoPaciente(models.Model):
    generos= (
         ('hetero', 'Heterosexual'),
         ('homo', 'Homosexual'),
         ('bi', 'Bisexual'),
         ('bi', 'Bisexual'),
 )
    zonas= (
         ('Rural', 'Rural'),
         ('Urbana', 'Urbana'),
 ) 

    escivil= (
         ('Soltera', 'Soltera'),
         ('Separada', 'Separada'),
         ('Unión Libre', 'Union Libre'),
         ('Viuda', 'Viuda'),
 ) 
    Escolaridad= (
         ('Primaria', 'Primaria'),
         ('Secundaria', 'Secundaria'),
         ('Tecnico', 'Tecnico'),
         ('Tecnologo', 'Tecnologo'),
         ('Universitaria', 'Universitaria'),
         ('Otro', 'Otro'),
 )
    seguridad= (
         ('Contributivo', 'Contributivo'),
         ('Sunsidiado', 'Subsiciado'),
         ('No afiliado', 'No afiliado'),
         ('No especifica', 'No especifica'),
 )
    si= (
         ('SI', 'SI'),
         ('NO', 'NO'),
 )
    talvez= (
         ('NO', 'NO'),
         ('Poco', 'Poco'),
         ('Mucho', 'Mucho'),

 )
    cito= (
                ('ACG','ACG'),    
                ('ASC - H', 'ASC - H'),
                ('ASC-US - VPH', 'ASC-US - VPH'),   
                ('ASC-US', 'ASC-US'),
                ('Cambios atrofia', 'Cambios atrofia'),
                ('Cambios indeterminados','Cambios indeterminados'),
                ('Cambios reactivos','Cambios reactivos'),
                ('Carcinoma invasivo','Carcinoma invasivo'),
                ('Displasia cervical','Displasia cervical'),
                ('Inflamatoria','Inflamatoria'),
                ('Inflamacion severa','Inflamacion severa'),
                ('Negativo neoplasia','Negativo neoplasia'),
                ('Leiomioma','Leiomioma'),
                ('LEI AG','LEI AG'),
                ('LEI AG - VPH','LEI AG - VPH'),
                ('LEI BG','LEI BG'),
                ('LEI BG - VPH','LEI BG - VPH'),
                ('Tricomonas','Tricomonas'),
                ('VPH','VPH'),
                ('Sin reporte','Sin reporte'),
                ('Sin dato','Sin dato'),         
    )
    control1= (
                ('ASC - US','ASC - US'),
                ('Atrofia','Atrofia'),
                ('Carcinoma escamocelular','Carcinoma escamocelular'),
                ('LEI AG','LEI AG'), ('LEI BG','LEI BG'),
                ('LEI BG -VPH','LEI BG -VPH'),
                ('Lesion Paracervical Extirpada','Lesion Paracervical Extirpada'),
                ('Negativo para neoplasia','Negativo para neoplasia'),
                ('Sin dato','Sin dato'), 
    ) 

    colposcopi= (
                ('Insatisfactoria típica','Insatisfactoria típica'),
                ('Insatisfactoria atípica','Insatisfactoria atípica'),
                ('Satisfactoria típica','Satisfactoria típica'),
                ('Satisfactoria atípica','Satisfactoria atípica'),
                ('Sin dato','Sin dato'), 
    ) 
    control2= (
                ('Insatisfactoria típica','Insatisfactoria típica'),
                ('Insatisfactoria atípica','Insatisfactoria atípica'),
                ('Satisfactoria típica','Satisfactoria típica'),
                ('Satisfactoria atípica','Satisfactoria atípica'),
                ('Sin dato','Sin dato'), 
    )
    Bio= (
                ('Carcinoma infiltrante','Carcinoma infiltrante'),      
                ('Carcinoma escamocelular no queratizante','Carcinoma escamocelular no queratizante'),        
                ('Carcinoma escamocelular','Carcinoma escamocelular'),        
                ('Cervicitis cronica - VPH','Cervicitis cronica - VPH'),        
                ('Cervicitis cronica - Polipo endocervical','Cervicitis cronica - Polipo endocervical'),       
                ('Coilocitosis - VPH','Coilocitosis - VPH'),      
                ('Displasia cervical leve','Displasia cervical leve'),        
                ('Displasia epitelial moderada','Displasia epitelial moderada'),        
                ('Endocervicitis cronica','Endocervicitis cronica'),       
                ('Histologicamente normal','Histologicamente normal'),        
                ('Hiperplasia sin atipias','Hiperplasia sin atipias'),        
                ('Negativo para neoplasia', 'Negativo para neoplasia'),        
                ('NICI', 'NICI'),        
                ('NICI - Coilocitosis', 'NICI - Coilocitosis'),       
                ('NICI - Coilocitosis - VPH','NICI - Coilocitosis - VPH'),        
                ('NICI - Polipo endocervical - VPH','NICI - Polipo endocervical - VPH'),        
                ('NICI - VPH','NICI - VPH'),        
                ('NICI - VPH - CC','NICI - VPH - CC'),        
                ('NICII','NICII'),        
                ('NICII - Coilocitosis', 'NICII - Coilocitosis'),        
                ('NICII - Coilocitosis - VPH','NICII - Coilocitosis - VPH'),        
                ('NICII - VPH','NICII - VPH'),        
                ('NICIII','NICIII'),        
                ('NICIII - Coilocitosis','NICIII - Coilocitosis'),        
                ('NICIII - Coilocitosis - VPH','NICIII - Coilocitosis - VPH'),        
                ('NICIII - VPH','NICIII - VPH'),        
                ('Polipo endocervical','Polipo endocervical'),        
                ('Polipo endocervical-cervicitis cronica','Polipo endocervical-cervicitis cronica') ,       
                ('Polipo edocervical - VPH','Polipo edocervical - VPH'),        
                ('VPH','VPH'),        
                ('VPH - Quiste de naboth', 'VPH - Quiste de naboth'),        
                ('Sin dato','Sin dato'),        
                ('Sin reporte', 'Sin reporte'), 
    )
    control3= (
                ('Carcinoma invasivo','Carcinoma invasivo'),
                ('Coilocitosis - VPH','Coilocitosis - VPH'),
                ('Compatible con cambios displasicos','Compatible con cambios displasicos'),
                ('Epitelio escamoso - coilocitosis','Epitelio escamoso - coilocitosis'),
                ('Material purulento cavidad uterina','Material purulento cavidad uterina'),
                ('Negativo para neoplasia','Negativo para neoplasia'),
                ('NICII','NICII'),
                ('NICII - Coilocitosis - VPH','NICII - Coilocitosis - VPH'),
                ('NICII - VPH','NICII - VPH'),
                ('NICI - VPH','NICI - VPH'),
                ('NICIII - VPH','NICIII - VPH'),
                ('Sin dato','Sin dato'),
    )

    trata= (
                ('Antibiotico','Antibiotico'),
                ('Baycuten','Baycuten'),
                ('Conizacion','Conizacion'),
                ('Clotrimazol','Clotrimazol'),
                ('Doxiciclina -metronidazol','Doxiciclina -metronidazol'),
                ('Fluconazol -gynoplus','Fluconazol -gynoplus'),
                ('Histerectomia','Histerectomia'),
                ('Hormonoterapia','Hormonoterapia'),
                ('Legrado endocervical','Legrado endocervical'),
                ('Metronidazol - Doxiciclina - Gentamicina','Metronidazol - Doxiciclina - Gentamicina'),
                ('Radioterapia','Radioterapia'),
                ('Topicacion con ATA','Topicacion con ATA'),
                ('Vaporizacion','Vaporizacion'),
                ('Vaporizacion -Levamisole','Vaporizacion -Levamisole'),
                ('No requiere','No requiere'),
                ('Sin dato','Sin dato'),
    )


 

    #folio = models.CharField(max_length=10, primary_key=True)
    ##datos generales
   
    Fecha_Primera_Atencion = models.CharField(null=False, max_length=50)
    Citologia =  models.CharField(max_length=50, choices=cito,null=False,)
    Fecha_Citologia = models.CharField(null=False, max_length=50)
    Colposcopia = models.CharField(max_length=200, choices=colposcopi, null=False,)
    Control_citologico = models.CharField(max_length=50, choices=control1, null=False,)
    Control_colposcopico = models.CharField(max_length=50, choices=control2, null=False,)
    Biopsia = models.CharField(max_length=50, choices=Bio, null=False,)
    Control_Histologico = models.CharField(max_length=50, choices=control3, null=False,)#models.FileField()
    #FechaNacimiento = models.DateField(max_length=50)
    Tratamiento = models.CharField(max_length=50, choices=trata, null=False,)

    Fecha_tratamiento = models.CharField(max_length=100, null=False,)
    Fecha_Ultimocontrol = models.CharField(max_length=100, null=False,)
    Hallazgo_mama = models.CharField(max_length=300, null=False,)

    #folio = models.CharField(max_length=10, primary_key=True)
    ##datos generales
    Departamento = models.CharField(null=True, max_length=50)
    Municipio =  models.CharField(max_length=50, null=True,)
    Zona = models.CharField(max_length=50, choices=zonas, null=True,)
    DocumentoIdentificacion = models.IntegerField(null=True)
    Nombre = models.CharField(max_length=50, null=True,)
    Apellido = models.CharField(max_length=50, null=True,)
    EstadoCivil = models.CharField(max_length=50, choices=escivil, null=True,)
    Edad = models.IntegerField(null=True) #models.FileField()
    #FechaNacimiento = models.DateField(max_length=50)
    FechaNacimiento = models.CharField(max_length=50, null=True,)
    Direccion = models.CharField(max_length=100, null=True,)
    Telefono = models.IntegerField(null=True)
    Ocupacion = models.CharField(max_length=50, null=True,)
    Escolaridad = models.CharField(max_length=50, choices=Escolaridad, null=True,)
    Seguridadsocial = models.CharField(max_length=50, choices=seguridad, null=True,)

    #datos medicos 
    Partos = models.IntegerField(null=True)
    Edadprimerparto = models.IntegerField(null=True)
    Menarca = models.CharField(max_length=50, null=True)
    EdadinicioRS = models.IntegerField(null=True)
    Abortos = models.IntegerField(null=True)
    Gravidex = models.CharField(max_length=50, null=True,)
    Paridad = models.CharField(max_length=50, null=True,)
    Vivos =  models.CharField(max_length=50, null=True,)
    Metodo_Anticompceptivo = models.CharField(max_length=50, null=True,)
    Fecha_ultimaMenstura = models.CharField(max_length=50, null=True,)
    CirugiaGinecologica = models.CharField(max_length=50, choices=si, null=True,)
    ETS = models.CharField(max_length=50, null=True,)
    AntecedenteFami = models.CharField(max_length=50, choices=si, null=True,)
    Fuma = models.CharField(max_length=50, choices=talvez, null=True,)
    ConsumoLicor = models.CharField(max_length=50, choices=talvez, null=True,)
    #############
    #image = models.ImageField()


class Image(models.Model):
   image = models.ImageField(upload_to = 'gallery') #, default 'gallery/static/images/no-img.jpg'
  # name = gato.Nombre
   name = models.ForeignKey(IngresoPaciente, on_delete=models.CASCADE, null=False, blank=False)
   uploaded_at = models.DateTimeField(auto_now_add=True)
   #name = models.ForeignKey('DocumentoIdentificacion', on_delete=models.CASCADE,)
# Create your models here.
   def _str_(self):
      return self.title

class Entrada(models.Model):
    Nombre_Paciente = models.ForeignKey(IngresoPaciente, on_delete=models.CASCADE, null=False, blank=False) # models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='muestra')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Entrada1(models.Model):
    Numero_espectros = models.IntegerField()
    #descripcion = models.ForeignKey(Entrada, on_delete=models.CASCADE, null=False, blank=False)

    descripcion = models.CharField(max_length=255, blank=True)

class PCAgraf(models.Model):
    image3 = models.ImageField(upload_to ='muestra') #, default 'gallery/static/images/no-img.jpg'
  # name = gato.Nombre
    name3 = models.ForeignKey(IngresoPaciente, on_delete=models.CASCADE, null=False, blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)



