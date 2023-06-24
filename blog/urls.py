from django.urls import path
from blog.views import PostListAPIView, PostDetailAPIView

urlpatterns = [
    path("api/posts/", PostListAPIView.as_view(), name="post-list"),
    path("api/posts/<int:pk>/", PostDetailAPIView.as_view(), name="post-detail"),
]
