# Generated by Django 5.0.4 on 2024-05-19 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca_api', '0002_alter_libro_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='fecha_caducidad',
            field=models.DateField(blank=True, null=True),
        ),
    ]
