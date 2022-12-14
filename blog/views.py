from django.shortcuts import render
from . import models

def blogview(request):
    post = models.Post.objects.all()
    return render(request, 'blog.html', {'post_object': post})
