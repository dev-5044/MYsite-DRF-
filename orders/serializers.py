from orders.models import Category, Image, SubCategory, Order, Comment
from rest_framework.fields import CurrentUserDefault
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    """ список категорий """

    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    """ список подкатегорий """
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = SubCategory
        fields = '__all__'


class CommentCreateSerializer(serializers.ModelSerializer):
    """ добавление комментария """

    class Meta:
        model = Comment
        fields = "__all__"


class CommentViewSerializer(CommentCreateSerializer):
    """ отображение полей комментария """
    user = serializers.SlugRelatedField(slug_field='name', read_only=True)
    order = serializers.SlugRelatedField(slug_field='name', read_only=True)


class OrderSerializer(serializers.ModelSerializer):
    """ список заказов """

    class Meta:
        model = Order
        fields = ['name', 'city', 'updated_on', 'id']


class OrderDetailSerializer(serializers.ModelSerializer):
    """ заказ подробно """
    user = serializers.SlugRelatedField(slug_field='name', read_only=True)
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    sub_category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    comments = CommentViewSerializer(many=True)
    image = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'


