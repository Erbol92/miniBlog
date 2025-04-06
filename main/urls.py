from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import post_view

router = DefaultRouter()
# router.register('products', ProductViewSet)
# router.register('stocks', StockViewSet)

urlpatterns = [
    path('', post_view, name='post_view'),
]

# urlpatterns = +router.urls