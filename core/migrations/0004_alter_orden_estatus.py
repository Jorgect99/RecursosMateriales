# Generated by Django 4.0 on 2022-01-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_departamento_idusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden',
            name='estatus',
            field=models.CharField(max_length=50, verbose_name='Estatus'),
        ),
    ]
