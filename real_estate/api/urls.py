from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('unit', views.unit, name="unit"),
    path('tenant', views.tenant, name="tenant"),
    path('vendor', views.vendor, name="vendor"),
    path('lease', views.lease, name="lease"),
    path('payment', views.payment, name="payment"),
    path('expense', views.expense, name="expense"),
]
