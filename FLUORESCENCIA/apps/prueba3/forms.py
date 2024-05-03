from django.forms import ModelForm
from django import forms
from apps.prueba3.models import IngresoPaciente, NotasMedicas
#from muestra.models import Datosmedicos


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import *
import datetime


class prueba3formu(forms.ModelForm):

    
    class Meta:
        model = IngresoPaciente

        fields = [
        'Departamento',
        'Municipio',
        'Zona',
        'DocumentoIdentificacion',
        'Nombre', 
        'Apellido',
        'EstadoCivil',
        'Edad', 
        'FechaNacimiento', 
        'Direccion', 
        'Telefono', 
        'Ocupacion', 
        'Escolaridad', 
        'Seguridadsocial',
        ##################
        'Partos', 
        'Edadprimerparto', 
        'Menarca', 
        'EdadinicioRS', 
        'Abortos', 
        'Gravidex', 
        'Paridad',
        'Vivos',
        'Metodo_Anticompceptivo', 
        'Fecha_ultimaMenstura',
        'CirugiaGinecologica',
        'ETS' ,
        'AntecedenteFami', 
        'Fuma' ,
        'ConsumoLicor',
        'Fecha_Primera_Atencion' ,
        'Citologia',
        'Fecha_Citologia', 
        'Colposcopia',
        'Control_citologico',
        'Control_colposcopico',
        'Biopsia',
        'Control_Histologico',
        'Tratamiento',
        'Fecha_tratamiento', 
        'Fecha_Ultimocontrol', 
        'Hallazgo_mama' ,
        
        
        ]

        help_texts ={

        'FechaNacimiento':'AAAA/MM/DD',
        'Fecha_ultimaMenstura':'AAAA/MM/DD',
        'Fecha_Primera_Atencion':'AAAA/MM/DD',
        'Fecha_Citologia':'AAAA/MM/DD',
        'Fecha_tratamiento':'AAAA/MM/DD',
        'Fecha_Ultimocontrol':'AAAA/MM/DD',
         
        }

        texts ={

        'Departamento': 'Departamento',
        'Municipio': 'Municipio',
        'Zona':'Zona',
        'DocumentoIdentificacion':'Documento de Identificacón',
        'Nombre': 'Nombre Completo', 
        }
        labels ={

        'Departamento': 'Departamento',
        'Municipio': 'Municipio',
        'Zona':'Zona',
        'DocumentoIdentificacion':'Documento de Identificacón',
        'Nombre': 'Nombres', 
        'Apellido': 'Apellido',
        'EstadoCivil':'Estado civil',
        'Edad':'Edad', 
        'FechaNacimiento':'Fecha de Nacimiento', 
        'Direccion':'Dirección', 
        'Telefono':'Teléfono', 
        'Ocupacion':'Ocupación', 
        'Escolaridad':'Escolaridad', 
        'Seguridadsocial':'Tipo Seguridad Social',
        #########################
        'Partos' : 'Número de Partos', 
        'Edadprimerparto':'Edad Primer Parto', 
        'Menarca': 'Edad Primera Menstruación',
        'EdadinicioRS':'Edad Inicio Relaciones Sexuales', 
        'Abortos': 'Número de Abortos',
        'Gravidex': 'Gravidex',
        'Paridad':'Paridad',
        'Vivos':'Vivos',
        'Metodo_Anticompceptivo':'Método Anticonceptivo', 
        'Fecha_ultimaMenstura': 'Fecha Última Mestruación',
        'CirugiaGinecologica': '¿Ha tenido una cirugia ginecologica?',
        'ETS' : 'ETS',
        'AntecedenteFami': 'Antecendentes Familiares',
        'Fuma' : '¿Es fumadora?',
        'ConsumoLicor': '¿Consume licor?',
        'Fecha_Primera_Atencion' : 'Fecha Primera Atención' ,
        'Citologia': 'Citologia',
        'Fecha_Citologia' : 'Fecha Citologia' ,
        'Colposcopia': 'Colposcopia ',
        'Control_citologico' : 'Control Citologico',
        'Control_colposcopico' : 'Control Colposcopico',
        'Biopsia' : 'Biopsia ',
        'Control_Histologico': 'Control Histologico ',
        'Tratamiento': 'Tratamiento ',
        'Fecha_tratamiento' : 'Fecha tratamiento',
        'Fecha_Ultimocontrol' : 'Fecha Ultimo Control' ,
        'Hallazgo_mama': 'Hallazgo en mama' ,
        
        
        }
    
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
                ('Sunsidiado', 'Subsidiado'),
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
         
   
        cito = (
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
        control1 = (
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
        
         
        Widgets = {

        'Departamento': forms.TextInput(attrs={'class':'form-control'}), 
        'Municipio' : forms.TextInput(attrs={'class':'form-control'}), 
        'Zona': forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=zonas)),
        'DocumentoIdentificacion' : forms.TextInput(attrs={'class':'form-control'}),  
        'Nombre' : forms.TextInput(attrs={ 'placeholder': 'Enter sender name'}),
        'Apellido' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter sender name'}), 
        'EstadoCivil' : forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=escivil)),
        'Edad' : forms.TextInput(attrs={'class':'form-control'}),  
        #'FechaNacimiento' : forms.SelectDateWidget(empty_label="Nothing"),
        'FechaNacimiento' : forms.TextInput(attrs={'class':'form-control'}),
        'Direccion' : forms.TextInput(attrs={'class':'form-control'}), 
        'Telefono': forms.TextInput(attrs={'class':'form-control'}),  
        'Ocupacion' : forms.TextInput(attrs={'class':'form-control'}), 
        'Escolaridad' : forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=Escolaridad)),
        'Seguridadsocial' : forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=seguridad)),
        'Partos': forms.TextInput(attrs={'class':'form-control'}),
        'Edadprimerparto' : forms.TextInput(attrs={'class':'form-control'}),
        'Menarca' : forms.TextInput(attrs={'class':'form-control'}),
        'EdadinicioRS': forms.TextInput(attrs={'class':'form-control'}),
        'Abortos' : forms.TextInput(attrs={'class':'form-control'}),
        'Gravidex': forms.TextInput(attrs={'class':'form-control'}),
        'Paridad': forms.TextInput(attrs={'class':'form-control'}),
        'Vivos': forms.TextInput(attrs={'class':'form-control'}),
        'Metodo_Anticompceptivo': forms.TextInput(attrs={'class':'form-control'}),
        #'Fecha_ultimaMenstura' : forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input','data-target': '#datetimepicker1'}),
        'Fecha_ultimaMenstura' : forms.TextInput(attrs={'class':'form-control'}),
        'CirugiaGinecologica': forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=si)),
        'ETS' : forms.TextInput(attrs={'class':'form-control'}),
        'AntecedenteFami': forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=si)),
        'Fuma': forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=talvez)),
        'ConsumoLicor': forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=talvez)), 
        'Fecha_Primera_Atencion' :  forms.TextInput(attrs={'class':'form-control'}),
        'Citologia' : forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=cito)),
        'Fecha_Citologia'  : forms.TextInput(attrs={'class':'form-control'}),  
        'Colposcopia' : forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=colposcopi)),
        'Control_citologico': forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=control1)),
        'Control_colposcopico': forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=control2)),
        'Biopsia': forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=Bio)),
        'Control_Histologico' : forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=control3)),
        'Tratamiento' : forms.ChoiceField(label='Seleccione su genero', widget=forms.Select(choices=trata)),
        'Fecha_tratamiento' : forms.TextInput(attrs={'class':'form-control'}),  
        'Fecha_Ultimocontrol' : forms.TextInput(attrs={'class':'form-control'}),  
        'Hallazgo_mama' : forms.TextInput(attrs={'class':'form-control'}),  
        
        }
    def __init__(self, *args, **kwargs):
      super(prueba3formu, self).__init__(*args, **kwargs)
      
      #self.fields['Nombre'].widget.attrs['placeholder'] = ' Nombre Completo'

      #self.helper.layout = Layout( PrependedText('Nombre', '<i class="fa fa-envelope-o"></i>', placeholder="Enter Email Address"))
      #self.fields['FechaNacimiento'].widget = forms.SelectDateWidget(years=range(1920, datetime.datetime.now().year+1))
      #self.fields['Nombre'].label = ''
      self.helper = FormHelper()
      self.helper.layout = Layout( PrependedText('Nombre', '@', placeholder="username"), InlineField('Apellido', readonly=True))
      #self.helper.form_show_labels = False
      self.helper.form_show_help_texts = False

class prueba3formu2(forms.ModelForm):
    class Meta:
        model = NotasMedicas

        fields = ['Hallazgo_imagen',
        'Nota',]
        labels ={ 'Hallazgo_imagen': 'Hallazgo en imagen Videocolposcopica',
        'Nota' : 'Nota',}
        Widgets = {'Hallazgo_imagen' : forms.TextInput(attrs={'class':'form-control'}),  
        'Nota' : forms.TextInput(attrs={'class':'form-control', 'size': 40}),}
    