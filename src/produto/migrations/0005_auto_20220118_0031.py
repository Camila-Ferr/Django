# Generated by Django 3.0.2 on 2022-01-18 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_auto_20220116_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
