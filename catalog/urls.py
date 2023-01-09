from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'catalogList', CatalogViewSet)
router.register(r'products', ProductsByTitleViewSet)
router.register(r'product', ProductViewSet)
router.register(r'similaryProducts', ProductsSimilarViewSet)
router.register(r'discounts', ProductsDiscountViewSet)
router.register(r'catalogProducts', CatalogProductsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('request', RequestMessageAPIView.as_view()),
    path('requestConsultation', RequestConsultationAPIView.as_view()),
]
