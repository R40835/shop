from django.http import JsonResponse
from django.db.models import Q
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


from ..models import MidCategory, Product, Follower


def newsletter(request):
    """
    This endpoint receives data from the client to create a new db entry and returns 
    a Json response to reflect the success or the failure of the operation. 
    """
    email = request.GET.get('email')
    confirm_email = request.GET.get('confirm_email')
    choice = request.GET.get('choice')

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({'response': 'invalid-email'})
    
    if email == confirm_email:
        _, new_follower = Follower.objects.get_or_create(
            email=email,
            category=choice
        )
        if new_follower:
            response = 'success'
        else:
            response = 'failure'
        return JsonResponse({'response': response})
    else:
        return JsonResponse({'response': 'unmatching-email'})


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
            items = [
                (
                    item.image.url, 
                    item.name, 
                    item.price, 
                    item.mid_category.name, 
                    item.pk
                ) for item in search_results
            ]
    return JsonResponse({'items': items, 'searched': query}, safe=False)



