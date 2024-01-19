from django.shortcuts import render, redirect
from django.core import mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.decorators import login_required

from .models import Followers, Dress, Blanket
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
    return render(request, "products/dresses.html")


def blankets(request): 
    """
    Blankets Page.
    """
    return render(request, "products/blankets.html")


def newsletter(request):
    """
    For vistors keen to be notified about novelties.
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
