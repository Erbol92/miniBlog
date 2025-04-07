from django.urls import path

from .views import post_view, add_comment


urlpatterns = [
    path('', post_view, name='post_view'),
    path('add_comment/<int:post_id>', add_comment, name='add_comment'),
]

