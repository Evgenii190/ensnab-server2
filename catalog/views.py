from rest_framework import viewsets
from.models import Product, CatalogCategory, ProductsDiscounts, CatalogItems, RequestMessage, RequestConsultation
from .serializers import ProductSerializer, CatalogSerializer, ProductsDiscountsSerializer, CatalogItemsSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.views import APIView


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = CatalogCategory.objects.all()
    serializer_class = CatalogSerializer


class ProductsByTitleViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def retrieve(self, request, pk=None):
        queryset = Product.objects.filter(subcategory__title=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductsSimilarViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def retrieve(self, request, pk=None):
        queryset = Product.objects.filter(subcategory=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def retrieve(self, request, pk=None):
        queryset = Product.objects.filter(slug=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data[0])

class ProductsDiscountViewSet(viewsets.ModelViewSet):
    queryset = ProductsDiscounts.objects.all()
    serializer_class = ProductsDiscountsSerializer


class CatalogProductsViewSet(viewsets.ModelViewSet):
    queryset = CatalogItems.objects.all()
    serializer_class = CatalogItemsSerializer

class RequestMessageAPIView(APIView):
    def post(self, request):
        new_requset = RequestMessage.objects.create(
            name = request.data['name'],
            phone = request.data['phone'],
            inn = request.data['inn'],
            address = request.data['address'],
            comment = request.data['comment'],
            products = request.data['products']
        )
        return Response({'request': model_to_dict(new_requset)})

class RequestConsultationAPIView(APIView):
    def post(self, request):
        print(request)
        new_requset = RequestConsultation.objects.create(
            name = request.data['name'],
            phone = request.data['phone'],
        )
        return Response({'request': model_to_dict(new_requset)})
