from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("customer.urls")),
    path("api/", include("product.urls")),
    path("api/", include("employee.urls")),
    path("api/", include("taskboard.urls")),
    path("api/", include("auth.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", TemplateView.as_view(template_name="index.html")),
    path("manage", TemplateView.as_view(template_name="manage.html")),
]
