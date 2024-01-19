from django.contrib import admin
from .models import Products, Contact, Subscribe_sending_email
# Register your models here.


class ConatctAdmin(admin.ModelAdmin):
    list_display = ('first_name','email','Comments')

admin.site.register(Contact,ConatctAdmin)