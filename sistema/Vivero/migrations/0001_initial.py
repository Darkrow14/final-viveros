# Generated by Django 4.2.1 on 2023-05-19 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Productor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_departamento', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
            },
        ),
        migrations.CreateModel(
            name='Vivero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=60)),
                ('municipio', models.CharField(max_length=60)),
                ('codigo', models.IntegerField(unique=True)),
                ('nombre_vivero', models.CharField(max_length=60)),
                ('productor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productor.productor')),
            ],
            options={
                'verbose_name': 'vivero',
                'verbose_name_plural': 'viveros',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_municipio', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=10)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vivero.departamento')),
            ],
            options={
                'verbose_name': 'municipio',
                'verbose_name_plural': 'municipios',
            },
        ),
    ]