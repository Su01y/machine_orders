from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'booking', BookingViewSet, basename='booking')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]
