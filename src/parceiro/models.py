from django.db import models

from categoria.models import Categoria


class Parceiro (models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    categoria =models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=50)
    imagem = models.CharField(max_length=100)

    class Meta():
        db_table='parceiro'

    def __str__(self):
        return self.nome