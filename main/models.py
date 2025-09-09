from django.db import models
import uuid

class AuctionSeason(models.Model):
    

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('memorabilia', 'Memorabilia'),
        ('collectible', 'Collectible')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auction_season = models.ForeignKey(AuctionSeason, on_delete=models.CASCADE, related_name="products")

    # Fields wajib sesuai ketentuan soal
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(max_length=255)
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(default=0)
    is_featured = models.BooleanField(default=False)

    club = models.CharField(max_length=100, blank=True, null=True)  
    player = models.CharField(max_length=100, blank=True, null=True) 
    match_date = models.DateField(blank=True, null=True)             
    
    def __str__(self):
        if self.club:
            club_info = self.club
        else: ""
        return f"{self.name} {club_info} - Starts from Rp{self.price:,.0f}"
    
    @property
    def highest_bid(self):
        return self.bids.order_by('-amount').first()
    
    @property
    def current_price(self):
        highest = self.highest_bid
        return highest.amount if highest else self.price