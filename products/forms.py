from django import forms
from .models import (
    Followers, 
    Category, 
    Product, 
    FullPurchase, 
    InstallementPurchase
)


class NewsLetterForm(forms.ModelForm): 
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
        ),
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
    # preference = forms.ModelChoiceField(
    #     queryset=Category.objects.all(), 
    #     required=True,
    #     widget=forms.Select(
    #         attrs={
    #             'id': 'preference',
    #             'class': 'letter-form',
    #             'placeholder': 'Produit(s)',
    #         }
    #     ),
    # )
    preference = forms.ChoiceField(
        required=True,
        choices=(('Tous', 'Tous'),),
        widget=forms.Select(
            attrs={
                'id': 'preference',
                'class': 'letter-form',
                'placeholder': 'Produit(s)',
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        """
        Overriding the constructor to append a custom choice.
        """
        super(NewsLetterForm, self).__init__(*args, **kwargs)
        custom_choice = (('Tous', 'Tous'))
        # self.fields['preference'].choices = list(self.fields['preference'].choices) + [custom_choice] 

    class Meta:
        model  = Followers
        fields = ("email", "phone", "preference")


class AdminProductUploadForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'product-name',
                'class': 'admin-upload', 
                'placeholder': 'Nom du produit',
            }
        ),
    )
    description = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'id': 'product-name',
                'class': 'admin-upload', 
                'placeholder': 'Description du produit',
            }
        )
    )
    image = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={
                'id': "product-image",
                'class': 'admin-upload', 
                'placeholder': 'Image', 
            }
        )
    )
    price = forms.FloatField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': "product-price",
                'class': 'admin-upload', 
                'placeholder': 'Prix',
            }
        )
    )
    stock = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': "product-stock",
                'class': 'admin-upload', 
                'placeholder': 'Nombre d\'article',
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        required=True,
        widget=forms.Select(
            attrs={
                'id': "product-category",
                'class': 'admin-upload', 
                'placeholder': 'Category',
            }
        )
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), 
        required=True,
        widget=forms.Select(
            attrs={
                'id': "product-category",
                'class': 'admin-upload', 
                'placeholder': 'Category',
            }
        )
    )


    class Meta:
        model  = Product
        fields = ('name', 'description', 'image', 'price', 'stock', 'category')


class AdminSaleConfirmationForm(forms.Form):
    quantity = forms.IntegerField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': "sale-quantity",
                'class': 'admin-sale-confirmation', 
                'placeholder': 'Nombre d\'articles vendus',
            }
        )
    )

    class Meta:
        model  = FullPurchase
        fields = ('quantity')


class AdminInstallementSaleForm:
    #TODO: working on...
    paid_installement = forms.FloatField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': "sale-revenue",
                'class': 'admin-sale-confirmation', 
                'placeholder': 'Revenue',
            }
        )
    )

    class Meta:
        model = InstallementPurchase
        fields = ('')
