from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("password/", views.clear_date, name="password"),
]
