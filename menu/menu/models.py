from django.db import models

from django.contrib.auth.models import User

from django.db.models import Avg
from datetime import datetime


# Create your models here.

class Receipe(models.Model):
    
    receipe_name = models.CharField(max_length=200)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="Receipe")
    receipe_price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.receipe_name

    def AveragReview(self):
        review = ReceipReview.objects.filter(receipe=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if review['average'] is not None:
            avg = float(review["average"])
        return avg

    @property  # if image is not presrnt    
    def imageURL(self):
        try:
            url = self.receipe_image.url
        except:
            url = ''
        return url


class ReceipReview(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    receipe = models.ForeignKey(Receipe, null=True, on_delete=models.SET_NULL)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.review  
    
    
    



    
    

   




