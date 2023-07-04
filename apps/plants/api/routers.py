from rest_framework.routers import DefaultRouter
from apps.plants.api.views.plant_viewset import PlantsViewSet
from apps.plants.api.views.category_viewset import CategoryViewSet



router = DefaultRouter()
router.register(r'category',CategoryViewSet, basename = 'category')
router.register(r'plants',PlantsViewSet, basename = 'plants')






urlpatterns = router.urls 