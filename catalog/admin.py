from django.contrib import admin

from .models import CatalogCategory, CatalogSubCategory, Product, ProductСharacteristic, Drawing, ProductsDiscounts, CatalogItems, RequestMessage, RequestConsultation

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')


class CategorySubAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'subcategory')
    list_display_links = ('id', 'title')

class ProductСharacteristicAdmin(admin.ModelAdmin):
    list_display = ('id', 'сharacteristic', 'value')
    list_display_links = ('id', 'сharacteristic')

class DrawingAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')
    list_display_links = ('id', 'photo')

class DiscountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')

class CatalogItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')
    list_display_links = ('id', 'text')


class RequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address', 'inn', 'comment', "created_at")
    list_display_links = ('name', 'phone')

class RequestConsultaitonAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', )
    list_display_links = ('name', 'phone')


admin.site.register(CatalogCategory, CategoryAdmin)
admin.site.register(CatalogSubCategory, CategorySubAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductСharacteristic, ProductСharacteristicAdmin)
admin.site.register(Drawing, DrawingAdmin)
admin.site.register(ProductsDiscounts, DiscountsAdmin)
admin.site.register(CatalogItems, CatalogItemsAdmin)
admin.site.register(RequestMessage, RequestAdmin)
admin.site.register(RequestConsultation, RequestConsultaitonAdmin)

