from django.contrib import admin
from .models import Product, Category, Follower, ProductImages


class AdminProduct(admin.ModelAdmin):
    list_display = ('name',)


class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)


class AdminFollowers(admin.ModelAdmin):
    list_display = ('email',)


class AdminProductImages(admin.ModelAdmin):
    list_display = ('image',)


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Follower, AdminFollowers)
admin.site.register(ProductImages, AdminProductImages)



