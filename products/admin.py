from django.contrib import admin
from .models import Product, Category, Follower


class AdminProduct(admin.ModelAdmin):
    list_display = ('name',)


class AdminCategory(admin.ModelAdmin):
    list_display = ('name',)


class AdminFollowers(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Product, AdminProduct)

admin.site.register(Category, AdminCategory)

admin.site.register(Follower, AdminFollowers)


