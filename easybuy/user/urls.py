from django.urls import path
from . import views
from easybuy.seller.models import Product
from easybuy.core.views import all_products

urlpatterns = [
    path('allproducts/', all_products, name='all_products'),
    path('newarrivals/', views.new_arrival, name='new_arrivals'),
]
    