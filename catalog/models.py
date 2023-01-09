from django.db import models

class CatalogCategory(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название категории')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class CatalogSubCategory(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название подкатегории')
    category = models.ForeignKey(CatalogCategory, on_delete=models.PROTECT, related_name='categories', verbose_name='Категория')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

class Product(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название продукта')
    description = models.TextField(blank=True, null=True, verbose_name='Описание продукта')
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Url', null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография продукта')
    subcategory = models.ForeignKey(CatalogSubCategory, null=True, on_delete=models.PROTECT, related_name='subcategory', verbose_name='Категория продукта')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class ProductСharacteristic(models.Model):
    сharacteristic = models.CharField(max_length=64, verbose_name='Характеристика')
    value = models.CharField(max_length=64, verbose_name='Название продукта')
    product = models.ForeignKey(Product, null=True, on_delete=models.PROTECT, related_name='characteristics', verbose_name='Продукт')

    def __str__(self):
        return self.сharacteristic
        
    class Meta:
        verbose_name = 'Характеристики для продуктов'
        verbose_name_plural = 'Характеристики для продуктов'

class Drawing(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Чертеж')
    product = models.ForeignKey(Product, null=True, on_delete=models.PROTECT, related_name='drawing', verbose_name='Продукт')

    def __str__(self):
        return 'Чертеж'
        
    class Meta:
        verbose_name = 'Чертеж для продукта'
        verbose_name_plural = 'Чертеж для продуктов'

class ProductsDiscounts(models.Model):
    text = models.CharField(max_length=64, verbose_name='Описание скидки')
    product = models.ForeignKey(Product, null=True, on_delete=models.PROTECT, related_name='discount', verbose_name='Продукт')

    def __str__(self):
        return 'Скидка'
        
    class Meta:
        verbose_name = 'Скидка для продукта'
        verbose_name_plural = 'Скидка для продуктов'

class CatalogItems(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    text = models.CharField(max_length=64, verbose_name='Описание')
    product = models.ForeignKey(CatalogCategory, null=True, on_delete=models.PROTECT, related_name='items', verbose_name='Категория')

    def __str__(self):
        return 'Каталог'
        
    class Meta:
        verbose_name = 'Каталог на главной странице'
        verbose_name_plural = 'Каталог на главной странице'

class RequestMessage(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя",)
    phone = models.CharField(max_length=12, verbose_name="Телефон",)
    address = models.CharField(max_length=64, verbose_name="Адрес")
    products = models.TextField(verbose_name="Продукты", null=True)
    inn = models.CharField(max_length=64, verbose_name="ИНН")
    comment = models.TextField(verbose_name="Комментарий к заказу",)
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Дата создания заявки")

    def __str__(self):
        return 'Заявка'
        
    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

class RequestConsultation(models.Model):
    name = models.CharField(max_length=32, verbose_name="Имя",)
    phone = models.CharField(max_length=12, verbose_name="Телефон",)

    def __str__(self):
        return 'Заявка'
        
    class Meta:
        verbose_name = 'Заявки на консультацию'
        verbose_name_plural = 'Заявки на консультацию'





