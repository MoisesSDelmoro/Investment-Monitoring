from django.urls import path
from .views import list_stocks,create_stock,edit_stock,delete_stock

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("lista/", list_stocks, name="list_stocks"),
    path("novo/",create_stock, name="create_stock"),
    path("editar/<int:id>/",edit_stock, name='edit_stock'),
    path("deletar/<int:id>/",delete_stock, name='delete_stock'),
]