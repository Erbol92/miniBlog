from django.urls import path

from .views_drf import PostView, CommentView, PostDetailView

urlpatterns = [
    path('posts', PostView.as_view()),
    path('posts/<int:pk>/',PostDetailView.as_view()),
    path('comments', CommentView.as_view()),
]
