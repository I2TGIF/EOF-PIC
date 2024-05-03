from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Row, Column
from crispy_forms.bootstrap import *
from crispy_forms.bootstrap import FormActions
from users.form import RegistroForm
from users.form2 import LoginForm
from users.models import User

import pdb  

def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "base/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

def about(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "base/about.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

#@login_required
@login_required 
def register(request):
     # Creamos el formulario de a   pdb.set_trace()
    user = request.user
    if user.is_superuser:
        form = RegistroForm
        #form = UserForm
        if request.method == "POST":
            # Añadimos los datos recibidos al formulario
            form = RegistroForm(data=request.POST)
            # Si el formulario es válido...
            if form.is_valid():

                # Creamos la nueva cuenta de usuario
                
                user = form.save()
                user.set_password(user.password)
                user.save()
                # Si el usuario se crea correctamente 
                if user is not None:
                    # Hacemos el login manualmente
                    do_login(request, user)
                    # Y le redireccionamos a la portada
            
                
                    return redirect('/')
    else :
        return redirect('/Paginaprincipal/nopermiso') 
    # Si llegamos al final renderizamos el formulario
    return render(request, "base/registers.html", {'form': form,})
    

def login(request):
    # Creamos el formulario de autenticación vacío
    #form = AuthenticationForm()
    form = LoginForm
    #pdb.set_trace()
    if request.method == "POST":
        
        # Añadimos los datos recibidos al formulario
        form = LoginForm(data = request.POST)
        
        # Si el formulario es válido...
        if form.is_valid():
            
        # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')
            else:
                form = LoginForm
                return render(request, "base/login.html", {'form': form})
    
    # Si llegamos al final renderizamos el formulario
    return render(request, "base/login.html", {'form': form})
    

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    # Redireccionamos a la portada
    return redirect('/')



#class LoginForm(AuthenticationForm):
   # class Meta:
   #     model = get_user_model()
    #    fields = ['username', 'password', 'is_medical', 'is_investigador', 'is_personalsalud', ]
     #   labels = {'is_medical' :'-- Medico',
      #   'is_investigador':'I-- Investigador',
       #  'is_personalsalud':'P-  Personal de la salud',}

 #   def __init__(self, *args, **kwargs):
  #    super(LoginForm, self).__init__(*args, **kwargs)
   #   self.helper = FormHelper()
    #  self.helper.layout = Layout(
     #     PrependedText('username', '<span class="fa fa-user"></span>'),
      #    PrependedText('password', '<i class="fas fa-key"></i>'),
          
         
     # )
      #self.helper.add_input(Submit('submit', 'Ingresar', css_class='btn btn-info sm'))

      
#class UserForm():

#class UserForm(RegistroForm):
#class UserForm(UserCreationForm):    
    
 #   def __init__(self, *args, **kwargs):

  #      super(UserForm, self).__init__(*args, **kwargs)
        
   #     self.helper = FormHelper()
    #    self.helper.layout = Layout(
     #       PrependedText('username', '<span class="fa fa-user"></span>'), #anteponer icono
      #      PrependedText('password1', '<i class="fas fa-key"></i>'),
       #     PrependedText('password2', '<i class="fas fa-key"></i>'),
            
            
        #)
       # self.form_show_help_texts = False
       # self.fields['username'].help_text = "Requerido. 150 carácteres como máximo."
       # self.fields['password1'].help_text = False
            

       # self.helper.add_input(Submit('submit', 'Registrar', css_class='btn btn-info-sm'))        
        
        
        