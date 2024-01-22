from django import forms
from ..models import Category, Product, FullPurchase, InstallementPurchase
from django.core.exceptions import ValidationError


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

    class Meta:
        model  = Product
        fields = ('name', 'description', 'image', 'price', 'stock', 'category')


class AdminUpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'stock', 'category')


class AdminCategoryCreationForm(forms.ModelForm): 
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'category-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre category',
            }
        ),
    )
    confirm_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'category-confirm-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre category',
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'category-description',
                'class': 'admin-category', 
                'placeholder': 'Description de votre category',
            }
        )
    )

    def clean_confirm_name(self):
        """
        Confirm the category name given by 
        the admin is correct to avoid typos.
        """
        name = self.cleaned_data["name"]
        confirm_name = self.cleaned_data['confirm_name']
        if name != confirm_name:
            raise ValidationError("Category name doesn't match.")
        return name

    class Meta:
        model = Category
        fields = ('name', 'confirm_name', 'image', 'description')


class AdminEditCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'image', 'description')


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

