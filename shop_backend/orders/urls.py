from django.urls import path

from orders.apps import OrdersConfig
from orders.views import OrderCreateView

app_name = OrdersConfig.name

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create')
]
