from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking, MenuItem


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = "__all__"
