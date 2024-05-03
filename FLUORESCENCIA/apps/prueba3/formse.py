from django import forms
#class FileFieldForm(forms.Form):
#    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
from apps.prueba3.models import Entrada
from apps.prueba3.models import Entrada1
from crispy_forms.helper import FormHelper

from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.bootstrap import *



class UploadFileForm(forms.ModelForm):

   document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
   class Meta:
      model = Entrada
      fields = ['document',]
      #labels ={
      #'Nombre_Paciente': 'Nombre del Paciente','document': 'Muestras-Archivos TXT',}
      #Widgets = {'Nombre_Paciente': forms.TextInput(attrs={'class':'form-control'}), 
      #'document' : forms.TextInput(attrs={'class':'form-control'}), }

class UploadFileForm1(forms.ModelForm):
  _placeholders = {
        'Numero_espectros': 'Ingrese el número de espectros',
    }
  class Meta:
    model = Entrada1
    fields = ['descripcion',
    'Numero_espectros',]
    Widgets = {'descripcion': forms.TextInput(attrs={'class':'form-control'}), 
    'Numero_espectros' : forms.TextInput(attrs={'class':'form-control mb-0'}), }
  def __init__(self, *args, **kwargs):
    super(UploadFileForm1, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.form_show_help_texts = False
    
    self.fields['Numero_espectros'].label = ''
   
    self.fields['Numero_espectros'].widget.attrs['placeholder'] = \
    self._placeholders['Numero_espectros']



    
   

