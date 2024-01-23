from django.urls import path
from .views import user_views, admin_views, json_views

app_name = 'products'

urlpatterns = [
    path('', user_views.index, name='index'),
    path('products-overview/', user_views.products, name='products'),
    path('about/', user_views.about, name='about'),
    path('dresses/', user_views.dresses, name='dresses'),
    path('blankets/', user_views.blankets, name='blankets'),
    path('news-letter/', user_views.newsletter, name='news-letter'),
    path('search/', user_views.search, name='search'),
    
    path('upload-content/', admin_views.admin_content_upload, name='upload-content'),
    path('confirm-sale/<int:product_pk>/', admin_views.admin_product_sold, name='confirm-sale'),
    path('create-category/', admin_views.admin_category_creation, name='create-category'),
    path('edit-category/<int:category_pk>/', admin_views.admin_edit_category, name='edit-category'),
    path('update-product/<int:product_pk>/', admin_views.admin_update_product, name='update-product'),

    path('get-categories/', json_views.get_categories, name='get-categories'),
    path('search-autocomplete/', json_views.search_autocomplete, name='search-autocomplete'),
]
 