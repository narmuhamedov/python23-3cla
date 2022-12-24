from django.db import models

class AboutUs(models.Model):
    text = models.TextField()
    img = models.ImageField(upload_to='')
