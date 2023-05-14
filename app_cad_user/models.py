from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) 
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()

class Venda(models.Model):
    id_venda = models.AutoField(primary_key=True) 
    servico = models.TextField(max_length=255)
    valor = models.IntegerField()
    cliente = models.TextField(max_length=255)
    data = models.TextField(max_length=255)




