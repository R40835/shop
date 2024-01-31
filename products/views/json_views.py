from django.http import JsonResponse
from django.db.models import Q

from ..models import MidCategory, Product


def newsletter(request):
    """
    Json response containing unique categories of the shop products.
    """
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    choice = request.GET.get('choice')
    
    print(email, phone, choice)
    return JsonResponse({'response': 'success'})


def search_autocomplete(request):
    """
    Search Auto Complete, suggests items based on Products and Categories.
    """
    items = None
    if 'term' in request.GET:
        query = request.GET.get('term')
        search_results = Product.objects.filter(
            Q(name__icontains=query) |
            Q(mid_category__name__icontains=query)
        ).order_by('-created_at')[:5]
        if search_results.exists():
            items = [(item.image.url, item.name, item.price, item.mid_category.name, item.pk) for item in search_results]
    return JsonResponse({'items': items, 'searched': query}, safe=False)



