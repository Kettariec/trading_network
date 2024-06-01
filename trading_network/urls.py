from trading_network.apps import TradingNetworkConfig
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NetworkNodeViewSet, ProductViewSet

app_name = TradingNetworkConfig.name
router = DefaultRouter()
router.register(r'network-nodes', NetworkNodeViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
] + router.urls
