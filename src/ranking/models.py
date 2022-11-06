from django.db import models

# Create your models here.
class Ranking (models.Model):
    posicao = models.IntegerField(unique=True,primary_key=True)
    titulo = models.CharField(max_length=1000, blank=False, unique=True)
    autor = models.CharField(max_length=1000, blank=False)
    genero = models.CharField(max_length=1000)
    imagem = models.CharField(max_length=1000)
    classificacao = models.FloatField()
    metade = models.BooleanField(default=False)

    class Meta:
        db_table='top10'

    def _str_(self):
        return self.imagem

class Lista (models.Model):
    titulo = models.CharField(max_length=1000, blank=False, unique=True)
    ativo = models.BooleanField(default=False)
    class Meta:
        db_table='lista'
    def _str_(self):
        return self.titulo
