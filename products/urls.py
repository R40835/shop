from django.contrib import admin
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('dresses/', views.dresses, name='dresses'),
    path('blankets/', views.blankets, name='blankets'),
    path('upload-content/', views.admin_content_upload, name='upload-content'),
    path('news-letter/', views.newsletter, name='news-letter'),
    path('search/', views.search, name='search'),
]
