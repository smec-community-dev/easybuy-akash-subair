from django.shortcuts import render

from easybuy.seller.models import Product




# def new_arrival(request):
#     products = Product.objects.filter(
#         is_active=True
#     ).prefetch_related(
#         'variant_set__images'
#     ).order_by('-id')[:8]
#     return render(request, 'user/new_arrival.html', {'products': products})


def new_arrival(request):
    products = Product.objects.filter(
        is_active=True,
        approval_status='APPROVED'
    ).order_by('-created_at')[:8]
    return render(request, 'user/new_arrivals.html', {'products': products})

