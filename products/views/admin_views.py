from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q

from ..models import Follower, Product, Category, FullPurchase, InstallementPurchase

from ..forms.admin_forms import AdminProductUploadForm, AdminSaleConfirmationForm, AdminInstallementSaleForm, \
                                AdminCategoryCreationForm, AdminEditCategoryForm, AdminUpdateProductForm


def is_superuser(user):
    """
    Checking if the user is an admin for security purposes.
    """
    return user.is_superuser
    

@login_required
@user_passes_test(is_superuser)
def admin_content_upload(request):
    """
    Admin - Sending emails to the followers upon admin new content upload.
    """
    if request.method == 'POST':
        form = AdminProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:index')
    else:
        form = AdminProductUploadForm()
        print(form.fields)
    context = {'form': form}
    return render(request, "admin/upload_content.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_product_sold(request, product_pk):
    """
    Admin - Confirm sale and update stock.
    """
    product = Product.objects.get(pk=product_pk)
    if request.method == 'POST':
        form = AdminSaleConfirmationForm(request.POST)
        if form.is_valid():
            FullPurchase.objects.create(
                quantity=form.cleaned_data['quantity'],
                product_id=product_pk
            )
            return redirect('products:index')
    else:
        form = AdminSaleConfirmationForm()
    context = {'form': form, 'product': product}
    return render(request, "admin/confirm_sale.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_category_creation(request):
    """
    Admin - Create a new unique category.
    """
    if request.method == 'POST':
        form = AdminCategoryCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:index')
    else:
        form = AdminCategoryCreationForm()
    context = {'form': form}
    return render(request, "admin/create_category.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_edit_category(request, category_pk):
    """
    Admin - Create a new unique category.
    """
    category = Category.objects.get(pk=category_pk)
    if request.method == 'POST':
        form = AdminEditCategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('products:index')
    form = AdminEditCategoryForm(instance=category)
    context = {'form': form}
    return render(request, "admin/update_category.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_update_product(request, product_pk):
    """
    Admin - Create a new unique category.
    """
    product = Product.objects.get(pk=product_pk)
    if request.method == 'POST':
        form = AdminUpdateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:index')
    form = AdminUpdateProductForm(instance=product)
    context = {'form': form}
    return render(request, "admin/update_product.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_full_purchases(request):
    """
    Admin - Purchases Page.
    """
    purchases = FullPurchase.objects.all()
    items_per_page = 12
    paginator = Paginator(purchases, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page}
    return render(request, "admin/full_purchases.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_full_purchase_details(request, product_pk):
    """
    Admin - Products' Full Purchase Details Page.
    """
    purchase = FullPurchase.objects.get(product_id=product_pk)
    context = {'purchase': purchase}
    return render(request, "admin/full_purchase_details.html", context)


@login_required
@user_passes_test(is_superuser)
def admin_installement_purchases(request):
    """
    Admin - Products' Installement Purchases Page.
    """
    purchases = InstallementPurchase.objects.all()
    items_per_page = 12
    paginator = Paginator(purchases, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page}
    return render(request, "admin/installement_purchases.html", context)

