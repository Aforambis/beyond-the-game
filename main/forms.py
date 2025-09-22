from django import forms
from .models import AuctionSeason, Product, Bid

class AuctionSeasonForm(forms.ModelForm):
    class Meta:
        model = AuctionSeason
        fields = ['name', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'auction_season', 'name', 'price', 'description', 'thumbnail',
            'category', 'is_featured', 'club', 'player', 'match_date'
        ]

class BidForm(forms.ModelForm):
    class Meta:
        model = Bid
        fields = ['amount']  