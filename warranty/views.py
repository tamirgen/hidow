from django.shortcuts import render, redirect
from .forms import WarrantyRegistrationForm
from products.models import Product, Category

# Create your views here.

def add_warranty(request):
    form = WarrantyRegistrationForm(request.POST or None)
    if form.is_valid():
        return redirect('registration_success')

    form = WarrantyRegistrationForm()
    # cat=Category.objects.get(name='devices')
    # form.products.queryset=Product.objects.filter(category=cat)
    context = {
        "form": form

    }
    return render(request, 'warranty/registration.html', context)

def registration_success(request):
    " A view to render the thank you page"
    return render(request, "warranty/success.html")