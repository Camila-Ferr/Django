# Generated by Django 4.1.3 on 2022-12-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=1000, unique=True)),
                ('ativo', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'lista',
            },
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('posicao', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=1000, unique=True)),
                ('autor', models.CharField(max_length=1000)),
                ('genero', models.CharField(max_length=1000)),
                ('imagem', models.CharField(max_length=1000)),
                ('classificacao', models.FloatField()),
                ('metade', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'top10',
            },
        ),
    ]
