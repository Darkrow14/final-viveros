# Generated by Django 4.2.1 on 2023-05-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Vivero", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="departamento",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="municipio",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="vivero",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]