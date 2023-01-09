from rest_framework import serializers
from .models import CatalogCategory, CatalogSubCategory, Product, ProductСharacteristic, Drawing, ProductsDiscounts, CatalogItems

class CatalogSubSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    class Meta:
        model = CatalogSubCategory
        fields = '__all__'

class ProductСharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductСharacteristic
        fields = '__all__'

class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='subcategory.title')
    characteristics = ProductСharacteristicSerializer(many = True, read_only = True)
    drawing = DrawingSerializer(many = True, read_only = True)
    class Meta:
        model = Product
        fields = '__all__'

class CatalogSerializer(serializers.ModelSerializer):
    categories = CatalogSubSerializer(many = True, read_only = True)
    class Meta:
        model = CatalogCategory
        fields = '__all__'

class ProductsDiscountsSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(source='product.slug')
    title = serializers.CharField(source='product.title')
    photo = serializers.CharField(source='product.photo')
    class Meta:
        model = ProductsDiscounts
        fields = '__all__'

class CatalogItemsSerializer(serializers.ModelSerializer):
    source = serializers.CharField(source='product.title')
    class Meta:
        model = CatalogItems
        fields = '__all__'


