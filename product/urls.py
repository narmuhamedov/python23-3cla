from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("product/", views.ProductListView.as_view(), name="product_list"),
    path("product/<int:id>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("add-order/", views.OrderCreateView.as_view(), name="add-order"),
]
