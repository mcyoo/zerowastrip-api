from rest_framework.routers import DefaultRouter
from . import views


app_name = "cafes"
router = DefaultRouter()
router.register("", views.CafeViewSet)

urlpatterns = router.urls
