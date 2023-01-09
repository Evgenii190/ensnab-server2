from django.contrib import admin

from django.contrib import admin

from .models import News, NewsContent
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class NewsContentFormAdmin(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = NewsContent
        fields = '__all__'

class NewsContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_display_links = ('id', 'title')
    form = NewsContentFormAdmin

admin.site.register(News, NewsAdmin)
admin.site.register(NewsContent, NewsContentAdmin)