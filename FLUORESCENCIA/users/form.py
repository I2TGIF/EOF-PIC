from django import forms

from users.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import MedicalProfile, investigadorProfile, personalsaludProfile

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column
from crispy_forms.bootstrap import *
from django.contrib.auth import get_user_model

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'is_medical', 'is_investigador', 'is_personalsalud', ]
        widgets = {
            'password': forms.PasswordInput() 
        }
        labels = {'is_medical' :' Medico',
         'is_investigador':' Investigador',
         'is_personalsalud':' Personal de la salud',}

    
    def __init__(self, *args, **kwargs):
      super(RegistroForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.layout = Layout(
            PrependedText('username', '<span class="fa fa-user"></span>'), #anteponer icono
            PrependedText('password', '<i class="fas fa-key"></i>'), 
            'Rol',
            TabHolder(
                Tab('Rol',
                   Column(
                    Row('is_medical', css_class='form-group col-md-12 mb-0'),
                    Row('is_investigador', css_class='form-group col-md-12 mb-0'),
                    Row('is_personalsalud', css_class='form-group col-md-12 mb-0'),
                    css_class='form-row'),
                ),
            )
            
        )

      self.form_show_help_texts = False
      self.fields['username'].help_text = "Requerido. 150 carácteres como máximo."
      self.fields['password'].help_text = False
      self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': ''})
      self.fields['password'].widget.attrs['class'] = 'form-control'
      self.fields['is_medical'].help_text = False
      self.helper.add_input(Submit('submit', 'Registrar', css_class='btn btn-info-sm'))


