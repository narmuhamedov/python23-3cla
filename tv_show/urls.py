from django.urls import path
from . import views

urlpatterns = [
    path('tv_show/', views.tv_show_view, name='tv_show'),
    path('tv_show_detail/<int:id>/', views.tv_show_view_detail, name='detail'),
]