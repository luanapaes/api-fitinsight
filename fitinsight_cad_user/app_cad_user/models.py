from django.db import models

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    email = models.EmailField(max_length=255)
    senha = models.IntegerField()
    conf_senha = models.CharField(max_length=128)
