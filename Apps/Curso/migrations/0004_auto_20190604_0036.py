# Generated by Django 2.2.2 on 2019-06-04 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Curso', '0003_auto_20190603_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='aula',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='año',
            field=models.IntegerField(default=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='seccion',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='curso',
            name='turno',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]