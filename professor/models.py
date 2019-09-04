from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
    idade = models.IntegerField()
    
    def __str__(self):
        return self.nome
