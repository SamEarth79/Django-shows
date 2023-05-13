from django.db import models


class Show(models.Model):
    title = models.CharField(("Title of the show"), max_length=100)
    fav = models.CharField(("Favourite character"), max_length=50)
    rating = models.IntegerField(("Rating for the show"))
    image = models.ImageField(
        ("Image for the show"),
        upload_to="shows_images",
        height_field=None,
        width_field=None,
        max_length=None,
    )

    def __str__(self):
        return self.title
