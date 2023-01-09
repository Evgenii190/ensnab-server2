from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название услуги')
    subContent = models.TextField(verbose_name="Краткое описание услуги", null=True)
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Url')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография услуги')
    content = models.TextField(verbose_name="Описание услуги", null=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

class ServiceContent(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название услуги')
    category = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='service', verbose_name='Услуга')
    subContent = models.TextField(verbose_name="Описание услуги", null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография услуги')
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Услуга контент'
        verbose_name_plural = 'Услуги контент'

class ServiceSlider(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок на слайдере')
    category = models.ForeignKey(Service, on_delete=models.PROTECT, related_name='serviceSlug', verbose_name='Услуга')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография на слайдере')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Слайдер (услуги)'
        verbose_name_plural = 'Сладеры (услуги)'

class Сooperation(models.Model):
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Сотрудничество"
        
    class Meta:
        verbose_name = 'Сотрудничество (Имейте только одну запись)'
        verbose_name_plural = 'Сотрудничество (Имейте только одну запись)'



