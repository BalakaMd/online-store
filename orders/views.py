from django.conf import settings
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from common.mixin import TitleMixin
from orders.forms import OrderForm


class OrderSuccessView(TitleMixin, TemplateView):
    template_name = 'orders/success_payment.html'
    title = 'Success Payment'


class OrderCancelView(TitleMixin, TemplateView):
    template_name = 'orders/canceled_payment.html'
    title = 'Canceled Payment'


class OrderCreateView(TitleMixin, CreateView):
    form_class = OrderForm
    title = 'Order'
    template_name = 'orders/order-create.html'
    success_url = reverse_lazy('orders:order_success')

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)


class OrdersDetailsView(TitleMixin, TemplateView):
    title = 'Orders Details'
    template_name = 'orders/orders.html'
