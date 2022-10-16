from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Booking

from. serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer 
    queryset = Booking.objects.all()
    permission_classes = (IsAuthenticated, )

