from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import AuctionSeason, Product, Bid

class AuctionSeasonForm(forms.ModelForm):
    class Meta:
        model = AuctionSeason
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# --- PRODUCT FORM YANG SUDAH DIPERBAIKI ---
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Tentukan field mana yang ingin Anda tampilkan di form
        fields = [
            'name', 'auction_season', 'price', 'description', 
            'thumbnail', 'category', 'is_featured', 'club', 'player', 'match_date'
        ]

    # __init__ ditambahkan untuk memberi styling pada input fields
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        
        # Daftar field yang ingin kita beri style umum
        styled_fields = [
            'name', 'price', 'description', 'thumbnail', 
            'club', 'player', 'match_date'
        ]

        # Loop untuk menambahkan kelas CSS ke setiap widget input
        for field_name in self.fields:
            if field_name in styled_fields:
                self.fields[field_name].widget.attrs.update({
                    'class': 'mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm placeholder-gray-400 focus:outline-none focus:ring-gray-800 focus:border-gray-800 sm:text-sm'
                })
            # Style khusus untuk dropdown/select
            if field_name in ['auction_season', 'category']:
                 self.fields[field_name].widget.attrs.update({
                    'class': 'mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-gray-800 focus:border-gray-800 sm:text-sm rounded-md'
                })
            # Style khusus untuk checkbox
            if field_name == 'is_featured':
                self.fields[field_name].widget.attrs.update({
                    'class': 'h-4 w-4 text-gray-800 focus:ring-gray-900 border-gray-300 rounded'
                })

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']

# 🔑 Tambahan: Auth Forms
class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label