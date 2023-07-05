from rest_framework.routers import DefaultRouter
from apps.Order.api.views.order_viewsets import OrderViewSet
from apps.Order.api.views.items_viewsets import Items_OrderViewSet




router = DefaultRouter()
router.register(r'order',OrderViewSet, basename = 'order')
router.register(r'items_order',Items_OrderViewSet, basename = 'items_order')






urlpatterns = router.urls 