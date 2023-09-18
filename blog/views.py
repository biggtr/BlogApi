from django.shortcuts import render
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.


class PostListApi(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class PostDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # lookup_field = "post_id"

    def get_object(self):
        post_id = self.kwargs["post_id"]
        return Post.objects.get(id=post_id)
