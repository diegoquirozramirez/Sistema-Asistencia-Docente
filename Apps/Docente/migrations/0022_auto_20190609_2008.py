# Generated by Django 2.2.2 on 2019-06-10 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docente', '0021_auto_20190609_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horario',
            name='f_digital',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
