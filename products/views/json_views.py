from django.http import JsonResponse
from ..models import Category


def get_categories(request):
    """
    Json response containing unique categories of the shop products.
    """
    return JsonResponse({'categories': ''})
