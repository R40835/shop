from django import forms
from .models import Followers, Dress, Blanket


class NewsLetterForm(forms.Form): 
    PRODUCT_CHOICES = ( 
        ("Tous", "Tous"), 
        ("Couvertures", "Couvertures"), 
        ("Robes", "Robes"), 
    ) 
    email = forms.EmailField(
        min_length=8, 
        max_length=30, 
        required=True,         
        widget=forms.TextInput(
            attrs={
                'id': 'email',
                'class': 'letter-form', 
                'placeholder': 'Adresse Email',
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'phone',
                'class': 'letter-form', 
                'placeholder': 'Numero de telephone',
            }
        )
    )
    preference = forms.ChoiceField(
        choices=PRODUCT_CHOICES,
        widget=forms.Select(
            attrs={
                'id': 'preference',
                'class': 'letter-form',
                'placeholder': 'Produit(s)',
            }
        )
    )

    class Meta:
        model = Followers
        fields = ("email", "phone", "preference")


class AdminDressUploadForm(forms.Form):
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'admin-upload', 
                'placeholder': 'Image', 
                'id': "set-image"
            }
        ), 
        label='Image', 
        required=True
    )
    price = forms.FloatField(
        widget=forms.TextInput(
            attrs={
                'class': 'admin-upload', 
                'placeholder': 'Prix', 
                'id': "set-price"
            }
        )
    )

    class Meta:
        model = Dress
        fields = ('image', 'price')
