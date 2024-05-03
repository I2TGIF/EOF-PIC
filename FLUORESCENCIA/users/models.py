from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
#from django.contrib.auth import get_user_model
#User = get_user_model()



class User(AbstractUser):
    is_medical = models.BooleanField(default=False)
    is_investigador = models.BooleanField(default=False)
    is_personalsalud = models.BooleanField(default=False)
    def get_medical_profile(self):
        medical_profile = None
        if hasattr(self, 'medicalprofile'):
            medical_profile = self.medicalprofile
        return medical_profile

    def get_investigador_profile(self):
        investigador_profile = None
        if hasattr(self, 'investigadorprofile'):
            investigador_profile = self.investigadorprofile
        return investigador_profile

    def get_personalsalud_profile(self):
        personalsalud_profile = None
        if hasattr(self, 'personalsaludprofile'):
            personalsalud_profile = self.personalsaludprofile
        return personalsalud_profile
    class Meta:
        db_table = 'auth_user'


class MedicalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)


class investigadorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)


class personalsaludProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    name = models.CharField(max_length=64)