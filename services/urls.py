from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'servicesList', ServicesViewSet)
router.register(r'servicesSlider', ServicesSliderViewSet)
router.register(r'cooperation', СooperationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
