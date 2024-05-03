"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
#from proyecto1 import settings 
from proyecto1.settings import * ###cambie esto
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from users import views
from users.views import welcome
from users.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('prue/', include('apps.prueba3.urls')),
    path('Paginaprincipal/', include('apps.prueba3.urls'), name ='Inicio'),
    path('', views.welcome, name='welcome'),
    path('about', views.about, name='about'),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    ]



urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(production.MEDIA_URL, document_root=production.MEDIA_ROOT)
urlpatterns += static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)