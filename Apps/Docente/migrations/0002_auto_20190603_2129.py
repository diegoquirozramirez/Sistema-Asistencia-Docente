# Generated by Django 2.2.2 on 2019-06-04 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='h_entrada',
            field=models.DateField(max_length=50),
        ),
        migrations.AlterField(
            model_name='horario',
            name='h_salida',
            field=models.DateField(max_length=50),
        ),
    ]
