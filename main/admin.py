from django.contrib import admin
from .models import Product, AuctionSeason, Bid

admin.site.register(Product)
admin.site.register(AuctionSeason)
admin.site.register(Bid)