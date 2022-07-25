from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_warranty, name='add-warranty'),
    path('registration_success', views.registration_success,
         name="registration_success"),
]
