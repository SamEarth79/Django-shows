# Generated by Django 4.2.1 on 2023-05-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Show",
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
                ("title", models.CharField(max_length=100, verbose_name="Title")),
                (
                    "fav",
                    models.CharField(max_length=50, verbose_name="Favourite character"),
                ),
                ("rating", models.IntegerField(verbose_name="Rating for the show")),
                (
                    "image",
                    models.ImageField(
                        upload_to="show_images", verbose_name="Image of the show"
                    ),
                ),
            ],
        ),
    ]
