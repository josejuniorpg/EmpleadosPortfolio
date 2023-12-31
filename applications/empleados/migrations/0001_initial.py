# Generated by Django 4.2.2 on 2023-06-27 02:59

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0002_alter_departamento_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellido')),
                ('job', models.CharField(choices=[('0', 'Contador'), ('1', 'Administrador')], max_length=50, verbose_name='Trabajo')),
                ('hoja_vida', ckeditor.fields.RichTextField()),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.departamento')),
                ('habilidades', models.ManyToManyField(to='empleados.habilidades')),
            ],
            options={
                'verbose_name': 'Mi Empleado',
                'verbose_name_plural': 'Mis Empleados',
                'ordering': ['first_name'],
                'unique_together': {('first_name', 'departamento')},
            },
        ),
    ]
