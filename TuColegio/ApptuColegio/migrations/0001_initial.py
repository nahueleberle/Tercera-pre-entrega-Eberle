# Generated by Django 5.0.3 on 2024-03-06 19:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colegios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mail', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cargaHoraria', models.IntegerField()),
                ('colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApptuColegio.colegios')),
            ],
        ),
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('colegio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApptuColegio.colegios')),
            ],
        ),
    ]