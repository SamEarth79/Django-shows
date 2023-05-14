from django.db import models


# Create your models here.
class Show(models.Model):
    title = models.CharField(("Title"), max_length=100)
    fav = models.CharField(("Favourite character"), max_length=50)
    rating = models.IntegerField(("Rating for the show"))
    image = models.ImageField(
        ("Image of the show"),
        upload_to="show_images",
        height_field=None,
        width_field=None,
        max_length=None,
        null=True,
    )

    def __str__(self):
        return self.title
