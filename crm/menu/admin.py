from django.contrib import admin

from .models import (Receipe, ReceipReview)

# Register your models here.

admin.site.register(Receipe)
admin.site.register(ReceipReview)