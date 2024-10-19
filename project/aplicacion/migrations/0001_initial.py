# Generated by Django 4.2.16 on 2024-10-18 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Libros",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                ("autor", models.CharField(max_length=100)),
                ("publicacion", models.DateField()),
                ("isbn", models.CharField(max_length=13, unique=True)),
            ],
        ),
    ]