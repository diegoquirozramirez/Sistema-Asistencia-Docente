# Generated by Django 2.2.2 on 2019-06-07 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docente', '0012_auto_20190606_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='horaentrada',
            name='f_entrada',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
