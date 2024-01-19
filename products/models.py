from django.db import models


class Dress(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    image = models.ImageField(upload_to="dresses/", null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)


class Blanket(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False)
    image = models.ImageField(upload_to="blankets/", null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)


class Category(models.Model):
    dress = models.ForeignKey(Dress, models.CASCADE)
    blanket = models.ForeignKey(Blanket, models.CASCADE)


class Followers(models.Model):
    PRODUCT_CHOICES = [
        ("Tous", "Tous"), 
        ("Couvertures", "Couvertures"), 
        ("Robes", "Robes"), 
    ]
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.CharField(max_length=15, null=False, blank=False, unique=True)
    preference = models.CharField(max_length=60, choices=PRODUCT_CHOICES)

