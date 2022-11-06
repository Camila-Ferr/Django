from django.db import models

# Create your models here.
class Divulgacao (models.Model):
    titulo = models.CharField(max_length=1000, blank=False)
    texto = models.CharField(max_length=5000, blank=False)
    titulo_inscricao = models.CharField(max_length=1000, blank=False)
    texto_inscricao= models.CharField(max_length=10000, blank=False)
    imagem = models.CharField(max_length=10000, blank=False)
    botao = models.CharField(max_length=10000, blank=False)

    class Meta:
        db_table='concurso'

    def _str_(self):
        return self.titulo

class Formulario (models.Model):
    campo = models.CharField(max_length=100, blank=False)
    placeholder = models.CharField(max_length=100, blank=False)
    nome = models.CharField(max_length=100, blank=False)

    class Meta:
        db_table='form'

    def _str_(self):
        return self.id
