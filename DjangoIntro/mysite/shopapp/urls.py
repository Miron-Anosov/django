from django.urls import path

from . import views

app_name = "shopapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("groups", views.get_groups, name="group"),
]
