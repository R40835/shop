from django.db import models


class Products: 
    """
        Fields : 
        - Product_name
        - product_price 
        - product_image 
        - product_quantity in stock
        - product_category 
        - product_quantity_shopping_cart => (it could change depend on the context)
    
    """



class Contact(models.Model):
    """
        fields : 
        - Firstname: CharField(max_length = 255)
        - email : 
        - Comment : TextArea
    
    """

    first_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    Comments = models.TextField()


class Subscribe_sending_email(models.Model):
    """ 
        We will use this model for sending an email to the people how are subsribe when we add 
        a new product for this we need from the user the enter an email and when the 
        admin add a new product in the database an email will be sending automaticly to 
        tel the user for this new product added in the store.

        fields : 
            - email 
            - product : after adding each product an email will be send to tell the subsribers that is a new product in our store. but the problem is it could add an 
            emails to the span when we will add 30 new products for example in 15 min so 30 emails will be send to all users ?? 
        we can add this as foreing  key in the product model 
    """

    

