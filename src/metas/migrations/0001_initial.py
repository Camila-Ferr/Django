# Generated by Django 4.1.3 on 2022-12-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculoMetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
            ],
            options={
                'db_table': 'metas_totais',
            },
        ),
        migrations.CreateModel(
            name='CardsMeta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('texto', models.CharField(max_length=1000)),
                ('imagem', models.CharField(max_length=100)),
                ('botao', models.CharField(default='Ganhadores', max_length=10)),
            ],
            options={
                'db_table': 'metas_usuarios',
            },
        ),
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=10)),
                ('contador', models.IntegerField()),
                ('texto', models.CharField(max_length=100)),
                ('complemento', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'contas',
            },
        ),
    ]
