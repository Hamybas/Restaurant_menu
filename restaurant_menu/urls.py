from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path("menu_item", views.MenuItemDetail.as_view(), name="menu_item")
]