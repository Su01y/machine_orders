from rest_framework import serializers

from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    is_actual = serializers.HiddenField(default=True)

    class Meta:
        model = Booking
        fields = "__all__"

    
    
    
