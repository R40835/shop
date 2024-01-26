from django.http import JsonResponse
from .models import Category


def categories(request):
    """
    Unique categories of the shop products.
    """
    is_admin: bool = request.user.is_superuser
    categories = Category.objects.distinct('name')
    print(categories)
    return {'categories': categories, 'is_admin': is_admin}
