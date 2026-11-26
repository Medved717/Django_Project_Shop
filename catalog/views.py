from django.shortcuts import render

from catalog.models import Product


def contacts(requests):
    return render(requests, 'catalog/contacts.html')


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/home.html', context)


def details(request, id_product):
    product = Product.objects.get(id=id_product)
    context = {'product': product}
    return render(request, 'catalog/details.html', context)
