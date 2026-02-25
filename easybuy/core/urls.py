from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('home/', views.home_view, name='home'),
    path('products/', views.all_products, name='all_products'),
    path('profile/', views.profile_settings, name='profile_settings'),

]
