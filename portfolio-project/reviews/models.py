from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Reviews(models.Model):
    film_title = models.CharField(max_length=200)
    review_text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='media/images/')
    rating = models.IntegerField(
        default = 0,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.film_title

    def summary(self):
        return self.review_text[:500] + '...'

    def publish_date_pretty(self):
        return self.publish_date.strftime('%b %e %Y')