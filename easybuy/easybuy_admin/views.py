from easybuy.core.models import Category, User
from easybuy.seller.models import SellerProfile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.text import slugify
from .models import Category



from django.shortcuts import render, get_object_or_404, redirect

def approve_seller(request, id):
    seller = get_object_or_404(SellerProfile, id=id)
    seller.status = "APPROVED"
    seller.save()
    return redirect('seller_veri')

def reject_seller(request, id):
    seller = get_object_or_404(SellerProfile, id=id)
    seller.status = "REJECTED"
    seller.save()
    return redirect('seller_veri')



def seller_veri(request):
    unverified = SellerProfile.objects.filter(status='PENDING')
    return render(request, 'admin/seller_veri.html', {'unverified': unverified})

def detailed_view(request,id):
    details=SellerProfile.objects.select_related('user').get(pk=id)
    return render(request,'admin/details_view.html',{'details':details})



def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        slug = slugify(name)
        image = request.FILES.get("image_url")
        description = request.POST.get("des")
        Category.objects.create(
            name=name,
            slug=slug,
            image_url=image,
            description=description,
        )
        messages.success(request, f"Category '{name}' added successfully!")
        return redirect('all_categories')
    return render(request, "add_category.html")


def all_users(request):
    users = User.objects.filter(role="CUSTOMER")
    return render(request, "admin/all_users.html", {"users": users})