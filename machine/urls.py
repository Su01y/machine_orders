from django.urls import include, path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'machine', MachineViewSet, basename='machine')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/machinelist/free/', FreeMachineListView.as_view())
]
