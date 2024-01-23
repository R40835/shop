from django.db import models
from PIL import Image
        

class Category(models.Model):
    name        = models.CharField(max_length=60, null=False, blank=False, unique=True)
    image       = models.ImageField(upload_to="category/", null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_category_choices(cls) -> tuple:
        """
        Unique category choices, used in newsletter form.
        """
        try:
            # check if the table exists in the database
            cls.objects.exists()
            
            # if the table exists, proceed with the query
            unique_values = cls.objects.values('name').distinct()
            categories = [(value['name'], value['name']) for value in unique_values] + [('Tous', 'Tous')]
            size = cls.get_longest_category_size(categories)
            no_choice = '-' * size
            if len(no_choice) <= 3 or size == 0:
                no_choice = '----'
            categories = [(no_choice, no_choice)] + categories
            return tuple(categories)
        
        except Exception as e:
            # handle the exception when creating db (table doesn't exist at this point)
            print(f"Database has just being created, setting choice field for categories to default (in forms.py)")
            return (('----', '----'),)
    
    @classmethod
    def get_longest_category_size(cls, choices: tuple) -> int:
        """
        Get the longest category string size.
        """
        if choices:
            longest_category = max(choices, key=lambda x: len(x[0]))
            return len(longest_category[0])
        return 0 

    def __str__(self) -> str:
        """
        This method comes into play when using queryset with forms.
        It's the attribute being queried there.
        """
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Overriding the save method to resize the images uploaded.
        """
        super(Category, self).save(*args, **kwargs)

        SIZE = (500, 500)
        image = Image.open(self.image.path)
        category_image = image.resize(SIZE)
        category_image.save(self.image.path)


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

    def save(self, *args, **kwargs):
        """
        Overriding the save method to resize the images uploaded.
        """
        super(Product, self).save(*args, **kwargs)

        SIZE = (500, 500)
        image = Image.open(self.image.path)
        product_image = image.resize(SIZE)
        product_image.save(self.image.path)


class Follower(models.Model):
    email    = models.EmailField(null=False, blank=False, unique=True)
    phone    = models.CharField(max_length=15, null=False, blank=False, unique=True)
    category = models.CharField(max_length=60, null=False, blank=False)


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
        Check if the product is fully paid and make it a full purchase if it is.
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
        Called when a part of the product's full price is paid.
        """
        self.revenue += installement
        self.save()
        self.check_purchase_complete()


class Installement(models.Model):
    amount                  = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    timestamp               = models.DateTimeField(auto_now_add=True)

    installement_purchase   = models.ForeignKey(InstallementPurchase, on_delete=models.CASCADE)


class ProductArchive(models.Model): ...