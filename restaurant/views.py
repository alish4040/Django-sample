from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Menu
from django.core import serializers
from .models import Booking
from datetime import datetime
import json
from .forms import BookingForm
from .serializers import MenuSerializer, BookingSerializer, MenuItemSerializer


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def book(request):
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "book.html", context)


# Add code for the bookings() view
@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        exist = (
            Booking.objects.filter(reservation_date=data["reservation_date"])
            .filter(reservation_slot=data["reservation_slot"])
            .exists()
        )
        if exist == False:
            booking = Booking(
                first_name=data["first_name"],
                reservation_date=data["reservation_date"],
                reservation_slot=data["reservation_slot"],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type="application/json")

    bookings_all = Booking.objects.all()
    booking_json = serializers.serialize("json", bookings_all)

    return render(
        request,
        "bookings.html",
        context={"booking": booking_json},
    )


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "menu.html", {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})


@csrf_exempt
def bookings_data(request):
    if request.method == "POST":
        data = json.load(request)
        exist = (
            Booking.objects.filter(reservation_date=data["reservation_date"])
            .filter(reservation_slot=data["reservation_slot"])
            .exists()
        )
        if exist == False:
            booking = Booking(
                first_name=data["first_name"],
                reservation_date=data["reservation_date"],
                reservation_slot=data["reservation_slot"],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type="application/json")

    date = request.GET.get("date", datetime.today().date())
    if date == "":
        date = datetime.today().date()

    bookings_filtered = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize("json", bookings_filtered)

    return HttpResponse(booking_json, content_type="application/json")


class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
