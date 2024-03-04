from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("menu/", views.menu, name="menu"),
    path("menu-items/", views.MenuItemView.as_view(), name="menu_item"),
    path(
        "menu-items/<int:pk>/",
        views.SingleMenuItemView.as_view(),
        name="single_menu_item",
    ),
    path("bookings_all/", views.bookings, name="bookings_all"),
    path("bookings/", views.bookings_data, name="bookings"),
]
