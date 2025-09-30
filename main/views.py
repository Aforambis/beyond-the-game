from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm, AuctionSeasonForm, BidForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm': '2406421081',
        'name': request.user.username,
        'class': 'PBP F',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)

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

@login_required(login_url='/login')
def show_products(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "my":
        products = Product.objects.filter(user=request.user)
    else:
        products = Product.objects.all()

    context = {
        'npm' : '2406421081',
        'name': request.user.username if request.user.is_authenticated else 'Guest',
        'class': 'PBP F',
        'product_list': products,   
        'products': products,       
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "products.html", context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "product_detail.html", {"product": product})

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_products')

    context = {
        'form': form
    }

    return render(request, "add_product.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def add_auction_season(request):
    form = AuctionSeasonForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        messages.success(request, "Auction season created!")
        return redirect('main:show_main')
    
    return render(request, 'add_auction_season.html', {'form': form})

@login_required(login_url='/login')
def place_bid(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = BidForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        bid = form.save(commit=False)
        bid.product = product
        bid.user = request.user

        if bid.amount <= product.current_price:
            messages.error(request, f"Bid must be higher than current price: IDR {product.current_price:,.0f}")
        else:
            bid.save()
            messages.success(request, "Bid placed successfully!")
            return redirect('main:product_detail', id=product.id)

    return render(request, 'place_bid.html', {'form': form, 'product': product})

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Check if the user is the owner of the product
    if product.user != request.user:
        messages.error(request, "You are not authorized to delete this item.")
        return redirect('main:show_products')
        
    product.delete()
    return redirect('main:show_products')

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    # Check if the user is the owner of the product
    if product.user != request.user:
        messages.error(request, "You are not authorized to edit this item.")
        return redirect('main:show_products')

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_products')

    context = {'form': form}
    return render(request, "edit_product.html", context)