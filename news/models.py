from django.db import models

class News(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название новости')
    content = models.TextField(verbose_name="Краткое описание новости", null=True)
    slug = models.SlugField(max_length=64, unique=True, verbose_name='Url')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография новости')

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class NewsContent(models.Model):
    title = models.CharField(max_length=64, verbose_name='Название услуги')
    category = models.ForeignKey(News, on_delete=models.PROTECT, related_name='news', verbose_name='Услуга')
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Новость контент'
        verbose_name_plural = 'Новости контент'


