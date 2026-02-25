from django.urls import path
from . import views


urlpatterns=[
    path('add_categories', views.add_category, name='add_category'),
    path('home',views.all_login,name='all_login'),
    path('category_list',views.category_list,name='category_list'),
    path('home/seller_veri',views.seller_veri,name='seller_veri'),
    path('detailed_view/<int:id>',views.detailed_view,name='detailed_view'),
    
]


