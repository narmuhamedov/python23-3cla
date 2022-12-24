from django.shortcuts import render
from . import models

def about_us_view(request):
    about = models.AboutUs.objects.all()
    return render(request, 'about.html', {'about': about})
