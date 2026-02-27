from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.seller_regi, name='seller_register'),
    path('inventory/', views.seller_inventory, name='seller_products_list'),
    path('sellerdashboard/', views.seller_dashboard, name='sellerdashboard'),
]