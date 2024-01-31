from django import forms
from ..models import TopCategory, MidCategory, Product, Purchase, BottomCategory
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
    top_category = forms.ModelChoiceField(
        queryset=TopCategory.objects.all(), 
        required=True,
        widget=forms.Select(
            attrs={
                'id': "product-category",
                'class': 'admin-subcategory', 
                'placeholder': 'category',
            }
        )
    )    

    mid_category = forms.ModelChoiceField(
        queryset=MidCategory.objects.all(), 
        required=True,
        widget=forms.Select(
            attrs={
                'id': "product-category",
                'class': 'admin-upload', 
                'placeholder': 'Category',
            }
        )
    )
    bottom_category = forms.ModelChoiceField(
        queryset=BottomCategory.objects.all(), 
        required=False,
        widget=forms.Select(
            attrs={
                'id': "product-bottom-category",
                'class': 'admin-upload', 
                'placeholder': 'Bottom category',
            }
        )
    )

    class Meta:
        model  = Product
        fields = ('name', 'description', 'image', 'price', 'stock','top_category', 'mid_category', 'bottom_category')


class AdminUpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'stock', 'mid_category')


class AdminTopCategoryCreationForm(forms.ModelForm): 
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'top-category-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre category',
            }
        ),
    )
    confirm_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'top-category-confirm-name',
                'class': 'admin-category', 
                'placeholder': 'Nom de votre category',
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'top-category-description',
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
        model = TopCategory
        fields = ('name', 'confirm_name', 'image', 'description')



class AdminMidCategoryCreationForm(forms.ModelForm): 
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
    top_category = forms.ModelChoiceField(
        queryset=TopCategory.objects.all(), 
        required=True,
        widget=forms.Select(
            attrs={
                'id': "category-category",
                'class': 'admin-subcategory', 
                'placeholder': 'category',
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
        model = MidCategory
        fields = ('name', 'confirm_name', 'image', 'description', 'top_category')


class AdminEditMidCategoryForm(forms.ModelForm):
    class Meta:
        model = MidCategory
        fields = ('name', 'image', 'description')


class AdminBottomCategoryCreationForm(forms.ModelForm): 
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'subcategory-name',
                'class': 'admin-subcategory', 
                'placeholder': 'Nom de votre sous category',
            }
        ),
    )
    confirm_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'id': 'subcategory-confirm-name',
                'class': 'admin-subcategory', 
                'placeholder': 'Nom de votre sous category',
            }
        ),
    )
    description = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': 'subcategory-description',
                'class': 'admin-subcategory', 
                'placeholder': 'Description de votre sous category',
            }
        )
    )
    mid_category = forms.ModelChoiceField(
        queryset=MidCategory.objects.all(), 
        required=True,
        widget=forms.Select(
            attrs={
                'id': "subcategory-category",
                'class': 'admin-subcategory', 
                'placeholder': 'category',
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
        model = BottomCategory
        fields = ('name', 'confirm_name', 'image', 'description', 'mid_category')


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
        model  = Purchase
        fields = ('quantity')



