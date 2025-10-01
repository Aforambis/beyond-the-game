from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class AuctionSeason(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
    @property
    def is_active(self):
        now = timezone.now()
        return self.start_date <= now <= self.end_date

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('jersey', 'Match-Worn Jersey'),
        ('shoes', 'Match-Worn Shoes'),
        ('ball', 'Match Ball'),
        ('artwork', 'Artwork & Posters'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auction_season = models.ForeignKey('AuctionSeason', on_delete=models.CASCADE, related_name="products")

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(max_length=205, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)    
    is_featured = models.BooleanField(default=False)

    club = models.CharField(max_length=100, blank=True, null=True)  
    player = models.CharField(max_length=100, blank=True, null=True) 
    match_date = models.DateField(blank=True, null=True)

    # --- KOLOM BARU ADA DI SINI ---
    hero_image_url = models.URLField(max_length=255, blank=True, null=True, help_text="Link gambar HD untuk banner besar di halaman detail.")
    story_details = models.TextField(blank=True, null=True, help_text="Cerita mendalam di balik item: statistik pertandingan, kutipan, dll.")
    
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_products")
    is_sold = models.BooleanField(default=False)
    # --- BATAS KOLOM BARU ---
    
    def __str__(self):
        club_info = f"{self.club}" if self.club else ""
        return f"{self.name} {club_info} - Starts from IDR {self.price:,.0f}"

    @property
    def highest_bid(self):
        return self.bids.order_by('-amount').first()
    
    @property
    def current_price(self):
        highest = self.highest_bid
        return highest.amount if highest else self.price


class Bid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-amount', 'created_at']

    def __str__(self):
        return f"{self.user.username} bids IDR {self.amount:,.0f} on {self.product.name}"