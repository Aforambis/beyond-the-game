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
    CATEGORY_CHOICES = [
        ('jersey', 'Match-Worn Jersey'),
        ('shoes', 'Match-Worn Shoes'),
        ('ball', 'Match Ball'),
        ('artwork', 'Artwork & Posters'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auction_season = models.ForeignKey(AuctionSeason, on_delete=models.CASCADE, related_name="products")

    # Fields wajib sesuai ketentuan soal
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)    
    is_featured = models.BooleanField(default=False)

    club = models.CharField(max_length=100, blank=True, null=True)  
    player = models.CharField(max_length=100, blank=True, null=True) 
    match_date = models.DateField(blank=True, null=True)             
    
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