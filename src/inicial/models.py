from django.db import models

# Create your models here.
class Sorteio(models.Model):
    titulo = models.CharField(max_length=1000, blank=False)
    imagem = models.CharField(max_length=1000, blank=False, unique=True)
    tamanho = models.CharField(max_length=10)

    class Meta:
        db_table='sorteio'

    def _str_(self):
        return self.imagem

class Noticia(models.Model):
    titulo = models.CharField(max_length=5000, unique=True)
    identificador = models.CharField(max_length=5000, unique=True)
    texto = models.CharField(max_length=5000, unique=True)
    data = models.CharField(max_length=1000)
    imagem = models.CharField(max_length=1000)
    tamanho = models.CharField(max_length=10)
    ativo = models.BooleanField(default=False)
    margin = models.BooleanField(default=False)

    class Meta:
        db_table='noticia'

    def _str_(self):
        return self.titulo


class Carrossel(models.Model):
    imagem = models.CharField(max_length=1000)
    ativo = models.BooleanField(default=False)


    class Meta:
        db_table='carrosel'

    def _str_(self):
        return self.imagem





