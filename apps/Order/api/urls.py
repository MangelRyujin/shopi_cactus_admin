from django.urls import path
from apps.Order.api.views.created_order_view import create_order_api_view
# ,create_items_order_api_view

urlpatterns = [
    path('order/', create_order_api_view, name ='order'),
    # path('items_order/', create_items_order_api_view, name ='order'),
    
]