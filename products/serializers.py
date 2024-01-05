from django.db.models import Sum
from rest_framework import serializers, fields

from products.models import Products, ProductsCategory, Basket


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField('name', queryset=ProductsCategory.objects.all(),
                                            many=True)

    class Meta:
        model = Products
        fields = ('name', 'price', 'description', 'image', 'quantity', 'category')


class BasketSerializer(serializers.ModelSerializer):
    products = ProductSerializer()
    sum = fields.FloatField()
    total_price = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ('id', 'products', 'quantity', 'sum', 'total_price', 'total_quantity')

    def get_total_price(self, obj):
        return Basket.objects.filter(user_id=obj.user_id).total_price()

    def get_total_quantity(self, obj):
        return Basket.objects.filter(user_id=obj.user_id).total_quantity()
