from django.contrib import admin
from .models import Products, Contact, Subscribe_sending_email
# Register your models here.


class ConatctAdmin(admin.ModelAdmin):
    display_list = ('first_name','email','Comments')

admin.site.regester(ConatctAdmin,Contact)