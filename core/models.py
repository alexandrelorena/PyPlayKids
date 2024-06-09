
from django.db import models
from django.contrib.auth.models import User

class Site(models.Model):
    url = models.URLField()

class Image(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    url = models.URLField()

# Usar o modelo de usuário embutido do Django:
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Adicionar campos adicionais do perfil do usuário, se necessário


