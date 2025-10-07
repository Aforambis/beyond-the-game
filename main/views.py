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
from django.contrib.auth.forms import PasswordChangeForm

from .forms import ProductForm, AuctionSeasonForm, BidForm, CustomUserCreationForm, UsernameChangeForm

@login_required(login_url='/login')
def show_main(request):
    # Kita pastikan view ini mengirimkan daftar produk untuk tes
    products = Product.objects.all()

    context = {
        'products': products,
        'name': request.user.username,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main/main.html", context)

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
        'name': request.user.username if request.user.is_authenticated else 'Guest',
        'products': products,       
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main/products.html", context)

def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, "main/product_detail.html", {"product": product})

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "main/add_product.html", context)

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login setelah daftar
            messages.success(request, "Your account has been successfully created!")
            return redirect("main:show_main")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "main/register.html", {"form": form})

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
   return render(request, 'main/login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("main:login"))
    response.delete_cookie("last_login")
    return response

@login_required(login_url='/login')
def add_auction_season(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to perform this action.")
        return redirect('main:show_main')

    form = AuctionSeasonForm(request.POST or None)
    
    if form.is_valid() and request.method == 'POST': 
        form.save()
        messages.success(request, "Auction season created!")
        return redirect('main:show_main')
    
    return render(request, 'main/add_auction_season.html', {'form': form})

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

    return render(request, 'main/place_bid.html', {'form': form, 'product': product})

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Check if the user is the owner of the product
    if product.user != request.user:
        messages.error(request, "You are not authorized to delete this item.")
        return redirect('main:show_main')
        
    product.delete()
    return redirect('main:show_main')

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)

    # Check if the user is the owner of the product
    if product.user != request.user:
        messages.error(request, "You are not authorized to edit this item.")
        return redirect('main:show_main')

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "main/add_product.html", context)

@login_required
def all_products(request):
    products = Product.objects.all()
    # Render the new partial and use the key 'products'
    return render(request, "main/partials/product_list.html", {"products": products})

@login_required
def my_products(request):
    products = Product.objects.filter(user=request.user)
    # Render the new partial and use the key 'products'
    return render(request, "main/partials/product_list.html", {"products": products})

@login_required
def profile(request):
    user = request.user
    username_form = UsernameChangeForm(instance=user)
    password_form = PasswordChangeForm(user)

    if request.method == 'POST':
        # Check which form was submitted
        if 'change_username' in request.POST:
            username_form = UsernameChangeForm(request.POST, instance=user)
            if username_form.is_valid():
                username_form.save()
                messages.success(request, 'Your username has been updated!')
                return redirect('main:profile')
        
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return redirect('main:profile')
            else:
                messages.error(request, 'Please correct the error below.')

    user_products = Product.objects.filter(user=request.user)

    context = {
        'username_form': username_form,
        'password_form': password_form,
        'products': user_products 
    }
    return render(request, 'main/profile.html', context)

def journal(request):
    return render(request, "main/journal.html")

def my_bids(request):
    bids = request.user.bids.select_related('product').order_by('-created_at')
    return render(request, "main/my_bids.html", {"bids": bids})