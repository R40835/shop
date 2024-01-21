from django.db import models
        

class Followers(models.Model):
    email       = models.EmailField(null=False, blank=False, unique=True)
    phone       = models.CharField(max_length=15, null=False, blank=False, unique=True)
    preference  = models.CharField(max_length=60, null=False, blank=False)


class Category(models.Model):
    name        = models.CharField(max_length=60, null=False, blank=False)
    image       = models.ImageField(upload_to="category/", null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> models.CharField:
        """
        This method comes into play when using queryset with forms.
        It's the attribute being queried there.
        """
        return self.name


class Product(models.Model):
    name        = models.CharField(max_length=60, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    image       = models.ImageField(upload_to="product/", null=False, blank=False)
    price       = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock       = models.PositiveIntegerField()
    created_at  = models.DateTimeField(auto_now_add=True)
    available   = models.BooleanField(default=True)

    category    = models.ForeignKey(Category, on_delete=models.CASCADE)

    def check_availabality(self) -> 'Product':
        """
        Check whether a product is still on sale.
        """
        if self.stock == 0:
            self.available = False
            self.save()
            return self
        return self

    def decrement_stock(self, sold_quantity: int) -> None:
        """
        Decrement a set of products by one after a sale.
        """
        self.stock -= sold_quantity
        self.save()


class Purchase(models.Model):
    quantity = models.PositiveIntegerField(null=False, blank=False)
    revenue  = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    date     = models.DateTimeField(auto_now_add=True)

    product  = models.ForeignKey(Product, on_delete=models.CASCADE)

    def save(self, *args, **kwargs) -> None:
        """
        Overriding the save method to update the 
        product stock upon client purchase.
        """
        self.revenue = self.product.price * self.quantity
        self.product.decrement_stock(self.quantity)
        super(Purchase, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class FullPurchase(Purchase): 
    complete = models.BooleanField(default=True)


class InstallementPurchase(Purchase): 
    complete = models.BooleanField(default=False)
    #TODO: discuss whether or not you wanna keep timestamps of all payments TODO
    
    def check_purchase_complete(self) -> bool:
        """
        Called to check whether a product is fully paid.
        """
        if self.revenue == self.product.price:
            FullPurchase.objects.create(
                quantity=self.quantity,
                revenue=self.revenue,
                date=self.date 
            )
            self.delete()
            return True
        return False 

    def pay_installement(self, installement: float) -> None:
        """
        Called when an part of the full price is paid.
        """
        self.revenue += installement
        self.save()
        self.check_purchase_complete()


