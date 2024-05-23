# Generated by Django 5.0.4 on 2024-05-22 15:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_api', '0004_alter_prestamo_fecha_caducidad'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariobiblioteca',
            name='id_bibliotecario',
        ),
        migrations.AddField(
            model_name='usuariobiblioteca',
            name='id_bibliotecario',
            field=models.ManyToManyField(related_name='bibliotecario', to=settings.AUTH_USER_MODEL),
        ),
    ]
