from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import post_view, add_comment

router = DefaultRouter()
# router.register('products', ProductViewSet)
# router.register('stocks', StockViewSet)

urlpatterns = [
    path('', post_view, name='post_view'),
    path('add_comment/<int:post_id>', add_comment, name='add_comment'),
]

# urlpatterns = +router.urls