from django.urls import path
from orders.views import (CategoryListView, SubCategoryListView,
                         OrderListView, OrderDetailView, CommentCreateView)


urlpatterns = [
    path('all_category/', CategoryListView.as_view()),
    path('category/<int:pk>/', SubCategoryListView.as_view()),
    path('subcategory/<int:pk>/orders/', OrderListView.as_view()),
    path('order/<int:pk>', OrderDetailView.as_view()),
    path('create_comment/', CommentCreateView.as_view()),

]