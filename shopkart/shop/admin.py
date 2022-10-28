from django.contrib import admin
from .models import *

"""
#Show admin panel in name, image, description field
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')
    admin.site.register(Catagory,CategoryAdmin)
"""

admin.site.register(Catagory)
admin.site.register(Product)

# Register your models here.
