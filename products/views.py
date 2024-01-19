from django.shortcuts import render


def index(request):
    """
    Landing page.
    """
    return render(request, "products/index.html")