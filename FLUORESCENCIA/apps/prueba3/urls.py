from django.urls import path
from django.urls import include
from apps.prueba3.views import ingreso
from apps.prueba3.views import registro_lista
from apps.prueba3.views import editar_registro
from apps.prueba3.views import eliminar_registro
from apps.prueba3.views import patient, patient2
from apps.prueba3.views import sample, sample2
from apps.prueba3.views import spectrography, spectrography2
from apps.prueba3.views import delete_spectrography ,delete_spectrography2
from apps.prueba3.views import delete_sample, delete_sample2
from apps.prueba3.views import nopermiso
from apps.prueba3.views import resultado, notas_medicas, reporte,  notas_medicas2, resultado2
from . import views
from apps.prueba3.views import pdf, pdf2


urlpatterns = [
    path('formulario', ingreso, name='formulario'),
    path('registro', registro_lista, name='registro'),
    
    
    #path('borrar', borrar_registro),
    path('editar/<int:id_registro>/' , editar_registro, name='edita'),
    path('eliminar/<int:id_registro>/' , eliminar_registro, name='elimina'),
    path('registro-patient/<int:id_registro>/', patient, name='patient'),
    path('registro-patient2/<int:id_registro>/', patient2, name='patient2'),
    path('registro-sample/<int:id_registro>/', sample, name='sample'),
    path('registro-sample2/<int:id_registro>/', sample2, name='sample2'),
    path('registro-reporte/<int:id_registro>/', reporte, name='reporte'),
    path('registro-notas_medicas/<int:id_registro>/', notas_medicas, name='notas_medicas'),
    path('registro-notas_medicas2/<int:id_registro>/', notas_medicas2, name='notas_medicas2'),
    path('registro-resultado/<int:id_registro>/', resultado, name='resultado'),
    path('registro-resultado2/<int:id_registro>/', resultado2, name='resultado2'),
    path('registro-spectrography/<int:id_registro>/', spectrography, name='spectrography'),
    path('registro-spectrography2/<int:id_registro>/', spectrography2, name='spectrography2'),
    path('registro-delete-spectrography/<int:id_registro>/', delete_spectrography, name='delete-spectrography'),
    path('registro-delete-sample/<int:id_registro>/', delete_sample, name='delete-sample'),
    path('registro-delete-spectrography2/<int:id_registro>/', delete_spectrography2, name='delete-spectrography2'),
    path('registro-delete-sample2/<int:id_registro>/', delete_sample2, name='delete-sample2'),
    path('nopermiso', nopermiso, name='nopermiso'),
    path('registro-pdf/<int:id_registro>/', pdf, name = 'pdf'),
    path('registro-pdf2/<int:id_registro>/', pdf2, name = 'pdf2'),
    ]