from django.urls import path
from orders.views import (CategoryListView, SubCategoryListView,
                         OrderListView, OrderDetailView)


urlpatterns = [
    path('all_category/', CategoryListView.as_view()),
    path('all_subcategory/', SubCategoryListView.as_view()),
    path('all_orders/', OrderListView.as_view()),
    path('order/<int:pk>', OrderDetailView.as_view()),

]