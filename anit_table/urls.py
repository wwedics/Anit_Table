from django.urls import path

from . import views

urlpatterns = [
    path("anmtn/", views.anmtn, name="anmtn"),
    path("analem/", views.analem, name="analem")
]
