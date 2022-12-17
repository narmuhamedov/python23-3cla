from django.shortcuts import render, get_object_or_404
from . import models

#не полное отображение
def tv_show_view(request):
    show = models.TvShow.objects.all()
    return render(request, 'tv_show.html', {'show_object': show})

#детальное отображение об объекте
def tv_show_view_detail(request, id):
    show_detail = get_object_or_404(models.TvShow, id=id)
    return render(request, 'tv_show_detail.html', {'object_detail': show_detail})