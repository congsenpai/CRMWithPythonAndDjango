from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet

# Tạo router và đăng ký viewset
router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer')

# Bao gồm router URLs
urlpatterns = router.urls
