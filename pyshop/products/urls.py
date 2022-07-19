from django.urls import path
from . import views


# /products
# /products/1/detail
# /Products/new
urlpatterns = [
    path('', views.index)
]