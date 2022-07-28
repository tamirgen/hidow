from django.shortcuts import render, redirect
from .forms import WarrantyRegistrationForm
from products.models import Product, Category
from .models import WarrantyRegistration

from django.core.mail import send_mail
from django.template.loader import render_to_string


def add_warranty(request):
    """ A view to add details for warranty registration and to send
        a confirmation email"""
        
    form = WarrantyRegistrationForm(request.POST or None)
    if form.is_valid():
        fullName = request.POST["full_name"]
        email = request.POST["email"]
        country = request.POST["country"]
        postcode = request.POST["postcode"]
        city = request.POST["city"]
        street_address1 = request.POST["street_address1"]
        street_address2 = request.POST["street_address2"]
        products = request.POST["products"]
        quantity = request.POST["quantity"]

        warranty = WarrantyRegistration(
            full_name=fullName,
            email=email,
            country=country,
            postcode=postcode,
            city=city,
            street_address1=street_address1,
            street_address2=street_address2,
            quantity=quantity,
        )

        id = int(products)
        specificProduct = Product.objects.get(pk=id)
        warranty.save()
        warranty.products.add(specificProduct)
        html = render_to_string(
            "warranty/confirmation_email/registration_confirm_email_body.html",
            {
                "warranty": warranty,
                "product": specificProduct.name,
                "contact_email": "support@hidowgeremany.com",
            },
        )

        response = send_mail(
            "Warranty Registarion - Hidow Germany",
            "This is the message",
            "noreply@hidowgeremany.com",
            [email],
            html_message=html,
        )
        return redirect("registration_success")

    form = WarrantyRegistrationForm()

    context = {"form": form}
    return render(request, "warranty/registration.html", context)


def registration_success(request):
    "A view to render the thank you page"
    return render(request, "warranty/success.html")
