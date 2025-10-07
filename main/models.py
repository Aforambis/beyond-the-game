from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.core.validators import MinValueValidator

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
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('sold', 'Sold'),
        ('ended', 'Ended (Not Sold)'),
    ]
    CATEGORY_CHOICES = [
        ('jersey', 'Match-Worn Jersey'),
        ('shoes', 'Match-Worn Shoes'),
        ('ball', 'Match Ball'),
        ('artwork', 'Artwork & Posters'),
        ('other', 'Other'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products") # Seller
    auction_season = models.ForeignKey('AuctionSeason', on_delete=models.CASCADE, related_name="products")
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_price = models.DecimalField(max_digits=18, decimal_places=2, default=0, validators=[MinValueValidator(0)]) 
    thumbnail = models.URLField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    
    # --- METADATA & STATUS ---
    is_featured = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_products")

    # --- OPTIONAL DETAILS ---
    club = models.CharField(max_length=100, blank=True, null=True)  
    player = models.CharField(max_length=100, blank=True, null=True) 
    match_date = models.DateField(blank=True, null=True)
    hero_image_url = models.URLField(max_length=255, blank=True, null=True, help_text="Link for high-res banner image.")
    story_details = models.TextField(blank=True, null=True, help_text="In-depth story behind the item.")
    
    def __str__(self):
        return f"{self.name} - Starts from IDR {self.start_price:,.0f}"

    @property
    def highest_bid(self):
        return self.bids.order_by('-amount').first()
    
    @property
    def current_price(self):
        highest = self.highest_bid
        return highest.amount if highest else self.start_price

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator

class Bid(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids")
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]  # bid harus positif (> 0)
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} bids IDR {self.amount:,.0f} on {self.product.name}"

    def clean(self):
        current_price = self.product.current_price
        if self.amount <= current_price:
            raise ValidationError(f"Bid amount must be higher than the current price (IDR {current_price:,.0f}).")

    def save(self, *args, **kwargs):
        self.full_clean() 
        super().save(*args, **kwargs)

# This new UserProfile model will hold the watchlist
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watchlist = models.ManyToManyField(Product, blank=True, related_name='watched_by')

    def __str__(self):
        return self.user.username

# These functions automatically create/save a UserProfile whenever a User is created/saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

@property
def is_active(self):
    return self.auction_season.start_date <= timezone.now() <= self.auction_season.end_date

def update_status(self):
    if not self.is_active:
        if self.highest_bid:
            self.status = 'sold'
            self.winner = self.highest_bid.user
        else:
            self.status = 'ended'
        self.save()