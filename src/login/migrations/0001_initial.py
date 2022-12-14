# Generated by Django 4.1.3 on 2022-12-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Divulgacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=1000)),
                ('texto', models.CharField(max_length=5000)),
                ('titulo_inscricao', models.CharField(max_length=1000)),
                ('texto_inscricao', models.CharField(max_length=10000)),
                ('imagem', models.CharField(max_length=10000)),
                ('botao', models.CharField(max_length=10000)),
            ],
            options={
                'db_table': 'concurso',
            },
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo', models.CharField(max_length=100)),
                ('placeholder', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'form',
            },
        ),
    ]
