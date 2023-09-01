from django.db import models

# Create your models here.

class Tarefa (models.Model):

    Estado = (
        ('fazendo','Fazendo'),
        ('feita','Feita')
    )

    Nome = models.CharField(max_length=100)
    Descricao = models.TextField()
    Status = models.CharField(
        max_length=15,
        choices= Estado,
    )
    criado_em = models.DateTimeField(auto_now_add=True)
    actualizado_em = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Nome
    