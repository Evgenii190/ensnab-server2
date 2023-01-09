
from rest_framework import viewsets

from.models import Service, ServiceContent, ServiceSlider, Сooperation

from .serializers import ServicesSerializer, ServiceContentSerializer, ServiceSliderSerializer, СooperationSerializer
from rest_framework.response import Response


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServicesSerializer
    def retrieve(self, request, pk=None):
        queryset = ServiceContent.objects.filter(category__slug=pk)
        serializer = ServiceContentSerializer(queryset, many=True)
        return Response(serializer.data)

class ServicesSliderViewSet(viewsets.ModelViewSet):
    queryset = ServiceSlider.objects.all()
    serializer_class = ServiceSliderSerializer

class СooperationViewSet(viewsets.ModelViewSet):
    queryset = Сooperation.objects.all()
    serializer_class = СooperationSerializer


