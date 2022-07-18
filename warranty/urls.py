from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_warranty, name='add-warranty'),
]
