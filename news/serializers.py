from rest_framework import serializers
from .models import News, NewsContent

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class LastNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NewsContentSerializer(serializers.ModelSerializer):
    news = serializers.CharField(source='category')
    class Meta:
        model = NewsContent
        fields = '__all__'