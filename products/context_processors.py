from .models import TopCategory, MidCategory, BottomCategory


def clothing_products(request):
    """
    Unique categories and sub-categories of the clothing products.
    """
    clothing = MidCategory.objects.filter(
        top_category__name='CLOTHING'
    ).order_by('created_at') 
    return {'clothing': clothing}


def garniture_products(request):
    """
    Unique categories and sub-categories of the garniture products.
    """
    garniture = MidCategory.objects.filter(
        top_category__name='LINENS & TEXTILES'
    ).order_by('-created_at') 
    return {'garniture': garniture}



