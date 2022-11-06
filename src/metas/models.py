from django.db import models

import metas.models


# Create your models here.
class CardsMeta (models.Model):
    titulo = models.CharField(max_length=500, blank=False)
    texto = models.CharField(max_length=1000, blank=False)
    imagem = models.CharField(max_length=100)
    botao = models.CharField(max_length=10, default="Ganhadores")

    class Meta:
        db_table='metas_usuarios'

    def _str_(self):
        return self.titulo


class CalculoMetas (models.Model):
    imagem = models.CharField(max_length=100)
    total = models.IntegerField ()

    class Meta:
        db_table = 'metas_totais'

    def _str_(self):
        return self.imagem

class Contas (models.Model):
    categoria = models.CharField(max_length=10)
    contador = models.IntegerField()
    texto = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)

    class Meta:
        db_table = 'contas'

    def _str_(self):
        return self.id