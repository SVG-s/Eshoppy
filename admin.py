from django.contrib import admin
from .models import Offer, Product


class OfferAdmin(admin.ModelAdmin):
     list_display = ('code', 'discount')  # fields to display in the admin panel

class ProductAdmin(admin.ModelAdmin):
     list_display = ('name', 'price', 'stock')  # fields to display in the admin panel
    

admin.site.register(Product, ProductAdmin)  # adding product section to the admin panel
admin.site.register(Offer, OfferAdmin)  # adding offer section to the admin panel


