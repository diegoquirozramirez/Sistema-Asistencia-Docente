# Generated by Django 2.2.2 on 2019-06-04 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Docente', '0007_auto_20190604_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
