
from rest_framework.routers import DefaultRouter
from .views import LostPetViewSet

router = DefaultRouter()
router.register(r'lost-pets', LostPetViewSet, basename='lostpet')

urlpatterns = router.urls
