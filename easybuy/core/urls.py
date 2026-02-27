from django.urls import path
from . import views
from easybuy.user.views import  new_arrival
urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.all_login, name='all_login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_settings, name='profile_settings'),
    path('products/', views.all_products, name='all_products'),
    path('all-categories/', views.all_categories, name='all_categories'),
    path('new-arrivals/', new_arrival, name='new_arrivals'),
]