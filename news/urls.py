from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'newsList', NewsViewSet)
router.register(r'lastNews', TwoNewsViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
