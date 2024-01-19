from django.shortcuts import render, redirect
from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Followers, Dress, Blanket, Category
from .forms import NewsLetterForm, AdminDressUploadForm


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
    items = Dress.objects.all().order_by('-created_at')
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
    items = Blanket.objects.all().order_by('-created_at')
    items_per_page = 12
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'page': page}
    return render(request, "products/blankets.html", context)


def newsletter(request):
    """
    News Letter Page - For vistors keen to be notified about novelties.
    """
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            follower = Followers(
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
    Searching for Categories.
    """
    items = None
    if request.method == 'GET':
        query = request.GET.get('q')
        # search_result = Category.objects.filter(
        #     Q(dress__name__icontains=query) | 
        #     Q(blanket__name__icontains=query)
        # ).all()#.order_by('-created_at')
        search_result = Dress.objects.filter(
            Q(name__icontains=query) 
        ).all()#.order_by('-created_at')
        if search_result.exists():
            items = search_result
        else:
            items = None
        context = {
            'searched': query,
            'items': items,
        }
        print(f'items: {items} serached: {query}')
        return render(request, 'products/search.html', context)
    

#@login_required
def admin_content_upload(request):
    """
    Sending emails to the followers upon admin new content upload.
    """
    followers = Followers.objects.all()
    if request.method == 'POST':
        form = AdminDressUploadForm(request.POST, request.FILES)
        if form.is_valid():
            dress = Dress(
                #add category | type
                name=form.cleaned_data['name'],
                image=form.cleaned_data['image'],
                price=form.cleaned_data['price'],
            )
            dress.save()
            
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
        form = AdminDressUploadForm()
    context = {'form': form}
    return render(request, "admin/upload_content.html", context)
