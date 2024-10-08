from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    toggle_activity,
)

app_name = BlogConfig.name

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("blog/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("update/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("activity/<int:pk>/delete/", toggle_activity, name="toggle_activity"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
