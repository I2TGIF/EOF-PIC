from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm
from users.models import MedicalProfile, investigadorProfile, personalsaludProfile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column
from crispy_forms.bootstrap import *
from django.contrib.auth import get_user_model

class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'is_medical', 'is_investigador', 'is_personalsalud', ]
        labels = {'is_medical' :'-- Medico',
         'is_investigador':'I-- Investigador',
         'is_personalsalud':'P-  Personal de la salud',}

    def __init__(self, *args, **kwargs):
      super(LoginForm, self).__init__(*args, **kwargs)
      self.helper = FormHelper()
      self.helper.layout = Layout(
          PrependedText('username', '<span class="fa fa-user"></span>'),
          PrependedText('password', '<i class="fas fa-key"></i>'),
          
         
      )
      self.helper.add_input(Submit('submit', 'Ingresar', css_class='btn btn-info sm'))