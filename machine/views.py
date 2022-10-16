from rest_framework import generics, viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from .models import Machine
from .serializers import MachineSerializer


class MachineViewSet(viewsets.ModelViewSet):
    serializer_class = MachineSerializer 
    permission_classes = (IsAuthenticated, )
    queryset = Machine.objects.all()
    

class FreeMachineListView(generics.ListAPIView):
    serializer_class = MachineSerializer 
    permission_classes = (IsAuthenticated, )
    queryset = Machine.objects.filter(is_free=True)

    