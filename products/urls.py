from django.urls import path

from products.views import ProductsListView, add_basket, delete_basket

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='products'),
    path('category/<int:product_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('basket/add/<int:product_id>/', add_basket, name='add_basket'),
    path('basket/del/<int:basket_id>/', delete_basket, name='delete_basket'),
]
