from django.urls import path
from . import views

urlpatterns = [
    path('', views.CrearListarUser.as_view())
]