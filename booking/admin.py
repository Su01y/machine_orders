from typing import Any

from django.contrib import admin

from booking.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    exclude = ('creator',)

    def save_model(self, request: Any, obj, form: Any, change: Any) -> None:
        if not obj.pk:
            obj.creator = request.user
        return super().save_model(request, obj, form, change)