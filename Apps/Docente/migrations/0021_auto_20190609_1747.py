# Generated by Django 2.2.2 on 2019-06-09 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Docente', '0020_auto_20190609_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='iduser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
