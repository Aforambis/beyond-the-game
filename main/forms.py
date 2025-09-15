from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['auction_season', 'name', 'price', 'description', 'thumbnail', 'category', 'is_featured', 'club', 'player', 'match_date']