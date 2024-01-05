from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from common.mixin import TitleMixin
from products.models import Basket, Products, ProductsCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'Store'


class ProductsListView(TitleMixin, ListView):
    model = Products
    title = 'Store'
    template_name = 'products/products.html'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['categories'] = ProductsCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        product_id = self.kwargs.get('product_id')
        queryset = queryset.filter(category=product_id) if product_id else queryset
        return queryset


@login_required
def add_basket(request, product_id):
    product = Products.objects.get(id=product_id)
    basket = Basket.objects.filter(products=product, user=request.user)

    if not basket.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
        messages.success(request, 'Item added to cart')
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()
        messages.success(request, 'The item was successfully added to the cart.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_basket(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    messages.success(request, f'The item was successfully removed from the cart.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
