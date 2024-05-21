# Generated by Django 5.0.4 on 2024-05-18 15:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('nombres', models.CharField(help_text='Nombres del autor, este campo es obligatorio', max_length=30)),
                ('apellido_paterno', models.CharField(help_text='Apellido paterno del autor, este campo es obligatorio', max_length=30)),
                ('apellido_materno', models.CharField(help_text='Apellido materno del autor, este campo es obligatorio', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id_devolucion', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('fecha_devolucion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id_editorial', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id_genero', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=350, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id_nacionalidad', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('pais', models.CharField(max_length=50)),
                ('gentilicio', models.CharField(help_text='Ejemplo: peruano (a)', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('telefono', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id_libro', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('titulo', models.CharField(max_length=150)),
                ('anio_publicacion', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=350, null=True)),
                ('id_autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.autor')),
                ('id_bibliotecario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.genero')),
                ('id_proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='autor',
            name='id_nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.nacionalidad'),
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id_prestamo', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('fecha_prestamo', models.DateField()),
                ('id_bibliotecario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_devolucion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.devolucion')),
            ],
        ),
        migrations.CreateModel(
            name='DetallePrestamo',
            fields=[
                ('id_detalle_prestamo', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.libro')),
                ('id_prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.prestamo')),
            ],
        ),
        migrations.CreateModel(
            name='Publica',
            fields=[
                ('id_publica', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('id_editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.editorial')),
                ('id_libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.libro')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioBiblioteca',
            fields=[
                ('id_usuario', models.AutoField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('nombres', models.CharField(max_length=30)),
                ('apellido_paterno', models.CharField(max_length=30)),
                ('apellido_materno', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=150)),
                ('es_activo', models.BooleanField(default=True, verbose_name='usuario activo')),
                ('id_bibliotecario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='prestamo',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_api.usuariobiblioteca'),
        ),
    ]
