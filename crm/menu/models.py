from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    receipe_name = models.CharField(max_length=200)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="Receipe")

    def __str__(self):
        return self.receipe_name


    @property  # if image is not presrnt
    def imageURL(self):
        try:
            url = self.receipe_image.url
        except:
            url = ''
        return url

RATING_CHOICES = [
    (1, 'One Star'),
    (2, 'Two Stars'),
    (3, 'Three Stars'),
    (4, 'Four Stars'),
    (5, 'Five Stars'),
]
class ReceipReview(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    receipe = models.ForeignKey(Receipe, null=True, on_delete=models.SET_NULL)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=None)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.receipe.receipe_name
    
    def get_rating(self):
        return self.rating




