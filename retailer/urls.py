# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .apps import RetailerConfig
from .views import ContactViewSet, SupplierViewSet, ProductViewSet

app_name = RetailerConfig.name

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
