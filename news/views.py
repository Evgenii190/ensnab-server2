from rest_framework import viewsets
from.models import News, NewsContent

from .serializers import NewsSerializer, NewsContentSerializer, LastNewsSerializer
from rest_framework.response import Response


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    def retrieve(self, request, pk=None):
        queryset = NewsContent.objects.filter(category__slug=pk)
        serializer = NewsContentSerializer(queryset, many=True)
        return Response(serializer.data)

class TwoNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-pk')[:2]
    serializer_class = LastNewsSerializer
