from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from django.views import generic

# не полное отображение
class TvShowView(generic.ListView):
    template_name = "tv_show.html"
    queryset = models.TvShow.objects.all()

    def get_queryset(self):
        return models.TvShow.objects.all()


# def tv_show_view(request):
#     show = models.TvShow.objects.all()
#     return render(request, 'tv_show.html', {'show_object': show})

# детальное отображение об объекте
class TvShowDetailView(generic.DetailView):
    template_name = "tv_show_detail.html"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.TvShow, id=show_id)


# def tv_show_view_detail(request, id):
#     show_detail = get_object_or_404(models.TvShow, id=id)
#     return render(request, 'tv_show_detail.html', {'object_detail': show_detail,
#                                                    })

# добавление tvshow
class TvShowCreateView(generic.CreateView):
    template_name = "create_tv_show.html"
    form_class = forms.ShowForm
    queryset = models.TvShow.objects.all()
    success_url = "/tv_show/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(TvShowCreateView, self).form_valid(form=form)


# def add_tv_show_view(request):
#     method = request.method
#     if method == 'POST':
#         form = forms.ShowForm(request.POST, request.FILES)
#         form.save()
#         return HttpResponse('<h1>Фильм успешно добавлен</h1>')
#     else:
#         form = forms.ShowForm()
#
#     return render(request, 'create_tv_show.html', {'form': form})

# обновление тв шоу
class TvShowUpdateView(generic.UpdateView):
    template_name = "tv_show_update.html"
    form_class = forms.ShowForm
    success_url = "/tv_show/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.TvShow, id=show_id)

    def form_valid(self, form):
        return super(TvShowUpdateView, self).form_valid(form=form)


# def update_tv_show_view(request, id):
#     show_object = get_object_or_404(models.TvShow, id=id)
#     if request.method == 'POST':
#         form = forms.ShowForm(instance=show_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h1>Фильм успешно обновлен</h1>')
#     else:
#         form = forms.ShowForm(instance=show_object)
#     return render(request, 'tv_show_update.html', {'form': form, 'object': show_object})


# Удаление Тв шоу
class TvShowDeleteView(generic.DeleteView):
    template_name = "confirm_delete.html"
    success_url = "/tv_show/"

    def get_object(self, **kwargs):
        show_id = self.kwargs.get("id")
        return get_object_or_404(models.TvShow, id=show_id)


# def delete_tv_show_view(request, id):
#     show_object = get_object_or_404(models.TvShow, id=id)
#     show_object.delete()
#     return HttpResponse('<h1>Фильм успешно удален</h1>')
