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

from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    # Definisikan field secara eksplisit untuk menambahkan placeholder/empty_label
    auction_season = forms.ModelChoiceField(
        queryset=AuctionSeason.objects.all(),
        empty_label="Select a Season", # <-- INI PLACEHOLDER-NYA
        label="Auction Season",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    category = forms.ChoiceField(
        choices=[('', 'Choose a Category')] + Product.CATEGORY_CHOICES, # <-- INI PLACEHOLDER-NYA
        label="Category",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Product
        fields = [
            'name', 'auction_season', 'start_price', 'category', 
            'description', 'thumbnail', 'club', 'player', 'match_date'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Lionel Messi Signed Jersey'}),
            'start_price': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'e.g., 5000000'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'rows': 4, 'placeholder': 'Describe the story and condition of the item...'}),
            'thumbnail': forms.URLInput(attrs={'class': 'form-input', 'placeholder': 'https://example.com/image.jpg'}),
            'club': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., FC Barcelona'}),
            'player': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g., Lionel Messi'}),
            'match_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
        }
        labels = {
            'name': 'Item Name',
            'start_price': 'Starting Price (IDR)',
        }

    def clean(self):
        cleaned_data = super().clean()
        category = cleaned_data.get("category")
        club = cleaned_data.get("club")
        player = cleaned_data.get("player")

        # Jika kategori adalah jersey atau sepatu
        if category in ["jersey", "shoes"]:
            # Cek apakah field club kosong
            if not club:
                self.add_error('club', "Club is required for jerseys and shoes.")
            # Cek apakah field player kosong
            if not player:
                self.add_error('player', "Player is required for jerseys and shoes.")
        
        return cleaned_data

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

class UsernameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        help_texts = {
            'username': None,
        }