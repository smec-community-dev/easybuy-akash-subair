from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomerRegisterForm
from .models import Category,Address
from easybuy.seller.models import Product,ProductVariant, ProductImage
from django.core.paginator import Paginator
def register_view(request):
    if request.method == "POST":
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = "CUSTOMER"
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomerRegisterForm()
    return render(request, "core/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)   
        if user is not None:
            login(request, user)
            return redirect("home") 
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, "core/login.html")

def logout_view(request):
    logout(request)
    return redirect("categories")

def home_view(request):
    categories = Category.objects.filter(is_active=True)
    product_images = ProductImage.objects.filter(is_primary=True).select_related('variant__product')
    return render(request, "core/home.html", {"categories": categories,"product_images": product_images })




def all_products(request):
    product_images = ProductImage.objects.filter(is_primary=True).select_related('variant__product')
    paginator = Paginator(product_images, 8) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "core/all_products.html", {"page_obj": page_obj})


@login_required
def profile_settings(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.phone_number = request.POST.get('phone_number')
        user.dob = request.POST.get('dob') if request.POST.get('dob') else None
        user.gender = request.POST.get('gender')
        
        if request.FILES.get('profile_image'):
            user.profile_image = request.FILES.get('profile_image')
            
        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile_settings')

    return render(request, "core/profile.html")