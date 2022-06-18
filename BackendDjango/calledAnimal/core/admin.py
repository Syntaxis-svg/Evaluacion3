from django.contrib import admin
from .models import Marca, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'precio', 'marca']
    search_fields = ['nombre', 'precio', 'marca']
    list_per_page = 15
    

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)