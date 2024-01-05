from django.urls import path

from orders.views import OrderCreateView, OrdersDetailsView, OrderSuccessView, OrderCancelView

app_name = 'orders'

urlpatterns = [
    path('create-order/', OrderCreateView.as_view(), name='create-order'),
    path('my-orders/', OrdersDetailsView.as_view(), name='my-orders'),
    path('order_successc/', OrderSuccessView.as_view(), name='order_success'),
    path('order_canceled/', OrderCancelView.as_view(), name='order_canceled'),
]
