from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('enable-rating/<int:product_id>/', views.enable_rating,
         name='enable_rating'),
    path('disable-rating/<int:product_id>/', views.disable_rating,
         name='disable_rating'),
    path('get_reviews/<int:product_id>/', views.get_reviews, name='get_reviews'),
]
