from rest_framework.response import Response
from rest_framework.views import APIView
from orders.models import Category, SubCategory, Order
from orders.serializers import (CategorySerializer, SubCategorySerializer,
                                OrderSerializer, OrderDetailSerializer)

class CategoryListView(APIView):
    """ Выводим список категорий """

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class SubCategoryListView(APIView):
    """ выводим список подкатегорий """

    def get(self, request):
        subcategory = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategory, many=True)
        return Response(serializer.data)


class OrderListView(APIView):
    """ выводим список заказов """

    def get(self, request):
        orders = Order.objects.filter(publish=True)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetailView(APIView):
    """ выводим детали заказа """

    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)