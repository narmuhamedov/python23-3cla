from django.urls import path
from . import views

urlpatterns = [
    #path('tv_show/', views.tv_show_view, name='tv_show'),
    path('tv_show/', views.TvShowView.as_view(), name='tv_show'),
    #path('tv_show_detail/<int:id>/', views.tv_show_view_detail, name='detail'),
    path('tv_show_detail/<int:id>/', views.TvShowDetailView.as_view(), name='detail'),
    #path('tv_show/<int:id>/update/', views.update_tv_show_view, name='update'),
    path('tv_show/<int:id>/update/', views.TvShowUpdateView.as_view(), name='update'),
    #path('tv_show/<int:id>/delete/', views.delete_tv_show_view, name='delete'),
    path('tv_show/<int:id>/delete/', views.TvShowDeleteView.as_view(), name='delete'),
    #path('add_tv_show/', views.add_tv_show_view, name='create_tv_show'),
    path('add_tv_show/', views.TvShowCreateView.as_view(), name='create_tv_show'),
]