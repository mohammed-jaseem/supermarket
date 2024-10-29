from django.urls import path
from web import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("products/", views.products, name="products"),
    path("features/", views.features, name="features"),
    path("categories/", views.categories, name="categories"),


]