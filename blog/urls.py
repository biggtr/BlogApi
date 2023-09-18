from django.urls import path
from .views import PostListApi, PostDetailApi

urlpatterns = [
    path("post/", PostListApi.as_view(), name="post-list"),
    path("post/<int:post_id>", PostDetailApi.as_view(), name="post-detail"),
]
