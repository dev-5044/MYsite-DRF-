from rest_framework.response import Response
from rest_framework.views import APIView
from orders.models import Category, SubCategory, Order
from orders.serializers import (CategorySerializer, SubCategorySerializer,
                                OrderSerializer, OrderDetailSerializer,
                                CommentViewSerializer, CommentCreateSerializer)

class CategoryListView(APIView):
    """ Выводим список категорий """

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class SubCategoryListView(APIView):
    """ выводим список подкатегорий """

    def get(self, request, pk):
        subcategory = SubCategory.objects.filter(category_id=pk)
        serializer = SubCategorySerializer(subcategory, many=True)
        return Response(serializer.data)


class OrderListView(APIView):
    """ выводим список заказов """

    def get(self, request, pk):
        orders = Order.objects.filter(publish=True, sub_category_id=pk)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderDetailView(APIView):
    """ выводим детали заказа """

    def get(self, request, pk):
        order = Order.objects.get(id=pk)
        serializer = OrderDetailSerializer(order)
        return Response(serializer.data)


class CommentCreateView(APIView):
    """ создание комментария к заказу """

    def post(self, request, format=None):
        print(request.data)
        serializer = CommentCreateSerializer(data=request.data)
        request.data['user'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=404)
