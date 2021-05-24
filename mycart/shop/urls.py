
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TracingStatus"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.ProductView, name="ProductView"),
    path("Checkout/", views.checkout, name="CheckOut"),
]


