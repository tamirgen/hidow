from django.shortcuts import render, redirect
from .models import WarrantyRegistration
from .forms import WarrantyForm


def register(request, id):
    " A view to present the rate form and to redirect to thank you page"
    post = WarrantyRegistration().objects.get(id=id)
    form = WarrantyForm(request.POST or None)
    if form.is_valid():
        full_name = request.POST.get('full name')
        email = request.POST.get('email')
        street_address1 = request.get('address')
        postcode = request.get('postcode')
        town_or_city = request.get('town_or_city')
        country = request.get('country')
        date = request.get('date')
        warranty = WarrantyRegistration(product=post, full_name=full_name, email=email,
                 street_address1=street_address1, postcode=postcode, town_or_city=town_or_city,
                 country=country, date=date,)
        warranty.save()
        return redirect('success')

    form = WarrantyForm()
    context = {
        "form": form

    }
    return render(request, 'warranty/warranty-form.html', context)
def success(request):
    " A view to render the thank you page"
    return render(request, "warranty/success.html")