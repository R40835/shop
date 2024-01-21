from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Followers, Product, Category, FullPurchase, InstallementPurchase
from .forms import NewsLetterForm, AdminProductUploadForm, AdminSaleConfirmationForm


def is_superuser(user):
    """
    Checking if the user is an admin for security purposes.
    """
    return user.is_superuser


def index(request):
    """
    Landing Page.
    """
    return render(request, "products/index.html")


def about(request): 
    """
    About Page.
    """
    return render(request, "products/about.html")


def dresses(request): 
    """
    Dresses Page.
    """
    items = Product.objects.filter(category__name='dress').order_by('-created_at')
    items = [item.check_availabality() for item in items]
    items_per_page = 12
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page}
    return render(request, "products/dresses.html", context)


def blankets(request): 
    """
    Blankets Page.
    """
    is_admin = request.user.is_superuser
    print(is_admin)
    items = Product.objects.filter(category__name__icontains='couverture').order_by('-created_at')
    print(items)
    items = [item.check_availabality() for item in items]
    print([item for item in items])

    items_per_page = 12
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page, 'is_admin': is_admin}
    return render(request, "products/blankets.html", context)


def jackets(request): 
    """
    Blankets Page.
    """
    items = Product.objects.filter(category__name='jacket').order_by('-created_at')
    items = [item.check_availabality() for item in items]
    items_per_page = 12
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page}
    return render(request, "products/jackets.html", context)


def newsletter(request):
    """
    News Letter Page - For vistors keen to be notified about novelties.
    """
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            follower = Followers.objects.create(
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                preference=form.cleaned_data['preference']
            )
            follower.save()
            return redirect('products:index')
    else:
        form = NewsLetterForm()
    context = {'form': form}
    return render(request, "products/newsletter.html", context)


def search(request):
    """
    Searching for Categories/Products.
    """
    items = None
    if request.method == 'GET':
        query = request.GET.get('q')
        search_result = Product.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query)
        ).order_by('-created_at')
        if search_result.exists():
            items = search_result
        else:
            items = None
        context = {
            'searched': query,
            'items': items,
        }
        return render(request, 'products/search.html', context)
    

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
