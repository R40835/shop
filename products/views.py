from django.shortcuts import render, redirect
from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Followers, Product, Category, FullPurchase, InstallementPurchase
from .forms import NewsLetterForm, AdminProductUploadForm, AdminSaleConfirmationForm


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
    

#@login_required
def admin_content_upload(request):
    """
    Admin - Sending emails to the followers upon admin new content upload.
    """
    followers = Followers.objects.all()
    if request.method == 'POST':
        form = AdminProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if followers.exists():
                connection = mail.get_connection()
                connection.open()
                for follower in followers:
                    email = EmailMessage(
                        'New Content!',
                        'Dear Customer\n\nWe\'ve got brand new products that may be of interest to you. Check it out! 127.0.0.1:8000', 
                        settings.EMAIL_HOST_USER,
                        [f'{follower.email}'],
                        connection=connection,
                    )
                    connection.send_messages([email])
                connection.close()
            return redirect('products:index')
    else:
        form = AdminProductUploadForm()
        print(form.fields)
    context = {'form': form}
    return render(request, "admin/upload_content.html", context)



@login_required
def admin_product_sold(request, product_pk):
    """
    Admin - Confirm sale and update stock.
    """
    is_admin = request.user.is_superuser
    if is_admin:
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
    else:
        print("Action forbidden! (render a template later)")