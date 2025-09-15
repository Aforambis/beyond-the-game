from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

def show_main(request):
    context = {
        'app_name': 'Beyond the Game',
        'name': 'Rusydan Mujtaba Ibnu Ramadhan',
        'class': 'PBP F'
    }
    return render(request, "main.html", context)

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_products")
    else:
        form = ProductForm()
    return render(request, "add_product.html", {"form": form})