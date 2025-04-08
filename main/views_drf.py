from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .paginators import StandardResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class PostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['title', 'author']

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status': 'OK'})


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({'status': 'OK'})
