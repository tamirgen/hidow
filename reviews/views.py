from django.shortcuts import render, redirect
from .models import Products
from .models import Review
from .forms import ReviewForm


def products(request):
    " A view to get render the products to be reviewed"
    items = Products.objects.all()
    context = {
        'items': items
    }

    return render(request, "reviews/products.html", context)


def rate(request, id):
    " A view to present the rate form and to redirect to thank you page"
    post = Products.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        author = request.POST.get('author')
        stars = request.POST.get('stars')
        comment = request.POST.get('comment')
        review = Review(author=author, stars=stars,  comment=comment,
                        product=post)
        review.save()
        return redirect('success')

    form = ReviewForm()
    context = {
        "form": form

    }
    return render(request, 'reviews/rate.html', context)


def success(request):
    " A view to render the thank you page"
    return render(request, "reviews/success.html")