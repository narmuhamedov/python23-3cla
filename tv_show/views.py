from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms

#не полное отображение
def tv_show_view(request):
    show = models.TvShow.objects.all()
    return render(request, 'tv_show.html', {'show_object': show})

#детальное отображение об объекте
def tv_show_view_detail(request, id):
    show_detail = get_object_or_404(models.TvShow, id=id)
    return render(request, 'tv_show_detail.html', {'object_detail': show_detail})


#добавление tvshow
def add_tv_show_view(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        form.save()
        return HttpResponse('<h1>Фильм успешно добавлен</h1>')
    else:
        form = forms.ShowForm()

    return render(request, 'create_tv_show.html', {'form': form})