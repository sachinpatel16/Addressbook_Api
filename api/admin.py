from django.contrib import admin

# Register your models here.
from api.models import Addres

class AddresAdmin(admin.ModelAdmin):
    list_display = ['addres','city','state','country']

admin.site.register(Addres,AddresAdmin)