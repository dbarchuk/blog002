from django.urls import path
from . import views


urlpatterns = [
    path("", views.posts_list),
    path("<id>/", views.post_detail),
    path("list", views.PostsListView.as_view())
]
