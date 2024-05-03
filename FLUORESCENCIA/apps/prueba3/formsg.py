from django import forms
from apps.prueba3.models import Image

#class ImageForm(forms.ModelForm):
#   class Meta:
#      model = Image
#      fields = ['image','name']

class ImageForm(forms.ModelForm):

   image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
   class Meta:
      model = Image
      fields = ['image']

