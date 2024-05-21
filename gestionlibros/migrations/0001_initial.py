# Generated by Django 5.0.4 on 2024-05-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAutor', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('nacionalidad', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEditorial', models.IntegerField()),
                ('NombreEditorial', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idEstudiante', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fecharegistro', models.DateField()),
                ('fechaultimoprestamo', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPrestamo', models.IntegerField()),
                ('idAutor', models.IntegerField()),
                ('nombreLibro', models.CharField(max_length=30)),
                ('idEditorial', models.IntegerField()),
                ('FechaLanzamiento', models.DateField()),
                ('EstadoLibro', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPrestamo', models.IntegerField()),
                ('idEstudiante', models.IntegerField()),
                ('idLibro', models.IntegerField()),
                ('FechaPrestamo', models.DateField()),
            ],
        ),
    ]
